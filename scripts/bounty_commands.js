'use strict';

const {
  parseState,
  snapshotReward,
  uncheckedDoneBoxes,
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
  if (labelNames().includes('opportunity:provider')) return;

  const currentStatus = statuses[0];

  if (command === '/claim') {
    if (currentStatus !== 'status:open') {
      await comment(`Cannot claim issue in status ${currentStatus}.`);
      return;
    }
    if (payload) {
      await comment('The /claim command does not accept arguments.');
      return;
    }
    await transition(`- **Claimed**: @${actor} at ${now}\n  - source: ${source}`);
    await reconcileIssue({ github, owner, repo, issue_number });
    return;
  }

  if (command === '/progress') {
    if (currentStatus !== 'status:claimed' && currentStatus !== 'status:blocked') {
      await comment(`Cannot move to progress from status ${currentStatus}.`);
      return;
    }
    if (state.assignee && state.assignee.toLowerCase() !== actor.toLowerCase() && !(await isMaintainer())) {
      await comment(`Only the assigned user (@${state.assignee}) or maintainers can update progress.`);
      return;
    }
    await transition(`- **Progress**: @${actor} updated progress at ${now}\n  - note: ${payload || 'in progress'}\n  - source: ${source}`);
    await reconcileIssue({ github, owner, repo, issue_number });
    return;
  }

  if (command === '/release') {
    if (currentStatus !== 'status:claimed' && currentStatus !== 'status:blocked') {
      await comment(`Cannot release issue in status ${currentStatus}.`);
      return;
    }
    if (state.assignee && state.assignee.toLowerCase() !== actor.toLowerCase() && !(await isMaintainer())) {
      await comment(`Only the assigned user (@${state.assignee}) or maintainers can release the claim.`);
      return;
    }
    await transition(`- **Released**: @${actor} released claim at ${now}\n  - source: ${source}`);
    await reconcileIssue({ github, owner, repo, issue_number });
    return;
  }

  if (command === '/submit') {
    if (currentStatus !== 'status:claimed' && currentStatus !== 'status:changes-requested') {
      await comment(`Cannot submit work from status ${currentStatus}.`);
      return;
    }
    if (state.assignee && state.assignee.toLowerCase() !== actor.toLowerCase() && !(await isMaintainer())) {
      await comment(`Only the assigned user (@${state.assignee}) or maintainers can submit work.`);
      return;
    }
    if (!payload) {
      await comment('Please provide submission details or a pull request reference with /submit.');
      return;
    }
    await transition(`- **Submitted**: @${actor} submitted work at ${now}\n  - details: ${quoteMarkdown(payload)}\n  - source: ${source}`);
    await reconcileIssue({ github, owner, repo, issue_number });
    return;
  }

  if (command === '/open') {
    if (!await isMaintainer()) {
      await comment('Only maintainers can reopen issues.');
      return;
    }
    await transition(`- **Reopened**: @${actor} reopened issue at ${now}\n  - source: ${source}`);
    await reconcileIssue({ github, owner, repo, issue_number });
    return;
  }

  if (command === '/block') {
    if (!await isMaintainer()) {
      await comment('Only maintainers can block issues.');
      return;
    }
    if (currentStatus === 'status:done') {
      await comment('Cannot block a completed issue.');
      return;
    }
    await transition(`- **Blocked**: @${actor} blocked issue at ${now}\n  - reason: ${quoteMarkdown(payload || 'no reason provided')}\n  - source: ${source}`);
    await reconcileIssue({ github, owner, repo, issue_number });
    return;
  }

  if (command === '/unblock') {
    if (!await isMaintainer()) {
      await comment('Only maintainers can unblock issues.');
      return;
    }
    if (currentStatus !== 'status:blocked') {
      await comment('Issue is not blocked.');
      return;
    }
    await transition(`- **Unblocked**: @${actor} unblocked issue at ${now}\n  - source: ${source}`);
    await reconcileIssue({ github, owner, repo, issue_number });
    return;
  }

  if (command === '/changes') {
    if (!await isMaintainer()) {
      await comment('Only maintainers can request changes.');
      return;
    }
    if (currentStatus !== 'status:submitted') {
      await comment('Can only request changes on submitted work.');
      return;
    }
    if (!payload) {
      await comment('Please provide feedback explaining the requested changes.');
      return;
    }
    await transition(`- **Changes Requested**: @${actor} requested changes at ${now}\n  - feedback: ${quoteMarkdown(payload)}\n  - source: ${source}`);
    await reconcileIssue({ github, owner, repo, issue_number });
    return;
  }

  if (command === '/approve') {
    if (!await isMaintainer()) {
      await comment('Only maintainers can approve work.');
      return;
    }
    if (currentStatus !== 'status:submitted') {
      await comment('Can only approve submitted work.');
      return;
    }
    await transition(`- **Approved**: @${actor} approved work at ${now}\n  - source: ${source}`);
    await reconcileIssue({ github, owner, repo, issue_number });
    return;
  }

  if (command === '/done') {
    if (!await isMaintainer()) {
      await comment('Only maintainers can complete issues.');
      return;
    }
    if (currentStatus !== 'status:approved') {
      await comment('Can only complete approved work.');
      return;
    }
    const unchecked = uncheckedDoneBoxes(issue.body || '');
    if (unchecked > 0) {
      await comment(`Cannot complete issue: there are ${unchecked} unchecked task list items in the issue description.`);
      return;
    }
    const rewardSnapshot = snapshotReward(issue.body || '');
    await transition(`- **Done**: @${actor} completed issue at ${now}\n  - reward: ${rewardSnapshot}\n  - source: ${source}`);
    await reconcileIssue({ github, owner, repo, issue_number });
    return;
  }
};