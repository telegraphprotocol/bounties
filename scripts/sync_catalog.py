#!/usr/bin/env python3
"""Rewrite catalog/intents.json from the Telegraph node.

The node is the source of truth for what an Intent is: its name, its evaluator class
(deterministic, hybrid or judgment), what it takes and what it answers. Nobody edits those
fields by hand, because a hand-kept copy drifts and contributors then build the wrong thing.

What this keeps from the existing file is only what the node does not know: the Season II
tier, the Category, the priority score and the mission map.

    python3 scripts/sync_catalog.py            # rewrite the file
    python3 scripts/sync_catalog.py --check    # fail if the file no longer matches the node

A catalogue name the node does not serve is kept, marked "on_network": false, and reported:
missions reference some of them, so they are never silently dropped. Renaming or removing
one is a protocol-team decision, not this script's.
"""
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'catalog/intents.json'
DEFAULT_NODE = 'https://devnode.telegraphprotocol.com'

# Kept from the existing entry: the node knows none of it.
KEPT = ('tier', 'category', 'priority_score', 'description', 'target_latency', 'used_by_missions')
TIER_ORDER = {'mandatory': 0, 'existing': 1, 'network': 2}


def get(url):
    # The node's CDN answers Python's default User-Agent with 403.
    req = urllib.request.Request(url, headers={'User-Agent': 'telegraph-bounties-sync'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def intent_detail(node, name):
    """The node's own record of one name, or None when it does not know it."""
    try:
        return get(f'{node}/engine/v1/intents/{name}')
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def fields(schema, key):
    return [f['name'] for f in (schema or {}).get(key) or []]


def build(node, existing):
    kept = {x['name']: {k: x[k] for k in KEPT if k in x} for x in existing}
    listing = get(f'{node}/engine/v1/intents')
    families = {}
    for item in sorted(listing['intents'], key=lambda i: i['intent_id']):
        name = item['intent_id']
        if item.get('canonical') is False:
            # A miner-declared name that is not a canonical Intent on chain.
            print(f'{name}: not a canonical Intent on chain, skipped')
            continue
        # The node names the family an adapter registers on, and the kind it is tested as.
        family = item.get('family')
        family_class = (item.get('adapter_registration') or {}).get('tested_as')
        if not family or not family_class:
            raise SystemExit(f'{name}: the node gives it no family; tell the protocol team')
        detail = intent_detail(node, name) or {}
        entry = {
            'name': name,
            'class': detail.get('class') or '',
            'description': item.get('description') or '',
            'params': fields(detail.get('request'), 'params'),
            'answer': fields(detail.get('response'), 'fields'),
            'onchain_ready': bool((detail.get('onchain') or {}).get('ready')),
        }
        if not entry['onchain_ready'] and (detail.get('onchain') or {}).get('reason'):
            entry['onchain_note'] = detail['onchain']['reason']
        fam = families.setdefault(family, {'name': family, 'class': family_class, 'on_network': True, 'intents': []})
        fam['intents'].append(entry)

    out = []
    for name, fam in families.items():
        entry = {'name': name, 'class': fam['class'], 'on_network': True}
        entry.update(kept.get(name, {'tier': 'network'}))
        entry['intents'] = fam['intents']
        out.append(entry)
    # A catalogue name the node does not serve keeps what we know about it and nothing more.
    for name, meta in kept.items():
        if name not in families:
            entry = {'name': name, 'on_network': False}
            entry.update(meta)
            out.append(entry)
    out.sort(key=lambda x: (TIER_ORDER.get(x.get('tier'), 9), x['name']))
    return out


def main(argv):
    node = DEFAULT_NODE
    for i, arg in enumerate(argv):
        if arg == '--node' and i + 1 < len(argv):
            node = argv[i + 1].rstrip('/')
    existing = json.loads(CATALOG.read_text(encoding='utf-8')) if CATALOG.exists() else []
    built = build(node, existing)
    text = json.dumps(built, indent=2, ensure_ascii=False) + '\n'

    on_network = [x for x in built if x.get('on_network')]
    missing = [x['name'] for x in built if not x.get('on_network')]
    counted = sum(len(x['intents']) for x in on_network)
    if '--check' in argv:
        if CATALOG.read_text(encoding='utf-8') != text:
            print('OUT OF DATE: catalog/intents.json no longer matches the node.')
            print('Run: python3 scripts/sync_catalog.py')
            return 1
        print(f'OK: {len(on_network)} families, {counted} Intents, matching the node')
        return 0
    CATALOG.write_text(text, encoding='utf-8', newline='\n')
    print(f'wrote catalog/intents.json: {len(on_network)} families, {counted} Intents')
    if missing:
        print(f'{len(missing)} catalogue names the node does not serve, kept and marked on_network false:')
        for name in missing:
            print(f'  {name}')
        print('Rename them to the network\'s own names, or drop them: a protocol-team decision.')
    print('Now run: python3 scripts/generate_docs.py')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
