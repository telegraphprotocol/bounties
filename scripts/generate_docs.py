#!/usr/bin/env python3
import json, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
INTENTS = json.loads((ROOT/'catalog/intents.json').read_text(encoding='utf-8'))
MISSIONS = json.loads((ROOT/'catalog/missions.json').read_text(encoding='utf-8'))
mission_name = {m['id']: m['name'] for m in MISSIONS}

EVAL = 'https://anjoman.ai/dashboard/eval'
DOCS = 'https://anjoman.ai/docs/scoring'
ON_NETWORK = [x for x in INTENTS if x.get('on_network')]
OFF_NETWORK = [x for x in INTENTS if not x.get('on_network')]

# What the network needs for an Intent, decided by the kind the node scores it as.
MATERIAL = {
    'deterministic': 'truth sources',
    'hybrid': 'truth sources and question pairs',
    'judgment': 'question pairs',
}


def eval_link(name):
    return f'{EVAL}?intent={name}'


def bounty_link(name):
    return f'../../issues?q=is%3Aissue+is%3Aopen+{name}'


def contribute(intent, family):
    """What a contributor can add for one Intent. A scoring module is registered on the
    family, and a family's module scores only the Intents of the family's own kind, so an
    Intent of another kind has no module anyone can build for it."""
    material = MATERIAL.get(intent['class'], 'evaluation material')
    if intent['class'] != family['class']:
        return f'{material} · no module (see above)'
    if family['class'] == 'deterministic':
        return f'{material} · comparator already live'
    return f"{material} · adapter on `{family['name']}`"


def render_intents():
    out = [
        '# Intent Catalogue', '',
        f'**{sum(len(x["intents"]) for x in ON_NETWORK)} Intents in {len(ON_NETWORK)} families on the Telegraph network.**', '',
        'Read straight from the node, so every kind below is the kind the network really scores that',
        'Intent as. Regenerate with `python3 scripts/sync_catalog.py` and this script.', '',
        '## What the network needs, by kind', '',
        '| Kind | Evaluation material it is scored on |', '|---|---|',
        '| **deterministic** | **Truth sources**: free public APIs (no key) that answer the Intent\'s question. The network asks a few each epoch and checks miners against the middle answer. |',
        '| **hybrid** | **Truth sources** for the checkable part and **question pairs** for the rest. |',
        '| **judgment** | **Question pairs**: a real question with a better and a worse answer. |', '',
        'Anyone can add material. It goes to the network through Anjoman:',
        f'[Evaluate]({EVAL}). Every Intent name below opens that page with the Intent already chosen.',
        f'The format, the limits and the reasons a row is turned down: [Contribute Evaluation Data]({DOCS}/contribute-evaluation-data).', '',
        '## Scoring modules: which families take one', '',
        'A scoring module is registered on a **family**, never on a single Intent, and the',
        "family's own kind decides which kind it takes. A family's module also scores only the",
        "Intents of the family's own kind. So:", '',
        '- A **judgment** or **hybrid** family takes an **evaluator adapter**. A better adapter can replace the one in place, so this is open work.',
        '- A **deterministic** family takes a **comparator module**. A comparator has no model: it only has to compute the network\'s fixed comparison rule, so there is no better one to build.',
        '- A **deterministic Intent under a judgment family** is scored by the network\'s own shared comparator. **Nothing registered on that family can score it**, so there is no module to build for it: one sent there waits as `pending` with `awaiting_compatible_material` and never goes live. The Contribute column says so per Intent.', '',
        f'How to build and register one: [Build an Evaluator Adapter]({DOCS}/build-a-scoring-module).', '',
        '## No open Issue for your Intent?', '',
        'You can still contribute. The network takes material for every Intent listed here,',
        'whether or not a bounty exists for it. GitHub is where bounty work is claimed, proven',
        'and approved; Anjoman is where the network receives the work and decides whether it',
        'uses it. The Bounty column finds any open Issue that names the Intent.', '',
    ]
    by_cat = defaultdict(list)
    for x in ON_NETWORK:
        by_cat[x.get('category') or 'Not yet categorised'].append(x)
    for cat in sorted(by_cat, key=lambda c: (c == 'Not yet categorised', c)):
        fams = sorted(by_cat[cat], key=lambda i: (-int(i.get('priority_score') or 0), i['name']))
        out += [f'## {cat}', '', '| Intent | Kind | Family | Contribute | Bounty |', '|---|---|---|---|---|']
        for fam in fams:
            for intent in fam['intents']:
                out.append(
                    f"| [`{intent['name']}`]({eval_link(intent['name'])}) | {intent['class']} "
                    f"| `{fam['name']}` ({fam['class']}) | {contribute(intent, fam)} "
                    f"| [open]({bounty_link(intent['name'])}) |")
        out += ['', '### Details', '']
        for fam in fams:
            used = ', '.join(mission_name[m] for m in fam.get('used_by_missions', [])) or '—'
            head = f"**`{fam['name']}`** — {fam['class']} family · tier {fam.get('tier', 'network')} · H2 missions: {used}"
            out += [head, '']
            if fam.get('description'):
                out += [fam['description'], '']
            for intent in fam['intents']:
                bits = [intent['class']]
                if intent.get('params'):
                    bits.append('asks ' + ', '.join(f'`{p}`' for p in intent['params']))
                if intent.get('answer'):
                    bits.append('answers ' + ', '.join(f'`{a}`' for a in intent['answer']))
                out += [f"#### `{intent['name']}`", '', ' · '.join(bits), '']
                if intent.get('description'):
                    out += [intent['description'], '']
                out += [f"Contribute {contribute(intent, fam)}. [Add it on Anjoman]({eval_link(intent['name'])}) · [open bounties]({bounty_link(intent['name'])})", '']
                if intent.get('onchain_note'):
                    out += [f"Not usable in an on-chain job yet: {intent['onchain_note']}.", '']
    if OFF_NETWORK:
        out += ['## Names the network does not serve', '',
                'These are in this catalogue and in the mission map, but the node serves no Intent',
                'under them. Some are a different spelling of a name the network does use. Renaming',
                'or dropping one is a protocol-team decision, so they are listed, not guessed at.', '',
                '| Name | Tier | H2 missions |', '|---|---|---|']
        for x in sorted(OFF_NETWORK, key=lambda i: i['name']):
            used = ', '.join(mission_name[m] for m in x.get('used_by_missions', [])) or '—'
            out.append(f"| `{x['name']}` | {x.get('tier', '—')} | {used} |")
        out += ['']
    return '\n'.join(out).rstrip()+'\n'


def render_missions():
    out = ['# Season II Mission → Intent Map', '', '**15 commercial missions define the end states. Reusable Intents provide the intelligence underneath them.**', '',
           'Apps build for missions. Miners and Evaluators build for Intents. The same Intent can power many missions.', '']
    off = {x['name'] for x in OFF_NETWORK}
    for i,m in enumerate(MISSIONS,1):
        out += [f"## {i:02d}. {m['name']}", '', 'Core starting Intents:', '']
        out += [f"- `{x}`" + (' — the network serves no Intent under this name yet' if x in off else '') for x in m['core_intents']]
        out += ['', '> This map is a coordination baseline, not a hard whitelist. App builders may compose any relevant Telegraph Intents.', '']
    return '\n'.join(out).rstrip()+'\n'


def render_network_map():
    usage = sorted(((x['name'], x.get('used_by_missions', [])) for x in INTENTS), key=lambda p:(-len(p[1]), p[0]))
    out=['# H2 Intent Coverage & Reuse Map','', 'Which reusable Intents appear across the most Season II missions?', '', '> Mission reuse is **not** market demand. This map only shows how often an Intent appears in the starting H2 mission design.', '', '| Intent | H2 mission count | Missions |', '|---|---:|---|']
    for name,mids in usage:
        if not mids: continue
        out.append(f"| `{name}` | {len(mids)} | {', '.join(mission_name[m] for m in mids)} |")
    out += ['', 'This is **not** a demand score or readiness score. It only shows reuse across the starting mission map. Live demand/readiness belongs in actual usage evidence and GitHub Issues / bounties.', '']
    return '\n'.join(out).rstrip()+'\n'

outputs = {
    ROOT/'docs/INTENTS.md': render_intents(),
    ROOT/'docs/MISSIONS.md': render_missions(),
    ROOT/'docs/NETWORK_MAP.md': render_network_map(),
}

check='--check' in sys.argv
failed=False
for path,content in outputs.items():
    if check:
        if not path.exists() or path.read_text(encoding='utf-8')!=content:
            print(f'OUT OF DATE: {path.relative_to(ROOT)}')
            failed=True
    else:
        path.write_text(content,encoding='utf-8',newline='\n')
        print(f'wrote {path.relative_to(ROOT)}')
if failed: raise SystemExit(1)
