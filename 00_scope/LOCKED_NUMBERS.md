# LOCKED NUMBERS

Generated: 2026-10-02 (Phase 11 / T5)
Corpus: 287 (LOCKED, Decision B)
Provenance: every number below is produced by 05_analysis/analyze.py
(tables) and 05_analysis/make_figures.py (figures), both committed and
deterministic. These are the ONLY numbers the manuscript may cite
(R2: every number has a home). Supersedes the prior-session LOCKED_NUMBERS
which carried the revoked 143/125/19 tiers and had no F6/F9 blocks.

## PRISMA Flow (source 01_data/*; authority CENSUS_AUDIT_REPORT_20261002.md)
Raw records identified .......... 2,000  (IEEE 1,000 + Scopus 1,000)
Duplicates removed .............. 284
Unique records .................. 1,716
Screened-in (title/abstract) .... 501
Full-text assessed .............. 291
Excluded ........................ 4   (X1 out-of-scope: 3; X3 non-English: 1)
Included (frozen denominator) ... 287

## F2 Method Category Distribution (source inference_table.csv)
HYBRID 78 | VISION_OBJECT 55 | COOPERATIVE 41 | OTHER 29 | VIO 19 |
UNKNOWN 16 | SLAM 13 | LIDAR 9 | UWB 8 | SURVEY 8 | QUANTUM 1 |
OPTICAL_FLOW 1 | SYSTEM 1 | TERRAIN_AIDED_NAVIGATION 1 |
DEEP_LEARNING_ODOMETRY 1 | VISUAL_INERTIAL 1 | MULTI_SENSOR_FUSION 1 |
COOPERATIVE_SWARM_LOCALIZATION 1 | RADAR 1 | DATASET 1 | VSLAM 1
  (21 categories; sum = 287)

## F3 Primary Sensor Distribution (source inference_table.csv)
VISION 182 | IMU_ONLY 35 | OTHER 27 | LIDAR 22 | UWB 14 | RADAR 7
  Method: most token hits in the sensors field; ties -> fixed order.

## F4 Real vs Sim (source MASTER_EVIDENCE.csv column real_or_sim)
REAL 123 | BOTH 88 | SIM 69 | NOT_REPORTED 7

## F5 Year Trajectory (source MASTER_EVIDENCE.csv column year)
2013:1 2014:2 2015:6 2016:21 2017:11 2018:27 2019:32 2020:5 2021:11
2022:36 2023:39 2024:9 2025:16 2026:71
  Year buckets: 2010-2015 = 9 | 2016-2020 = 96 | 2021-2026 = 182

## F6 Geography (source MASTER_EVIDENCE.csv column country, NORMALIZED)
Top 10 (normalized): China 66 | USA 41 | NOT_REPORTED 33 | Canada 14 |
Australia 12 | India 11 | Singapore 11 | Taiwan 11 | Spain 10 | Germany 8
  NORMALIZATION RULE (RULING F6-NORM, logged in _AUDIT/rules_log.md):
    (1) drop the parenthetical affiliation; (2) if a top-level comma
    separates countries, count the study once per country. NOT_REPORTED is
    its own label, never merged into a country.
  OLD vs NEW (traceability):
    China: raw exact string = 28 ; normalized (affiliations merged) = 66
    USA:   raw exact string = 17 ; normalized (affiliations merged) = 41
    NOT_REPORTED: normalized = 33
    Sum of normalized counts = 287 (no study double-counted in this corpus)
  LONG TAIL (STEP C, 2026-10-02): the 70 studies NOT in the Top 10 (Top-10
    sum 217 + 70 = 287) are distributed across 32 further countries:
    Italy 6 | Finland 6 | Iran 6 | South Korea 5 | Brazil 4 | Poland 4 |
    Czech Republic 4 | Turkey 3 | UK 3 | Japan 3 | New Zealand 2 |
    Norway 2 | Mexico 2 | Saudi Arabia 2 | Nepal 1 | Malaysia 1 |
    Morocco 1 | Egypt 1 | Vietnam 1 | Ethiopia 1 | France 1 | Sri Lanka 1 |
    Switzerland 1 | Russia 1 | Lithuania 1 | Philippines 1 | Ukraine 1 |
    Kazakhstan 1 | Greece 1 | Ireland 1 | Belgium 1 | Israel 1
    (32 tail countries; 70 studies; full 42-country distribution now
     complete; 217 + 70 = 287 verified)

## F7 Quality Tier Distribution (source quality_appraisal_scored.csv)
Q-High 145 | Q-Medium 118 | Q-Low 24
  The 49 rows whose raw total >= 8 but tier = Q-Medium are all
  real_or_sim = SIM (simulation-only cap).

## F8 Fusion Method Distribution (source inference_table.csv)
OTHER/UNKNOWN 241 | KALMAN_FILTER 45 | FACTOR_GRAPH 1
  Label "OTHER/UNKNOWN" = the master fusion_method column is NOT_REPORTED
  corpus-wide; fusion is DERIVED from algorithm text, remainder explicitly
  labeled UNKNOWN, not silently dropped.

## F9 Studies Reporting a Numeric Accuracy Metric, by Method Category
   (source MASTER_EVIDENCE.csv headline_result + metrics)
Denominator n = 287 studies.
Inclusion regex: \d+(?:\.\d+)?\s*(m|cm|mm|%)  (case-insensitive), applied
to the concatenation headline_result + ' ' + metrics.
This is a COUNT of studies, NOT a pooled or averaged value (Rule P4).
Studies with a numeric metric (total = 233):
  HYBRID 66 | VISION_OBJECT 48 | COOPERATIVE 35 | OTHER 26 | VIO 19 |
  UNKNOWN 11 | SLAM 10 | UWB 7 | LIDAR 7 | QUANTUM 1 | SYSTEM 1 |
  RADAR 1 | DATASET 1
  RECONCILIATION of the earlier "n = 115" figure (Gate E Issue 2):
    The Gate E plan quoted n = 115. That 115 was an EXPLORATORY count only:
    a narrower regex \d+(\.\d+)?\s*(m|cm|meter(s)?|centimeter(s)?) applied
    to headline_result ALONE. It was never written to any artifact and is
    NOT used anywhere in the pipeline.
    The published 233 uses the broader regex above over headline_result +
    metrics (adding mm and %; adding the metrics column):
      headline_result only, plan regex   = 115  <-- the discarded probe
      headline_result only, script regex = 164
      headline_result + metrics, plan    = 194
      headline_result + metrics, script  = 233  <-- published (F9, LOCKED)
    115 exists nowhere else; the single canonical F9 value is 233/287.

## Taxonomy Distribution (source taxonomy_distribution.csv; Rule E10 derived)
CORE 270 | IMPORTANT 11 | NOT_REPORTED 5 | PERIPHERAL 1
