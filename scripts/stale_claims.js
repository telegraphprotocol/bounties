'use strict';

const {
  parseState,
  isStaleWarningFor,
} = require('./bounty_state');
const { createHash } = require('crypto');
const { reconcileIssue, recordTransition } = require('./bounty_journal');

module.exports = async function runStaleClaims({ github, context }) {
  const owner = context.repo.owner;
  const repo = context.repo.repo;
  const issues = await github.paginate(github.rest.issues.listForRepo, {
    owner, repo, state: 'open', per_page: 100,
  });

  for (const issue of issues) {
    if (issue.pull_request) continue;
    let comments = await github.paginate(github.rest.issues.listComments, {
      owner, repo, issue_number: issue.number, per_page: 100,
    });
    let state = parseState(comments);
    const latest = await reconcileIssue({ github, owner, repo, issue_number: issue.number, state });
    if (latest.state !== 'open' || !['status:claimed', 'status:review'].includes(state.status)) continue;

    // Each claimant has their own progress window. Someone whose submission waits for
    // review is not idle.
    for (const claim of state.claimants) {
      const who = claim.user.toLowerCase();
      if (state.pendingSubmitters.some(u => u.toLowerCase() === who) || !claim.lastProgressAt) continue;
      let ageHours = (Date.now() - new Date(claim.lastProgressAt).getTime()) / 36e5;
      const alreadyWarned = comments.some(c => isStaleWarningFor(c, claim.user, claim.claimedAt));

      if (ageHours >= 72) {
        // Re-read immediately before mutation so a just-posted /progress or manual release is observed.
        comments = await github.paginate(github.rest.issues.listComments, {
          owner, repo, issue_number: issue.number, per_page: 100,
        });
        state = parseState(comments);
        const current = state.claimants.find(c => c.user.toLowerCase() === who);
        if (!current || !current.lastProgressAt || !['status:claimed', 'status:review'].includes(state.status)) continue;
        if (state.pendingSubmitters.some(u => u.toLowerCase() === who)) continue;
        ageHours = (Date.now() - new Date(current.lastProgressAt).getTime()) / 36e5;
        if (ageHours < 72) continue;

        const latestIssue = (await github.rest.issues.get({ owner, repo, issue_number: issue.number })).data;
        const labels = latestIssue.labels.map(l => typeof l === 'string' ? l : l.name);
        if (latestIssue.state !== 'open' || !labels.some(l => ['status:claimed', 'status:review'].includes(l))) continue;
        // A valid progress command can already be on GitHub while its job waits
        // behind this scheduled job. Let that command run before expiring it.
        const pendingProgress = comments.some(c => {
          const text = String(c.body || '').trim();
          return c.user?.type === 'User' && c.user.login.toLowerCase() === who &&
            /^\/progress\s+\S[\s\S]*$/.test(text) && text.replace(/^\/progress\s+/, '').trim().length >= 15 &&
            text.length <= 8192 && Date.parse(c.created_at) > Date.parse(current.lastProgressAt) &&
            Date.now() - Date.parse(c.created_at) < 72 * 36e5;
        });
        if (pendingProgress) continue;
        const version = createHash('sha256').update(`${current.user}:${current.claimedAt}:${current.lastProgressAt}`).digest('hex').slice(0, 24);
        const now = new Date().toISOString();
        const left = state.claimants.length - 1;
        state = await recordTransition({
          owner, repo, issue_number: issue.number,
          github, source: `stale-release:${version}`,
          body: `<!-- telegraph-release user="telegraph-bot" claimant="${current.user}" at="${now}" -->\n@${current.user}'s claim was automatically released after **72 hours without a \`/progress\` update**.` +
            (left ? ' The others keep theirs.' : ' This bounty is open again.'),
        });
        comments = await github.paginate(github.rest.issues.listComments, {
          owner, repo, issue_number: issue.number, per_page: 100,
        });
      } else if (ageHours >= 48 && !alreadyWarned) {
        const version = createHash('sha256').update(`${claim.user}:${claim.claimedAt}`).digest('hex').slice(0, 24);
        await recordTransition({
          owner, repo, issue_number: issue.number,
          github, source: `stale-warning:${version}`,
          body: `<!-- telegraph-stale-warning claimant="${claim.user}" claimed_at="${claim.claimedAt}" -->\n@${claim.user}: this claim has had no \`/progress\` update for 48 hours. Post an update before 72 hours to keep the claim.`,
        });
      }
    }
  }
};
