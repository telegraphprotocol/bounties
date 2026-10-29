'use strict';

const {
  parseState,
  snapshotReward,
  quoteMarkdown,
  permissionAllowsMaintenance,
} = require('./bounty_state');
const { STATUS_LABELS, reconcileIssue, recordTransition } = require('./bounty_journal');
const COMMANDS = new Set(['/claim', '/progress', '/release', '/submit', '/open', '/block', '/unblock', '/changes', '/approve', '/done']);
const MENTION = /^@([A-Za-z0-9][A-Za-z0-9-]{0,38})$/;

module.exports = async function runBountyCommand({ github, context }) {
  const event = context.payload.comment;
  const raw = String(event?.body || '').trim();
  if (raw.length > 8192) return;

  const [command, ...rest] = raw.split(/\s+/);
  if (!COMMANDS.has(command)) return;
  const payload = rest.join(' ').trim();
  const owner = context.repo.owner;
  const repo = context.repo.repo;
  const issue_number = context.issue.number;
  const actor = context.actor;
  if (!Number.isSafeInteger(event.id) || event.id <= 0 || event.user?.type !== 'User' ||
      event.user.login.toLowerCase() !== String(actor).toLowerCase() ||
      !/^[A-Za-z0-9][A-Za-z0-9-]{0,38}$/.test(actor)) return;
  const source = `comment:${event.id}`;

  const issueResp = await github.rest.issues.get({ owner, repo, issue_number });
  let issue = issueResp.data;
  const labelNames = () => issue.labels.map(l => typeof l === 'string' ? l : l.name);

  async function comment(body) {
    await github.rest.issues.createComment({ owner, repo, issue_number,
      body: `<!-- telegraph-reject source="${source}" -->\n${body}` });
  }
  async function comments() {
    return github.paginate(github.rest.issues.listComments, { owner, repo, issue_number, per_page: 100 });
  }
  async function transition(body) {
    await recordTransition({ github, owner, repo, issue_number, source, body });
  }

  const all = await comments();
  const state = parseState(all);
  // Recover a prior accepted command before considering this delivery again.
  if (state.processedSources.has(source)) {
    await reconcileIssue({ github, owner, repo, issue_number, state });
    return;
  }
  if (issue.state !== 'open' || issue.pull_request) return;
  const current = (await github.rest.issues.getComment({ owner, repo, comment_id: event.id })).data;
  if (current.body !== event.body || current.user?.login?.toLowerCase() !== actor.toLowerCase()) return;
  issue = await reconcileIssue({ github, owner, repo, issue_number, state });
  const statuses = labelNames().filter(label => STATUS_LABELS.has(label));
  if (statuses.length !== 1 || statuses[0] === 'status:done') return;
  const now = new Date().toISOString();

  let maintainerPermission;
  async function isMaintainer() {
    if (maintainerPermission !== undefined) return maintainerPermission;
    try {
      const resp = await github.rest.repos.getCollaboratorPermissionLevel({ owner, repo, username: actor });
      maintainerPermission = permissionAllowsMaintenance(resp.data?.permission);
    } catch (_) {
      maintainerPermission = false;
    }
    return maintainerPermission;
  }

  // Provider recruitment follows a separate commercial process, so bounty commands are unavailable.
  if (labelNames().includes('opportunity:provider') &&
      ['/claim', '/progress', '/release', '/submit', '/changes', '/approve', '/done'].includes(command)) {
    await comment('This is a commercial Provider onboarding opportunity. Follow its public contact instructions; onboarding and any terms are coordinated through the separate commercial process.');
    return;
  }

  const lower = user => String(user || '').toLowerCase();
  const claimOf = user => state.claimants.find(c => lower(c.user) === lower(user));
  const pendingOf = user => state.pendingSubmitters.find(u => lower(u) === lower(user));
  // "/cmd @user rest": the named user (if any) and the rest of the text.
  const [firstWord, ...restWords] = payload.split(/\s+/);
  const named = MENTION.test(firstWord || '') ? firstWord.slice(1) : null;
  const reason = named ? restWords.join(' ').trim() : payload;

  if (command === '/claim') {
    // Several people can work on one bounty: anyone can join while it is open, claimed or in review.
    if (!['status:open', 'status:claimed', 'status:review'].includes(statuses[0])) {
      await comment('This Issue is not currently open for claiming. Only `status:open` bounties, or ones others are already working on, can be claimed.');
      return;
    }
    if (claimOf(actor)) {
      await comment(`@${actor}, you have already claimed this bounty. Post \`/progress ...\` to keep your claim.`);
      return;
    }

    const reward = snapshotReward(issue.body);
    if ((reward.text || '').length > 16000) {
      await comment('Reward terms are too long to snapshot safely. A maintainer must shorten the Reward section before claiming.');
      return;
    }
    const rewardHash = reward.sha256 || 'none';
    const rewardText = reward.text
      ? `\n\n**Reward terms recorded for this claim** (SHA-256 \`${rewardHash}\`):\n${quoteMarkdown(reward.text)}`
      : '\n\n**Reward terms recorded for this claim:** the Issue had no explicit `## Reward` section at claim time.';
    const others = state.claimants.map(c => `@${c.user}`);
    const together = others.length ? ` Also working on it: ${others.join(', ')}.` : '';

    await transition(
      `<!-- telegraph-claim user="${actor}" at="${now}" reward_sha256="${rewardHash}" -->\n` +
      `Claimed by @${actor}.${together} Post a meaningful \`/progress ...\` update within **72 hours** or your claim will be released automatically.` +
      rewardText
    );
    return;
  }

  if (command === '/progress') {
    if (!claimOf(actor)) {
      await comment('Only a current claimant can post a bounty progress command. Comment `/claim` first.');
      return;
    }
    if (!['status:claimed', 'status:review'].includes(statuses[0])) {
      await comment('Progress can only be recorded while the bounty is claimed or in review.');
      return;
    }
    if (payload.length < 15) {
      await comment('Please include a meaningful progress update after `/progress` (at least 15 characters).');
      return;
    }
    await transition(`<!-- telegraph-progress user="${actor}" at="${now}" -->\nProgress recorded for @${actor}: ${payload}`);
    return;
  }

  if (command === '/release') {
    if (!state.claimants.length) {
      await comment('There is no active claim to release.');
      return;
    }
    const maintainer = await isMaintainer();
    let target = named ? claimOf(named) : claimOf(actor);
    if (!target && !named && maintainer && state.claimants.length === 1) target = state.claimants[0];
    if (!target) {
      await comment(named ? `@${named} has no active claim on this bounty.`
        : maintainer ? 'Several people hold this bounty. Name the claim to release: `/release @user`.'
          : `Only a claimant or a maintainer can release a claim.`);
      return;
    }
    if (lower(target.user) !== lower(actor) && !maintainer) {
      await comment(`Only @${target.user} or a maintainer can release this claim.`);
      return;
    }
    const left = state.claimants.length - 1;
    await transition(`<!-- telegraph-release user="${actor}" claimant="${target.user}" at="${now}" -->\n` +
      `@${target.user}'s claim was released by @${actor}.` + (left ? ' The others keep theirs.' : ' This bounty is open again.'));
    return;
  }

  if (command === '/submit') {
    const maintainer = await isMaintainer();
    const isClaimant = !!claimOf(actor);

    if (!maintainer) {
      if (!['status:claimed', 'status:review'].includes(statuses[0]) || !isClaimant) {
        await comment(state.claimants.length
          ? 'Only someone who has claimed this bounty can submit. Comment `/claim` first.'
          : 'This bounty must be claimed before it can be submitted. Comment `/claim` first.');
        return;
      }
    } else if (!['status:claimed', 'status:open', 'status:review'].includes(statuses[0])) {
      await comment('Maintainer `/submit` override is only valid from `status:claimed`, `status:open` or `status:review`.');
      return;
    }

    if (payload.length < 15) {
      await comment('Please include repository/demo/evidence links after `/submit`.');
      return;
    }
    const override = maintainer && !isClaimant ? ' (maintainer override)' : '';
    await transition(`<!-- telegraph-submit user="${actor}" at="${now}" -->\nSubmission from @${actor}${override} moved to **review**.\n\n${payload}`);
    return;
  }

  if (command === '/open') {
    if (!(await isMaintainer())) return;
    if (state.claimant || !['status:triage', 'status:open'].includes(statuses[0])) return;
    await transition(`<!-- telegraph-open user="${actor}" at="${now}" -->\nTriage complete. This bounty is now open for contribution.`);
    return;
  }

  if (command === '/block') {
    if (!(await isMaintainer())) return;
    if (!['status:open', 'status:claimed', 'status:review'].includes(statuses[0])) return;
    await transition(`<!-- telegraph-block user="${actor}" at="${now}" -->\nMarked blocked by @${actor}.${payload ? `\n\n${payload}` : ''}`);
    return;
  }

  if (command === '/unblock') {
    if (!(await isMaintainer())) return;
    if (state.status !== 'status:blocked') return;
    await transition(`<!-- telegraph-unblock user="${actor}" at="${now}" -->\nUnblocked by @${actor}.`);
    return;
  }

  // A review names the submission it is about; with one submission waiting it is that one.
  const reviewTarget = async verb => {
    const target = named ? pendingOf(named) : state.pendingSubmitters.length === 1 ? state.pendingSubmitters[0] : null;
    if (!target) {
      await comment(named ? `@${named} has no submission waiting for review.`
        : state.pendingSubmitters.length ? `Several submissions are waiting. Name one: \`${verb} @user\`.`
          : 'A recorded submission is required before approval.');
    }
    return target;
  };

  if (command === '/changes') {
    if (!(await isMaintainer())) return;
    if (!labelNames().includes('status:review')) {
      await comment('`/changes` is only valid while the bounty is in `status:review`.');
      return;
    }
    const target = await reviewTarget('/changes');
    if (!target) return;
    if (reason.length < 10) {
      await comment('Please include a clear reason after `/changes` (at least 10 characters).');
      return;
    }
    await transition(
      `<!-- telegraph-changes user="${actor}" claimant="${target}" at="${now}" -->\n` +
      `Changes requested by @${actor}. Returned to @${target} as **claimed**; the 72-hour progress window restarts now.\n\n${reason}`
    );
    return;
  }

  if (command === '/approve') {
    if (!(await isMaintainer())) return;
    if (!labelNames().includes('status:review')) {
      await comment('`/approve` is only valid while the bounty is in `status:review`.');
      return;
    }
    const target = await reviewTarget('/approve');
    if (!target) return;
    if (lower(actor) === lower(target) || claimOf(actor) || pendingOf(actor)) {
      await comment('This submission requires an independent maintainer. Claimants and submitters are ineligible to approve it.');
      return;
    }
    const othersActive = state.claimants.some(c => lower(c.user) !== lower(target)) ||
      state.pendingSubmitters.some(u => lower(u) !== lower(target));
    await transition(`<!-- telegraph-approve user="${actor}" submitter="${target}" at="${now}" -->\n` + (othersActive
      ? `@${target}'s part is verified and accepted by @${actor}. The bounty stays open for the others. A maintainer closes it with \`/done\`.`
      : `Verified and approved by @${actor}. Bounty complete. Payment, when applicable, follows the separate funding and treasury process.`));
    return;
  }

  if (command === '/done') {
    if (!(await isMaintainer())) return;
    if (!state.accepted.length) {
      await comment('`/done` needs at least one approved submission first.');
      return;
    }
    await transition(`<!-- telegraph-done user="${actor}" at="${now}" -->\nClosed as complete by @${actor}. Accepted: ${state.accepted.map(u => '@' + u).join(', ')}. ` +
      'Payment, when applicable, follows the separate funding and treasury process.');
  }
};
