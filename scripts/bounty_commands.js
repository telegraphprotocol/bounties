strict';

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

  if (command === '/claim') {
    if (state.assignee) {
      await comment(`Issue is already claimed by @${state.assignee}.`);
      return;
    }
    if (!(await isMaintainer())) {
      const assignees = issue.assignees || [];
      if (assignees.length > 0 && !assignees.some(a => a.login.toLowerCase() === actor.toLowerCase())) {
        await comment(`Only assigned users or maintainers can claim this bounty.`);
        return;
      }
    }
    await transition({
      type: 'CLAIM',
      actor,
      timestamp: now,
      assignee: actor,
      status: 'status:in-progress'
    });
  } else if (command === '/progress') {
    if (state.assignee && state.assignee.toLowerCase() !== actor.toLowerCase() && !(await isMaintainer())) {
      await comment(`Only the assigned bounty hunter or a maintainer can update progress.`);
      return;
    }
    await transition({
      type: 'PROGRESS',
      actor,
      timestamp: now,
      note: payload,
      status: 'status:in-progress'
    });
  } else if (command === '/release') {
    if (!state.assignee || (state.assignee.toLowerCase() !== actor.toLowerCase() && !(await isMaintainer()))) {
      await comment(`Only the assigned bounty hunter or a maintainer can release this claim.`);
      return;
    }
    await transition({
      type: 'RELEASE',
      actor,
      timestamp: now,
      status: 'status:open'
    });
  } else if (command === '/submit') {
    if (!state.assignee || state.assignee.toLowerCase() !== actor.toLowerCase()) {
      await comment(`Only the assigned bounty hunter can submit work for review.`);
      return;
    }
    await transition({
      type: 'SUBMIT',
      actor,
      timestamp: now,
      note: payload,
      status: 'status:in-review'
    });
  } else if (command === '/open') {
    if (!(await isMaintainer())) {
      await comment(`Only maintainers can reopen issues.`);
      return;
    }
    await transition({
      type: 'OPEN',
      actor,
      timestamp: now,
      status: 'status:open'
    });
  } else if (command === '/block') {
    if (!(await isMaintainer())) {
      await comment(`Only maintainers can block issues.`);
      return;
    }
    await transition({
      type: 'BLOCK',
      actor,
      timestamp: now,
      note: payload,
      status: 'status:blocked'
    });
  } else if (command === '/unblock') {
    if (!(await isMaintainer())) {
      await comment(`Only maintainers can unblock issues.`);
      return;
    }
    const targetStatus = state.assignee ? 'status:in-progress' : 'status:open';
    await transition({
      type: 'UNBLOCK',
      actor,
      timestamp: now,
      status: targetStatus
    });
  } else if (command === '/changes') {
    if (!(await isMaintainer())) {
      await comment(`Only maintainers can request changes.`);
      return;
    }
    await transition({
      type: 'CHANGES',
      actor,
      timestamp: now,
      note: payload,
      status: 'status:in-progress'
    });
  } else if (command === '/approve') {
    if (!(await isMaintainer())) {
      await comment(`Only maintainers can approve work.`);
      return;
    }
    await transition({
      type: 'APPROVE',
      actor,
      timestamp: now,
      status: 'status:approved'
    });
  } else if (command === '/done') {
    if (!state.assignee || state.assignee.toLowerCase() !== actor.toLowerCase()) {
      await comment(`Only the assigned bounty hunter can mark work as done.`);
      return;
    }
    const uncompleted = uncheckedDoneBoxes(issue.body, all);
    if (uncompleted.length > 0) {
      await comment(`Cannot complete issue: there are unchecked task list items in the description or comments.`);
      return;
    }
    const reward = snapshotReward(issue.body);
    await transition({
      type: 'DONE',
      actor,
      timestamp: now,
      reward,
      status: 'status:done'
    });
  }

  await reconcileIssue({ github, owner, repo, issue_number, state: parseState(await comments()) });
};