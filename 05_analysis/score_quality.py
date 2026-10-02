#!/usr/bin/env python
"""Phase 10 (T4) - QA SCORING for the 287-corpus slr_project SLR.

Rubric (0-10): rigor 0-4, reporting 0-3, baseline 0-2, repro 0-1.
Tiers: 8-10 Q-High, 5-7 Q-Medium, 0-4 Q-Low. Simulation-only capped at Q-Medium.

Every subscore is DERIVED from what the frozen card actually quotes (Rule E1:
no fabrication; Rule E10: derived, not extracted). The evidence_quote column is
assembled from verbatim card substrings so each score has a visible home
(Rule R2). This script never edits a card; it only reads 02_cards/.

Input : 02_cards/REC_XXXX.md (287 in-corpus cards, manifest INCLUDE rows)
        04_master/MASTER_EVIDENCE.csv  (id order + real_or_sim truth)
Output: 05_analysis/quality_appraisal_scored.csv
"""
import csv, os, re, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, '02_cards')
MANIFEST = os.path.join(CARDS, 'FROZEN_MANIFEST_20261002.csv')
MASTER = os.path.join(ROOT, '04_master', 'MASTER_EVIDENCE.csv')
OUT = os.path.join(ROOT, '05_analysis', 'quality_appraisal_scored.csv')

EXCLUDED = {'REC_0053', 'REC_0693', 'REC_0866', 'REC_1688'}
NR = 'NOT_REPORTED'

REPRO_POS = re.compile(
    r'(publicly available|open[- ]source|open[- ]dataset|github|available at|'
    r'released|downloadable|dataset is available|available online|'
    r'TUM RGB-D|EuRoC|KITTI|Competition|OpenVINS|MAV|'
    r'we release|is open)', re.I)


def get_section(text, num_name):
    m = re.search(rf'(?m)^##\s*{num_name}\.\s*(.*?)(?=^##\s|\Z)', text, re.S)
    return m.group(1).strip() if m else ''


def first_quote(block, limit=200):
    m = re.search(r'"(.+?)"', block, re.S)
    if not m:
        return ''
    q = m.group(1).strip()
    q = re.sub(r'\s+', ' ', q)
    return (q[:limit] + '...') if len(q) > limit else q


def has_table(block):
    return bool(re.search(r'(?m)^\|.*\|.*\|', block))


def table_has_numbers(block):
    """A metric table with at least one numeric data row."""
    for line in block.splitlines():
        if line.strip().startswith('|') and re.search(r'\d\.\d|\d\s*%|\d\s*(m|cm|mm|km|dB|s)\b', line):
            return True
    return False


NUM_MEASURE = re.compile(r'\d+(?:\.\d+)?\s*(?:m|cm|mm|km|%|dB|deg|Hz|s)\b', re.I)


def score_card(text, real_or_sim):
    """Return (rigor, reporting, baseline, repro, total, tier, evidence_quote)."""
    sec = {n: get_section(text, str(n)) for n in range(1, 19)}

    # ---- RIGOR 0-4 (study design + evaluation depth) ----
    # 1 base for a stated method; +1 evaluation setup; +1 quantitative
    # result with numbers; +1 ablation/sensitivity OR a controlled
    # multi-condition comparison. Pure surveys/position papers stay low.
    rigor = 0
    method = sec[5]
    has_method = bool(method and method != NR)
    if has_method:
        rigor += 1
    exp = sec[7]
    has_exp = bool(exp and exp != NR)
    if has_method and has_exp:
        rigor += 1
    hr = sec[8]
    has_numbers = bool(hr and hr != NR and (table_has_numbers(hr) or NUM_MEASURE.search(hr)))
    if has_numbers:
        rigor += 1
    abl = sec[9]
    has_abl = bool(abl and abl != NR and 'NOT_REPORTED' not in abl)
    base_txt = re.search(r'baselines?\s*:\s*(.*)', exp, re.I)
    base_txt = base_txt.group(1).strip() if base_txt else ''
    multi_cond = bool(base_txt and 'NO_BASELINE' not in base_txt.upper() and base_txt != NR)
    if has_abl or (has_numbers and multi_cond):
        rigor += 1
    rigor = min(4, rigor)

    # ---- REPORTING 0-3 (clarity of metrics + quotes) ----
    # 1 numeric headline; +1 tabular metrics; +1 anchored verbatim quote
    reporting = 0
    if has_numbers:
        reporting += 1
    if has_table(hr):
        reporting += 1
    anchored = bool(re.search(r'\[p\.\s*\d', text))
    if anchored:
        reporting += 1
    reporting = min(3, reporting)

    # ---- BASELINE 0-2 ----
    baseline = 0
    if base_txt and base_txt != NR and 'NO_BASELINE' not in base_txt.upper():
        baseline = 1
        if re.search(r'[A-Za-z]', base_txt) and has_numbers:
            baseline = 2
    baseline = min(2, baseline)

    # ---- REPRODUCIBILITY 0-1 ----
    repro = 1 if (REPRO_POS.search(sec[7]) or REPRO_POS.search(text)) else 0

    total = rigor + reporting + baseline + repro
    tier = 'Q-High' if total >= 8 else ('Q-Medium' if total >= 5 else 'Q-Low')
    if real_or_sim == 'SIM' and tier == 'Q-High':
        tier = 'Q-Medium'

    parts = []
    if has_method:
        parts.append('method: ' + first_quote(sec[5], 120))
    if has_table(hr):
        clean = re.sub(r'(?m)^\|.*$', '', hr)
        q = first_quote(clean, 120)
        parts.append('metrics: ' + (q if q else 'numeric metric table present'))
    elif has_numbers:
        parts.append('headline: ' + first_quote(hr, 120))
    parts.append('baseline: ' + (first_quote(exp, 100) if baseline > 0 else 'NO_BASELINE'))
    if repro == 1:
        parts.append('repro: ' + first_quote(exp, 100))
    ev = ' | '.join(p for p in parts if p)
    return rigor, reporting, baseline, repro, total, tier, ev[:900]


def main():
    master = list(csv.DictReader(open(MASTER, encoding='utf-8-sig')))
    assert len(master) == 287, f'master rows {len(master)} != 287'
    real = {r['id']: (r['real_or_sim'] or '').strip() for r in master}

    manifest = list(csv.DictReader(open(MANIFEST, encoding='utf-8-sig')))
    include = [r['id'] for r in manifest if r.get('status', '').strip().upper() == 'INCLUDE']
    assert set(include) == set(real), 'manifest INCLUDE set != master id set'
    for eid in EXCLUDED:
        assert eid not in real, f'excluded id {eid} present in master'

    rows = []
    for rid in include:
        text = open(os.path.join(CARDS, f'{rid}.md'), encoding='utf-8').read()
        r, rep, b, rp, t, tier, ev = score_card(text, real[rid])
        rows.append({'id': rid, 'subscore_rigor': r, 'subscore_reporting': rep,
                     'subscore_baseline': b, 'subscore_repro': rp, 'total': t,
                     'tier': tier, 'evidence_quote': ev})

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['id', 'subscore_rigor',
            'subscore_reporting', 'subscore_baseline', 'subscore_repro',
            'total', 'tier', 'evidence_quote'])
        w.writeheader()
        w.writerows(rows)

    n = len(rows)
    mean = sum(r['total'] for r in rows) / n
    tiers = {}
    for r in rows:
        tiers[r['tier']] = tiers.get(r['tier'], 0) + 1
    sha = hashlib.sha256(open(OUT, 'rb').read()).hexdigest().upper()

    print(f'rows={n}')
    print(f'tiers={dict(sorted(tiers.items()))}')
    print(f'mean_total={mean:.4f}')
    for s in ['subscore_rigor', 'subscore_reporting', 'subscore_baseline', 'subscore_repro']:
        print(f'  mean {s} = {sum(r[s] for r in rows)/n:.3f}')
    print(f'SHA256={sha}')


if __name__ == '__main__':
    main()