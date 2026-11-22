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

  // Test 1: Basic command execution and state transition
  {
    const h = makeHarness();
    await h.command('alice', '/claim');
    const state = parseState(h.state.comments);
    assert.strictEqual(state.assignee, 'alice');
    assert.deepStrictEqual(h.state.issue.labels, ['status:assigned']);
    console.log('  ✓ /claim assigns issue and updates status label');
  }

  // Test 2: Issue #202 fix verification - Web3 Native & DeFi / Season II mission or related workflow edge cases
  {
    const h = makeHarness({
      labels: ['status:assigned'],
      body: '## Reward\n100 USDC\n## Mission\nMission 14 — Web3 Native & DeFi — Season II\n'
    });
    // Alice submits progress or work on the DeFi mission
    await h.command('alice', '/submit');
    const state = parseState(h.state.comments);
    assert.deepStrictEqual(h.state.issue.labels, ['status:review']);
    console.log('  ✓ /submit moves assigned issue to review status correctly for Season II mission');
  }

  // Test 3: Unauthorized user command handling
  {
    const h = makeHarness({ labels: ['status:open'] });
    // Attempting to approve without maintenance permission should be rejected/ignored
    await h.command('bob', '/approve');
    assert.deepStrictEqual(h.state.issue.labels, ['status:open']);
    console.log('  ✓ Unauthorized /approve command does not alter status');
  }

  console.log('All bounty workflow tests passed successfully.');
}

if (require.main === module) {
  runTests().catch(err => {
    console.error('Test failure:', err);
    process.exit(1);
  });
}

module.exports = { makeHarness, runTests };