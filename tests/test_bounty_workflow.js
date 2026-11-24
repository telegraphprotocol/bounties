'use strict';

const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const runCommand = require('../scripts/bounty_commands');
const { parseState, snapshotReward, TRUSTED_BOT_LOGIN } = require('../scripts/bounty_state');

function makeHarness({ labels = ['status:open'], body = '## Reward\nNo monetary/token reward is currently committed.\n', permissions = {} } = {}) {
  const state = {
    issue: { number: 42, labels: [...labels], body, state: 'open' },
    comments: [],
    permissions: { ...permissions },
    nextId: 1,
  };

  function addComment(user, body, created_at = new Date().toISOString()) {
    const c = { id: state.nextId++, user: { login: user, type: user.endsWith('[bot]') ? 'Bot' : 'User' }, body, created_at };
    state.comments.push(c);
    return c;
  }

  const github = {
    rest: {
      issues: {
        get: async () => ({ data: { ...state.issue, labels: state.issue.labels.map(name => ({ name })) } }),
        setLabels: async ({ labels: next }) => { state.issue.labels = [...next]; return { data: {} }; },
        createComment: async ({ body: text }) => ({ data: addComment(TRUSTED_BOT_LOGIN, text) }),
        listComments: async () => ({ data: [...state.comments] }),
        getComment: async ({ comment_id }) => ({ data: state.comments.find(c => c.id === comment_id) }),
        update: async ({ state: nextState, state_reason }) => {
          state.issue.state = nextState;
          state.issue.state_reason = state_reason;
          return { data: state.issue };
        },
      },
      repos: {
        getCollaboratorPermissionLevel: async ({ username }) => ({ data: { permission: state.permissions[username] || 'read' } }),
      },
    },
    paginate: async (fn, args) => {
      const resp = await fn(args);
      return resp.data;
    },
  };

  async function command(actor, text, commentId) {
    const event = commentId ? state.comments.find(c => c.id === commentId) : addComment(actor, text);
    const context = {
      repo: { owner: 'telegraph', repo: 'bounties' },
      issue: { number: 42 },
      actor,
      payload: { comment: event },
    };
    await runCommand({ github, context });
    return event.id;
  }

  return { state, github, command, addComment };
}

async function runTests() {
  console.log('Running bounty workflow tests...');

  // Test 1: Basic command parsing and claim validation
  {
    const h = makeHarness();
    const commentId = await h.command('alice', '/claim');
    const comments = await h.github.rest.issues.listComments();
    assert.strictEqual(comments.length, 2); // 1 user command + 1 bot reply
    assert(comments[1].body.includes('<!-- telegraph-reject'));
  }

  // Test 2: Mission 01 Exchange / Season II validations if applicable
  {
    const h = makeHarness({ labels: ['status:open'] });
    await h.command('alice', '/claim');
    const parsed = parseState(await h.github.rest.issues.listComments());
    assert.strictEqual(parsed.processedSources.size, 1);
  }

  console.log('All bounty workflow tests passed successfully.');
}

if (require.main === module) {
  runTests().catch(err => {
    console.error(err);
    process.exit(1);
  });
}

module.exports = { makeHarness, runTests };