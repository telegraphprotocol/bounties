'use strict';

const crypto = require('crypto');

const TRUSTED_BOT_LOGIN = 'github-actions[bot]';
const ISO_UTC = '\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3}Z';
const GH_USER = '[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})(?:\\[bot\\])?';

const patterns = {
  reject: /^<!-- telegraph-reject source="(comment:\d+)" -->$/,
  claim: new RegExp(`^<!-- telegraph-claim user="(${GH_USER})" at="(${ISO_UTC})" reward_sha256="([a-f0-9]{64}|none)" -->$`),
  progress: new RegExp(`^<!-- telegraph-progress user="(${GH_USER})" at="(${ISO_UTC})" -->$`),
  // claimant names whose claim is released; without it (older records) every claim is.
  release: new RegExp(`^<!-- telegraph-release user="(${GH_USER})"(?: claimant="(${GH_USER})")? at="(${ISO_UTC})" -->$`),
  submit: new RegExp(`^<!-- telegraph-submit user="(${GH_USER})" at="(${ISO_UTC})" -->$`),
  changes: new RegExp(`^<!-- telegraph-changes user="(${GH_USER})" claimant="(${GH_USER})" at="(${ISO_UTC})" -->$`),
  open: new RegExp(`^<!-- telegraph-open user="(${GH_USER})" at="(${ISO_UTC})" -->$`),
  block: new RegExp(`^<!-- telegraph-block user="(${GH_USER})" at="(${ISO_UTC})" -->$`),
  unblock: new RegExp(`^<!-- telegraph-unblock user="(${GH_USER})" at="(${ISO_UTC})" -->$`),
  // submitter names the one submission accepted; without it (older records) the bounty is done.
  approve: new RegExp(`^<!-- telegraph-approve user="(${GH_USER})"(?: submitter="(${GH_USER})")? at="(${ISO_UTC})" -->$`),
  done: new RegExp(`^<!-- telegraph-done user="(${GH_USER})" at="(${ISO_UTC})" -->$`),
  staleWarning: new RegExp(`^<!-- telegraph-stale-warning claimant="(${GH_USER})" claimed_at="(${ISO_UTC})" -->$`),
};

function loginOf(comment) {
  return String(comment?.user?.login || '').toLowerCase();
}

function firstLine(body) {
  return String(body || '').split(/\r?\n/, 1)[0].trim();
}

function parseTrustedControl(comment) {
  if (loginOf(comment) !== TRUSTED_BOT_LOGIN) return null;
  const line = firstLine(comment?.body);
  let m;

  if ((m = line.match(patterns.reject))) return { type: 'reject', source: m[1] };

  if ((m = line.match(patterns.claim))) {
    return { type: 'claim', user: m[1], at: m[2], rewardSha256: m[3] };
  }
  if ((m = line.match(patterns.progress))) {
    return { type: 'progress', user: m[1], at: m[2] };
  }
  if ((m = line.match(patterns.release))) {
    return { type: 'release', user: m[1], claimant: m[2] || null, at: m[3] };
  }
  if ((m = line.match(patterns.submit))) {
    return { type: 'submit', user: m[1], at: m[2] };
  }
  if ((m = line.match(patterns.changes))) {
    return { type: 'changes', user: m[1], claimant: m[2], at: m[3] };
  }
  if ((m = line.match(patterns.open))) {
    return { type: 'open', user: m[1], at: m[2] };
  }
  if ((m = line.match(patterns.block))) {
    return { type: 'block', user: m[1], at: m[2] };
  }
  if ((m = line.match(patterns.unblock))) {
    return { type: 'unblock', user: m[1], at: m[2] };
  }
  if ((m = line.match(patterns.approve))) {
    return { type: 'approve', user: m[1], submitter: m[2] || null, at: m[3] };
  }
  if ((m = line.match(patterns.done))) {
    return { type: 'done', user: m[1], at: m[2] };
  }
  if ((m = line.match(patterns.staleWarning))) {
    return { type: 'stale-warning', claimant: m[1], claimedAt: m[2] };
  }
  return null;
}

function orderedComments(comments) {
  return [...comments].sort((a, b) => {
    const ta = Date.parse(a?.created_at || '') || 0;
    const tb = Date.parse(b?.created_at || '') || 0;
    if (ta !== tb) return ta - tb;
    return Number(a?.id || 0) - Number(b?.id || 0);
  });
}

// parseState replays the trusted bot records. Several people can hold a claim on the same
// bounty at once; each has their own claim time, progress window and reward snapshot, and
// each submits and is approved on their own. `claimant` and its fields are the earliest
// active claim, for callers that show one name.
function parseState(comments) {
  const claims = new Map(); // lower-case login -> { user, claimedAt, lastProgressAt, rewardSha256 }
  const pending = new Map(); // lower-case login -> login, submissions waiting for review
  const accepted = new Set();
  const participants = new Set(); // lower-case logins; retained after release or acceptance
  let lastSubmitter = null;
  let status = null;
  let blockedStatus = null;
  const processedSources = new Set();
  const key = user => String(user).toLowerCase();
  const settle = () => pending.size ? 'status:review' : claims.size ? 'status:claimed' : 'status:open';

  for (const comment of orderedComments(comments)) {
    const ctl = parseTrustedControl(comment);
    if (!ctl) continue;
    const source = ctl.source || String(comment.body || '').split(/\r?\n/)[1]?.match(/^<!-- telegraph-event source="([a-z0-9:-]+)" -->$/)?.[1];
    if (source && processedSources.has(source)) continue;
    if (source) processedSources.add(source);
    if (status === 'status:done') continue;

    if (ctl.type === 'claim') {
      if (claims.has(key(ctl.user))) continue;
      participants.add(key(ctl.user));
      claims.set(key(ctl.user), {
        user: ctl.user, claimedAt: ctl.at, lastProgressAt: ctl.at,
        rewardSha256: ctl.rewardSha256 === 'none' ? null : ctl.rewardSha256,
      });
      if (status !== 'status:review' && status !== 'status:blocked') status = 'status:claimed';
    } else if (ctl.type === 'progress') {
      const c = claims.get(key(ctl.user));
      if (c) c.lastProgressAt = ctl.at;
    } else if (ctl.type === 'changes') {
      // A changes request starts a fresh work window for that claimant.
      const k = key(ctl.claimant);
      if (!pending.has(k) && !claims.has(k)) continue;
      pending.delete(k);
      const c = claims.get(k);
      if (c) c.lastProgressAt = ctl.at;
      lastSubmitter = [...pending.values()].at(-1) || null;
      status = settle();
    } else if (ctl.type === 'release') {
      if (ctl.claimant) {
        claims.delete(key(ctl.claimant));
        pending.delete(key(ctl.claimant));
      } else {
        claims.clear();
        pending.clear();
      }
      lastSubmitter = [...pending.values()].at(-1) || null;
      status = settle();
    } else if (ctl.type === 'submit') {
      participants.add(key(ctl.user));
      pending.set(key(ctl.user), ctl.user);
      lastSubmitter = ctl.user;
      status = 'status:review';
    } else if (ctl.type === 'open') {
      if (!claims.size) status = 'status:open';
    } else if (ctl.type === 'block') {
      if (status !== 'status:blocked') {
        blockedStatus = status || (claims.size ? 'status:claimed' : 'status:open');
        status = 'status:blocked';
      }
    } else if (ctl.type === 'unblock') {
      if (status === 'status:blocked') status = blockedStatus;
    } else if (ctl.type === 'approve') {
      if (!ctl.submitter) {
        status = 'status:done';
        continue;
      }
      const k = key(ctl.submitter);
      if (!pending.has(k)) continue;
      pending.delete(k);
      claims.delete(k);
      accepted.add(ctl.submitter);
      lastSubmitter = [...pending.values()].at(-1) || null;
      status = !claims.size && !pending.size ? 'status:done' : settle();
    } else if (ctl.type === 'done') {
      if (accepted.size) status = 'status:done';
    }
  }

  const first = claims.values().next().value || null;
  return {
    claimant: first ? first.user : null,
    claimedAt: first ? first.claimedAt : null,
    lastProgressAt: first ? first.lastProgressAt : null,
    rewardSha256: first ? first.rewardSha256 : null,
    claimants: [...claims.values()],
    pendingSubmitters: [...pending.values()],
    accepted: [...accepted],
    participants: [...participants],
    lastSubmitter, status, blockedStatus, processedSources,
  };
}

function isStaleWarningFor(comment, claimant, claimedAt) {
  const ctl = parseTrustedControl(comment);
  return !!ctl && ctl.type === 'stale-warning' &&
    ctl.claimant.toLowerCase() === String(claimant).toLowerCase() &&
    ctl.claimedAt === claimedAt;
}

function extractRewardSection(issueBody) {
  const body = String(issueBody || '').replace(/\r\n/g, '\n');
  const match = body.match(/^## Reward\s*\n([\s\S]*?)(?=^##\s|(?![\s\S]))/m);
  if (!match) return null;
  return match[1].trim().replace(/[ \t]+$/gm, '');
}

function snapshotReward(issueBody) {
  const section = extractRewardSection(issueBody);
  if (!section) return { text: null, sha256: null };
  const text = section.trim();
  return {
    text,
    sha256: crypto.createHash('sha256').update(text, 'utf8').digest('hex'),
  };
}

function quoteMarkdown(text) {
  return String(text || '').split('\n').map(line => `> ${line}`).join('\n');
}

function permissionAllowsMaintenance(permission) {
  return ['write', 'maintain', 'admin'].includes(String(permission || '').toLowerCase());
}

module.exports = {
  TRUSTED_BOT_LOGIN,
  parseTrustedControl,
  parseState,
  isStaleWarningFor,
  extractRewardSection,
  snapshotReward,
  quoteMarkdown,
  permissionAllowsMaintenance,
  _patterns: patterns,
};
