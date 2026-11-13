#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSES = {'deterministic', 'hybrid', 'judgment'}


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


# Apply the repository's declared JSON schema first.
subprocess.run([sys.executable, str(ROOT / 'scripts/schema_check.py')], cwd=ROOT, check=True)

intents = load('catalog/intents.json')
missions = load('catalog/missions.json')
seed = load('seed/h2-bounties.json')
family_names = {x['name'] for x in intents}
assert len(family_names) == len(intents), 'Duplicate catalogue names'
mission_ids = {m['id'] for m in missions}
assert len(mission_ids) == len(missions) == 15, 'Mission catalogue must contain 15 unique missions'

mission_by_id = {m['id']: m for m in missions}
family_by_name = {x['name']: x for x in intents}
on_network = [x for x in intents if x.get('on_network')]
off_network = [x for x in intents if not x.get('on_network')]

# catalog/intents.json is written by scripts/sync_catalog.py from the node, so the checks
# here are about what the node cannot tell us: the tier, the Category and the mission map.
seen_intents = set()
for x in intents:
    assert x.get('tier') in {'mandatory', 'existing', 'network'}, f"{x['name']}: unknown tier {x.get('tier')!r}"
    if x.get('on_network'):
        assert x['class'] in CLASSES, f"{x['name']}: family class {x['class']!r} is not one the node uses"
        assert x.get('intents'), f"{x['name']}: on the network but serves no Intent"
        for i in x['intents']:
            assert i['class'] in CLASSES, f"{i['name']}: class {i['class']!r} is not one the node uses"
            assert i['name'].startswith(x['name']), f"{i['name']} is not under the family {x['name']}"
            assert i['name'] not in seen_intents, f"{i['name']} is listed under two families"
            seen_intents.add(i['name'])
    else:
        # A name the node does not serve carries no claim about how anything is scored.
        assert 'class' not in x and not x.get('intents'), f"{x['name']}: not on the network, so it must claim no class or Intents"
    for mid in x.get('used_by_missions', []):
        assert mid in mission_ids, f"Unknown mission on {x['name']}: {mid}"
        assert x['name'] in mission_by_id[mid]['core_intents'], (
            f"Reverse map mismatch: {x['name']} says it is used by {mid}, "
            "but the mission does not list it"
        )

for m in missions:
    missing = [x for x in m['core_intents'] if x not in family_names]
    assert not missing, f"{m['id']} references names that are not in the catalogue: {missing}"
    for name in m['core_intents']:
        assert m['id'] in family_by_name[name].get('used_by_missions', []), (
            f"Reverse map mismatch: {m['id']} lists {name}, "
            "but the catalogue entry does not list the mission"
        )

for item in seed:
    assert item['work_type'] in {'miner', 'evaluator', 'app', 'protocol', 'tooling', 'security'}
    assert item['priority'] in {'p0', 'p1', 'p2'}
    if item.get('intent'):
        assert item['intent'] in family_names, f"Unknown Intent in seed: {item['intent']}"
    for mid in item.get('missions', []):
        assert mid in mission_ids, f"Unknown mission in seed: {mid}"
    assert item.get('acceptance'), f"Missing acceptance criteria: {item.get('title')}"
    reward = item.get('reward') or {}
    assert 'funded' in reward, f"Missing reward.funded: {item.get('title')}"
    assert reward.get('max_awards', 1) == 1, (
        f"One claim/award per Issue is enforced; use separate slot Issues for multiple implementations: {item['title']}"
    )
    if reward['funded']:
        for field in ['amount', 'denomination', 'payout_asset', 'eligibility', 'verification_condition', 'payout_window']:
            assert reward.get(field) not in (None, ''), f"Funded bounty missing reward.{field}: {item['title']}"
        if str(reward['denomination']).upper() != str(reward['payout_asset']).upper():
            assert reward.get('conversion_rule') not in (None, ''), (
                f"Cross-denomination funded bounty missing reward.conversion_rule: {item['title']}"
            )

# The Season II lists are decided by the protocol team, not by a sync, so losing one is a bug.
mandatory = sum(1 for x in intents if x['tier'] == 'mandatory')
existing = sum(1 for x in intents if x['tier'] == 'existing')
assert (mandatory, existing) == (63, 40), f'Expected 63 mandatory + 40 existing Season II Intents, found {mandatory} + {existing}'

print(f'OK: {len(seen_intents)} Intents in {len(on_network)} families on the network '
      f'({mandatory} mandatory + {existing} existing Season II, {len(off_network)} names the network does not serve), '
      f'{len(missions)} missions, {len(seed)} seed candidates')
