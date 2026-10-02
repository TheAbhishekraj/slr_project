#!/usr/bin/env python
"""Phase 11 (T5) - ANALYTICS for the 287-corpus slr_project SLR.

Produces:
  05_analysis/inference_table.csv        one row per id, derived labels
  05_analysis/taxonomy_distribution.csv  count by taxonomy_category (Rule E10)

All labels are DERIVED from the certified master + frozen cards (Rule E1 no
fabrication; Rule E10 derived). No card is modified.

Country normalization (RULING F6-NORM, logged in _AUDIT/rules_log.md):
  a raw `country` string is normalized to its leading country name by
  (1) taking the text before the first '(' and (2) if that text contains a
  top-level ',', the whole string counts once for EACH comma-separated
  country (one count per country). Parenthetical affiliations are dropped.
  `NOT_REPORTED` is kept as its own label, never merged into a country.
"""
import csv, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, '04_master', 'MASTER_EVIDENCE.csv')
CARDS = os.path.join(ROOT, '02_cards')
OUT_INF = os.path.join(ROOT, '05_analysis', 'inference_table.csv')
OUT_TAX = os.path.join(ROOT, '05_analysis', 'taxonomy_distribution.csv')

EXCLUDED = {'REC_0053', 'REC_0693', 'REC_0866', 'REC_1688'}
NR = 'NOT_REPORTED'

CANON_METHODS = {
    'HYBRID', 'SLAM', 'OTHER', 'VISION_OBJECT', 'QUANTUM', 'VIO', 'UWB',
    'COOPERATIVE', 'SURVEY', 'OPTICAL_FLOW', 'SYSTEM', 'LIDAR',
    'TERRAIN_AIDED_NAVIGATION', 'DEEP_LEARNING_ODOMETRY', 'VISUAL_INERTIAL',
    'MULTI_SENSOR_FUSION', 'COOPERATIVE_SWARM_LOCALIZATION', 'RADAR',
    'DATASET', 'VSLAM',
}

VISION_RE = re.compile(r'camera|vision|visual|stereo|monocular|opencv|aruco|zed|realsense|rgb|image|optical flow|landmark|v-slam|vslam', re.I)
LIDAR_RE = re.compile(r'lidar|laser|point cloud|loam|hector|cartographer|depth camera', re.I)
RADAR_RE = re.compile(r'radar|millimeter', re.I)
IMU_RE = re.compile(r'\bimu\b|inertial|gyro|accelerometer|\bins\b', re.I)
UWB_RE = re.compile(r'\buwb\b|ultra-wideband|ultra wideband', re.I)

FUSION_KF = re.compile(r'\bekf\b|kalman|unscented|federated filter', re.I)
FUSION_FG = re.compile(r'factor graph|graph optimi|gtsam|isam|bundle adjustment|ceres', re.I)

YEAR_BUCKETS = [(2010, 2015, '2010-2015'), (2016, 2020, '2016-2020'),
                (2021, 2026, '2021-2026')]


def norm_country(raw):
    """Return a list of normalized country tokens for one raw string."""
    if not raw or raw.strip() == NR:
        return [NR]
    s = raw.strip().split('(')[0].strip()
    s = s.rstrip(' ,;')
    parts = [p.strip() for p in s.split(',') if p.strip()]
    return [p for p in parts] or [NR]


def clean_sensor(sensors_text):
    """Primary sensor = the category with the most token hits in `sensors`.

    Counting hits (rather than first-match) prevents a paper that merely
    mentions 'UWB' once from outranking a vision-dominant platform. Ties
    break by the fixed priority order below.
    """
    t = (sensors_text or '').lower()
    counts = {
        'VISION': len(VISION_RE.findall(t)),
        'LIDAR': len(LIDAR_RE.findall(t)),
        'UWB': len(UWB_RE.findall(t)),
        'RADAR': len(RADAR_RE.findall(t)),
        'IMU_ONLY': len(IMU_RE.findall(t)),
    }
    best = max(counts, key=lambda k: counts[k])
    if counts[best] == 0:
        return 'OTHER'
    return best


def classify_fusion(*texts):
    blob = ' '.join(x or '' for x in texts)
    if FUSION_FG.search(blob):
        return 'FACTOR_GRAPH'
    if FUSION_KF.search(blob):
        return 'KALMAN_FILTER'
    return 'OTHER/UNKNOWN'


def env_class(gps_denied_type):
    g = (gps_denied_type or NR).strip().upper()
    if g in ('INDOOR', 'UNDERGROUND', 'FOREST', 'URBAN_CANYON', 'MIXED'):
        return g
    if g in ('GNSS_SPOOFED', 'TOTAL_OUTAGE', 'CONTESTED_OR_DENIED',
             'LONG_TERM_DENIED'):
        return 'GNSS_DENIED_OTHER'
    return 'NOT_REPORTED'


def year_bucket(year):
    try:
        y = int(year)
    except (TypeError, ValueError):
        return NR
    for lo, hi, name in YEAR_BUCKETS:
        if lo <= y <= hi:
            return name
    return NR


def get_section(text, num_name):
    m = re.search(rf'(?m)^##\s*{num_name}\.\s*(.*?)(?=^##\s|\Z)', text, re.S)
    return m.group(1).strip() if m else ''


def taxonomy(text):
    sec = get_section(text, '13')
    if not sec:
        return NR
    # drop the section title line ("Taxonomy Category"); keep the body
    body = sec.split('\n', 1)[1] if '\n' in sec else sec
    up = body.strip().upper()
    for tok in ('CORE', 'IMPORTANT', 'PERIPHERAL', 'NOT_REPORTED'):
        if up.startswith(tok):
            return tok
    return NR


def main():
    master = list(csv.DictReader(open(MASTER, encoding='utf-8-sig')))
    assert len(master) == 287, f'master rows {len(master)} != 287'
    for r in master:
        assert r['id'] not in EXCLUDED, f'excluded id {r["id"]} in master'

    qa = {r['id']: r['tier'] for r in csv.DictReader(
        open(os.path.join(ROOT, '05_analysis', 'quality_appraisal_scored.csv'),
             encoding='utf-8-sig'))}

    inf_rows, tax_rows = [], []
    for r in master:
        rid = r['id']
        mc = (r['method_category'] or NR).strip()
        method_clean = mc if mc in CANON_METHODS else ('UNKNOWN' if mc == NR else mc)
        inf_rows.append({
            'id': rid,
            'method_category_clean': method_clean,
            'sensor_primary': clean_sensor(r['sensors']),
            'environment_class': env_class(r['gps_denied_type']),
            'fusion_class': classify_fusion(r['fusion_method'], r['algorithm'], r['approach_summary']),
            'quality_tier': qa.get(rid, NR),
            'year_bucket': year_bucket(r['year']),
        })
        card = open(os.path.join(CARDS, f'{rid}.md'), encoding='utf-8').read()
        tax_rows.append({'id': rid, 'taxonomy_category': taxonomy(card)})

    with open(OUT_INF, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['id', 'method_category_clean',
            'sensor_primary', 'environment_class', 'fusion_class',
            'quality_tier', 'year_bucket'])
        w.writeheader(); w.writerows(inf_rows)

    tc = collections.Counter(t['taxonomy_category'] for t in tax_rows)
    with open(OUT_TAX, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['taxonomy_category', 'count'])
        for k in sorted(tc):
            w.writerow([k, tc[k]])

    print('inference rows:', len(inf_rows))
    print('taxonomy:', dict(sorted(tc.items())))
    for col in ['method_category_clean', 'sensor_primary', 'environment_class',
                'fusion_class', 'quality_tier', 'year_bucket']:
        print(col, '=>', dict(collections.Counter(x[col] for x in inf_rows).most_common()))


if __name__ == '__main__':
    main()