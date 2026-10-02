#!/usr/bin/env python
"""Phase 11 (T5) - FIGURES F1..F9 for the 287-corpus slr_project SLR.

Deterministic: fixed DPI, no timestamp/uuid in image metadata, sorted inputs.
Running twice reproduces byte-identical PNGs (verified in step 11.5).

  F9 is NOT a pooled/averaged accuracy chart. It is a COUNT of studies that
  report a numeric accuracy/locality metric, per method category. No value
  from one paper is ever combined with another (Rule P4: no pooling).
  Inclusion regex:  \\d+(?:\\.\\d+)?\\s*(m|cm|mm|%)  over headline_result+metrics.
  Denominator n = 287.
"""
import csv, os, re, collections
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# A7 (2026-10-02): submission-grade output. Double-column 7.16 in; filled
# charts 300 dpi; line art (F1 PRISMA, F5 year trajectory) 600 dpi.
WIDTH = 7.16
DPI = 300
DPI_LINE = 600

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, '04_master', 'MASTER_EVIDENCE.csv')
INF = os.path.join(ROOT, '05_analysis', 'inference_table.csv')
FIG = os.path.join(ROOT, '05_analysis', 'figures')
NR = 'NOT_REPORTED'

NUM_METRIC = re.compile(r'\d+(?:\.\d+)?\s*(?:m|cm|mm|%)', re.I)


def norm_country(raw):
    if not raw or raw.strip() == NR:
        return [NR]
    s = raw.strip().split('(')[0].strip().rstrip(' ,;')
    return [p.strip() for p in s.split(',') if p.strip()] or [NR]


def load():
    master = list(csv.DictReader(open(MASTER, encoding='utf-8-sig')))
    inf = {r['id']: r for r in csv.DictReader(open(INF, encoding='utf-8-sig'))}
    return master, inf


def bar(labels, values, title, path, xlabel='', rotate=30, color='#2b6cb0'):
    fig, ax = plt.subplots(figsize=(WIDTH, WIDTH * 0.62))
    ax.bar([str(x) for x in labels], values, color=color)
    ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    ax.set_ylabel('Number of studies')
    plt.xticks(rotation=rotate, ha='right')
    fig.tight_layout()
    fig.savefig(path, dpi=DPI)
    plt.close(fig)


def f1_prisma():
    fig, ax = plt.subplots(figsize=(WIDTH, WIDTH * 0.85))
    ax.axis('off')
    steps = [
        ('Records identified: 2,000 (IEEE 1,000 + Scopus 1,000)', 0.95),
        ('Duplicates removed: 284', 0.82),
        ('Unique records: 1,716', 0.69),
        ('Screened-in (title/abstract): 501', 0.56),
        ('Full-text assessed: 291', 0.43),
        ('Excluded: 4 (X1 out-of-scope 3; X3 non-English 1)', 0.30),
        ('Studies included (frozen denominator): 287', 0.17),
    ]
    for txt, y in steps:
        ax.text(0.5, y, txt, ha='center', va='center', fontsize=10,
                bbox=dict(boxstyle='round', fc='#e6f0fa', ec='#2b6cb0'))
    ax.set_title('F1: PRISMA 2020 Flow')
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, 'F1_PRISMA_flow.png'), dpi=DPI_LINE)
    plt.close(fig)


def main():
    os.makedirs(FIG, exist_ok=True)
    master, inf = load()
    assert len(master) == 287

    f1_prisma()

    c = collections.Counter(r['method_category_clean'] for r in inf.values())
    items = c.most_common()
    bar([k for k, _ in items], [v for _, v in items],
        'F2: Method Category Distribution', os.path.join(FIG, 'F2_Method_Category.png'),
        color='#2f855a')

    c = collections.Counter(r['sensor_primary'] for r in inf.values())
    items = c.most_common()
    bar([k for k, _ in items], [v for _, v in items],
        'F3: Primary Sensor Distribution', os.path.join(FIG, 'F3_Sensor_Distribution.png'),
        color='#805ad5')

    c = collections.Counter((r['real_or_sim'] or NR) for r in master)
    order = ['REAL', 'BOTH', 'SIM', NR]
    bar(order, [c.get(k, 0) for k in order],
        'F4: Real vs Simulation Evidence', os.path.join(FIG, 'F4_Real_vs_Sim.png'),
        rotate=0, color='#c05621')

    yrs = collections.Counter()
    for r in master:
        try:
            yrs[int(r['year'])] += 1
        except (TypeError, ValueError):
            pass
    xs = sorted(yrs)
    fig, ax = plt.subplots(figsize=(WIDTH, WIDTH * 0.62))
    ax.plot(xs, [yrs[y] for y in xs], marker='o', color='#2b6cb0')
    ax.set_title('F5: Publication Year Trajectory')
    ax.set_xlabel('Year'); ax.set_ylabel('Number of studies')
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, 'F5_Year_Trajectory.png'), dpi=DPI_LINE)
    plt.close(fig)

    cc = collections.Counter()
    for r in master:
        for tok in norm_country(r['country']):
            cc[tok] += 1
    items = cc.most_common(10)
    bar([k for k, _ in items], [v for _, v in items],
        'F6: Geography of Lead Institutions (Top 10, normalized)',
        os.path.join(FIG, 'F6_Geography.png'), color='#dd6b20')

    c = collections.Counter(r['quality_tier'] for r in inf.values())
    order = ['Q-High', 'Q-Medium', 'Q-Low']
    bar(order, [c.get(k, 0) for k in order],
        'F7: Quality Tier Distribution', os.path.join(FIG, 'F7_Quality_Tier.png'),
        rotate=0, color='#38a169')

    c = collections.Counter(r['fusion_class'] for r in inf.values())
    items = c.most_common()
    bar([k for k, _ in items], [v for _, v in items],
        'F8: Fusion Method Distribution (OTHER/UNKNOWN = not extracted)',
        os.path.join(FIG, 'F8_Fusion_Method.png'), color='#718096')

    metric_by_cat = collections.Counter()
    for r in master:
        blob = (r.get('headline_result', '') or '') + ' ' + (r.get('metrics', '') or '')
        if NUM_METRIC.search(blob):
            metric_by_cat[inf[r['id']]['method_category_clean']] += 1
    items = metric_by_cat.most_common()
    bar([k for k, _ in items], [v for _, v in items],
        'F9: Studies Reporting a Numeric Accuracy Metric, by Method Category '
        '(counts, NOT pooled values)', os.path.join(FIG, 'F9_Headline_Accuracy.png'),
        color='#b7791f')

    print('figures written to', FIG)
    print('F9 counts:', dict(items))
    print('F9 denominator n:', len(master))
    print('F9 total studies with metric:', sum(metric_by_cat.values()))


if __name__ == '__main__':
    main()