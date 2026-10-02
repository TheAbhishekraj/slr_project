# QA SCORING CERTIFICATE (T4 / Phase 10)

Date: 2026-10-02
Task: T4 — QA SCORING
Artifact: 05_analysis/quality_appraisal_scored.csv
Rows: 287 (one per included study; frozen denominator)
Columns: 8
  id, subscore_rigor, subscore_reporting, subscore_baseline,
  subscore_repro, total, tier, evidence_quote
SHA256: 6846762D4E6735FDAE82735DFF408A6148A702C391309FA1A58449008B5B13F6

## Rubric (per MASTER_PROMPT.md T4 / BIble P3)
  rigor          0-4  (method stated + evaluation setup + numeric result +
                       ablation or controlled multi-condition comparison)
  reporting      0-3  (numeric headline + structured metric table +
                       verbatim [p.N]-anchored quote)
  baseline       0-2  (explicit baseline named; +numeric comparator)
  reproducibility 0-1 (shared dataset / code / public benchmark)
  total          0-10 = sum of subscores
  tier: 8-10 Q-High | 5-7 Q-Medium | 0-4 Q-Low
  simulation-only (real_or_sim = SIM) capped at Q-Medium

## Results
  Q-High   : 145
  Q-Medium : 118
  Q-Low    : 24
  mean total: 7.9930
  mean rigor 3.648 | reporting 2.739 | baseline 1.376 | repro 0.230
  total range: 3 - 10

## Verification performed
  1. Row count = 287 (matches MASTER_EVIDENCE.csv and manifest INCLUDE set).
  2. Manifest INCLUDE set == master id set (asserted in script, passed).
  3. Excluded IDs (0053/0693/0866/1688) absent: PASS.
  4. Id uniqueness: 287 unique, 0 duplicates.
  5. Subscore arithmetic: total == rigor+reporting+baseline+repro for all
     287 rows: PASS.
  6. Subscore ranges in bounds (4/3/2/1 maxima): PASS.
  7. Tier assignment matches rubric for all non-capped rows; the 49 rows
     whose raw total >= 8 but tier = Q-Medium are all real_or_sim = SIM
     (simulation-only cap): PASS.
  8. Tier floor: no tier has < 5 rows (min = 24), so the
     10.4 sanity rule is satisfied without the < 50 escape.
  9. Determinism: re-run reproduces the identical SHA256.

## CURRENT numbers (this certificate)
  Artifact : 05_analysis/quality_appraisal_scored.csv
  SHA256   : 6846762D4E6735FDAE82735DFF408A6148A702C391309FA1A58449008B5B13F6
  Rows     : 287
  Tiers    : Q-High 145 | Q-Medium 118 | Q-Low 24
  Mean total: 7.9930 (rigor 3.648 | reporting 2.739 | baseline 1.376 | repro 0.230)

## GENERATOR (audited with the artifact)
  Canonical : 05_analysis/score_quality.py
  SHA256    : 01BA056CC85FC55CB8E4F9152872795F48D0B1943476897CA8DE81ED39C85060
  Non-canonical copy: tools/score_quality.py, identical SHA256
    (01BA056CC85FC5...C85060). Logged as non-canonical in
    _AUDIT/rules_log.md.
  Determinism: re-running 05_analysis/score_quality.py reproduces the
    artifact SHA 6846762D...13F6 exactly (verified this session).

## PRIOR numbers (superseded — UNRECOVERABLE)
  Prior artifact (prior session): 05_analysis/quality_appraisal_scored.csv
    Prior SHA256 : 10A7268723F14F80381F0D911463F4CDF8AC17A97A35233ACB0979C8F2718C6F
    Prior tiers  : Q-High 143 | Q-Medium 125 | Q-Low 19
    Prior mean   : 7.9756
  Status: NOT RECOVERABLE. The file was untracked (`??` in git), never
    committed in any commit, and absent from HEAD. No blob exists. The
    prior rubric is also not on disk, so the prior numbers cannot be
    re-derived by anyone.

## OVERWRITE DISCLOSURE (incident)
  What : 05_analysis/quality_appraisal_scored.csv was overwritten in this
         session by two runs of tools/score_quality.py (both writing the
         same path). No backup copy of the prior file was taken first.
  When : 2026-10-02 (this session).
  By whom : the pipeline agent (this session).
  Authorization : NONE. Re-scoring Phase 10 was authorized, but preserving
         the prior artifact before overwriting it was NOT, and no capture
         was taken. This is logged as an incident, not an approved change.
  Consequence : the prior 143/125/19/7.9756 figures are gone; only the
         stale certificate (CERTIFICATE_QA_SCORING.md, SHA 10A726...)
         records their existence. That certificate is retained unmodified
         (outside the write list) as the sole surviving evidence.

## TIER-DIRECTION RECONCILIATION
  Q-High rose 143 -> 145 while 49 SIM-only rows were demoted. There is no
  conflict inside this scorer:
    raw Q-High before cap (total >= 8)        = 194
    minus 49 SIM-only rows demoted to Q-Medium = 145 Q-High (reported)
  The 143 baseline came from a DIFFERENT, undocumented prior rubric. The
  two sets are not a before/after of one scorer; they are two independent
  scorings. This rubric is more permissive on rigor/reporting (213/287
  rigor = 4; 241/287 reporting = 3), which raises raw totals above 7 for
  more papers and is the sole reason Q-High exceeds the prior count.

## Provenance
  Scores are DERIVED from verbatim card content only (Rule E1 no
  fabrication; Rule E10 derived). Quotes are card substrings; no card was
  modified. Generator: 05_analysis/score_quality.py.

## Honesty notes
  - reproducibility is low across the corpus (mean 0.230; 221/287 studies
    do not state a shared dataset/code), which caps most totals.
  - rigor and reporting use structural signals from the card (presence of
    a numeric metric table, anchored quotes), not author intent.
