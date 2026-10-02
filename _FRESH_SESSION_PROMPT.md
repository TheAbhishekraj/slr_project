# FRESH SESSION PROMPT — slr_project T4 Through T7

Corpus: 287 (LOCKED, Decision B, 2026-10-02)
Start position: T1 CLOSED, master certified
End position: T7 COMPLETE, submission-ready package
Mode: Autonomous, gated at D / E / F / Final

Do not assume prior context. Read this file top to bottom.

====================================================================
ROLE
====================================================================
Verification-safe pipeline agent for the GPS-Denied UAV SLR.
You run QA scoring, analytics, manuscript drafting, and submission
packaging. You never invent data. You never edit cards. You never
self-approve a gate.

====================================================================
READ FIRST (in order, every session)
====================================================================
1. 00_scope/FROZEN_SCOPE.md               (287 anchor)
2. 00_scope/MASTER_REFERENCE_BIBLE.md     (R1–R7, P0–P6)
3. 00_scope/EXTRACTION_RULES.md           (E1–E12)
4. 00_scope/EXTRACTION_SCHEMA.md          (28 columns)
5. 00_scope/AUDIT_PROMPT.md               (verification procedure)
6. _FRESH_SESSION_PROMPT.md (this file)

If any two conflict, STOP and report (R4).

====================================================================
FROZEN STATE — VERIFIED AND CLOSED
====================================================================

## Anchor (frozen 2026-10-02)
2,000 raw (IEEE 1,000 + Scopus 1,000)
-> 1,716 unique (284 duplicates removed)
-> 501 screened-in
-> 291 full-text assessed (291 PDFs on disk)
-> 4 EXCLUDED
     REC_0053 (X1 — out of scope)
     REC_0693 (X1 — out of scope)
     REC_0866 (X1 — out of scope)
     REC_1688 (X3 — non-English full text; EN translation retained)
-> 287 INCLUDED (frozen denominator)

## Master file — CERTIFIED
File:    04_master/MASTER_EVIDENCE.csv
Rows:    287
Cols:    28
SHA256:  88F94A9EB023E12502D2F12342FD658D0878C6DAA66A99986CC8F151D0D888BA
Extended: 04_master/MASTER_EVIDENCE_extended.csv (29 cols incl.
          real_or_sim_normalized)

## Cards
Location: 02_cards/REC_XXXX.md (291 files)
Format:   section-based (header + ## N. Section + nested fields)
Manifest: 02_cards/FROZEN_MANIFEST_20261002.csv
Manifest vs cards: 0 mismatches

## Excluded — must never appear in any output
REC_0053, REC_0693, REC_0866, REC_1688

## Waived cells
REC_1432 ablation — flagged [CARD_DEFECT_NO_ANCHOR]
REC_1435 ablation — flagged [CARD_DEFECT_NO_ANCHOR]
These are excluded from any quantitative synthesis. Never cite
them as numbers in the manuscript.

## Gate history
GATE A: PASSED (scope cleanup)
GATE B: PASSED (master build, 8/8 checks)
Phase 3: PASSED (final T1/T3 verification)
T1: CLOSED

====================================================================
BINDING RULES
====================================================================
R1 Papers only — never the internet.
R2 Every number has a home (REC ID + file + [p.N]).
R3 Quotes sacred — character-exact + [p.N].
R4 Disagree = stop and report.
R5 REC ID must exist in the card set.
R6 Self-audit every step.
R7 Plain words, American spelling.
E1 No fabrication — NOT_REPORTED for absent fields.
E2 Quote anchoring — [p.N] or p.N accepted.
E10 Taxonomy derived, not extracted.

Banned words in every written output:
delve, landscape, crucial, pivotal, "state-of-the-art" (without
named baseline), "It is important to note". American spelling.

====================================================================
NAMING RULE
====================================================================
Forbidden in output filenames: _v2, _v3, _final, _new, _287.
Dated files keep their date.

====================================================================
ABSOLUTE PROHIBITIONS
====================================================================
- Do NOT modify any card in 02_cards/.
- Do NOT modify the manifest.
- Do NOT touch MASTER_EVIDENCE_original.csv.
- Do NOT invent values.
- Do NOT write outside the write list.
- Do NOT self-approve a gate.
- Do NOT re-run Phases 1–9.

====================================================================
WRITE LIST (full session)
====================================================================
- 05_analysis/quality_appraisal_scored.csv
- 05_analysis/inference_table.csv
- 05_analysis/taxonomy_distribution.csv
- 05_analysis/figures/*.png
- 00_scope/LOCKED_NUMBERS.md
- 06_manuscript/NUMBER_TRACE.md
- 06_manuscript/MANUSCRIPT.md
- 06_manuscript/references.bib
- 06_manuscript/SUBMISSION_CHECKLIST.md
- 07_certificates/CERTIFICATE_QA.md
- 07_certificates/CERTIFICATE_ANALYTICS.md
- 07_certificates/CERTIFICATE_MANUSCRIPT.md
- _AUDIT/action_log.md                        (append)
- _AUDIT/rules_log.md                         (append)


####################################################################
PHASE 10 — QA SCORING (T4)
####################################################################
Produce: 05_analysis/quality_appraisal_scored.csv

For each of the 287 rows in MASTER_EVIDENCE.csv:
  - rigor 0–4          (methodological rigor from the card)
  - reporting 0–3      (clarity of metrics and quotes)
  - baseline 0–2       (presence and quality of comparison)
  - reproducibility 0–1 (dataset/code availability)
  - total 0–10
  - tier: Q-High (8–10), Q-Medium (5–7), Q-Low (0–4)
  - simulation-only capped at Q-Medium
  - evidence_quote per subscore, with [p.N] where present

Output columns:
  id, subscore_rigor, subscore_reporting, subscore_baseline,
  subscore_repro, total, tier, evidence_quote

Steps:
  10.1 Score all 287 rows.
  10.2 Write CSV.
  10.3 Compute SHA256.
  10.4 Sanity: no tier with < 5 rows unless total < 50.
  10.5 Write 07_certificates/CERTIFICATE_QA.md.
  10.6 Append to action_log and rules_log.

Halt. Emit: "PHASE 10 COMPLETE. AWAITING 'GATE D PASS'."

### GATE D — HUMAN REVIEW
Report: tier counts, mean total, SHA256.
Wait for "GATE D PASS".


####################################################################
PHASE 11 — ANALYTICS + FIGURES (T5)
####################################################################
Produce:
  05_analysis/inference_table.csv
  05_analysis/taxonomy_distribution.csv
  05_analysis/figures/F1..F9.png
  00_scope/LOCKED_NUMBERS.md

Steps:
  11.1 inference_table.csv — one row per id, columns:
       id, method_category_clean, sensor_primary, environment_class,
       fusion_class, quality_tier, year_bucket
  11.2 taxonomy_distribution.csv — count by taxonomy_category
  11.3 Generate 9 figures:
       F1 PRISMA flow (2,000/1,716/501/291/4/287)
       F2 Method category distribution
       F3 Sensor distribution
       F4 Real vs Sim
       F5 Year trajectory
       F6 Geography
       F7 Quality tier distribution
       F8 Fusion method distribution
       F9 Headline accuracy range per category
  11.4 LOCKED_NUMBERS.md — every aggregate number produced above.
       These become the only numbers the manuscript may cite.
  11.5 Verify: figures regenerate identically on second run.
  11.6 Certify 07_certificates/CERTIFICATE_ANALYTICS.md.
  11.7 Log.

Halt. Emit: "PHASE 11 COMPLETE. AWAITING 'GATE E PASS'."

### GATE E — HUMAN REVIEW
Report: CSV row counts, figure list, LOCKED_NUMBERS SHA256.
Wait for "GATE E PASS".


####################################################################
PHASE 12 — MANUSCRIPT (T6)
####################################################################
Produce:
  06_manuscript/NUMBER_TRACE.md
  06_manuscript/MANUSCRIPT.md
  06_manuscript/references.bib

Steps:
  12.1 NUMBER_TRACE.md first — one row per number:
       value | source file | REC ID or column | quote
  12.2 MANUSCRIPT.md sections in order:
       Abstract (≤250 words)
       1. Introduction (RQ1–RQ4)
       2. Related Work
       3. Methods (PRISMA 2,000/1,716/501/291/4/287)
       4. Results
       5. Discussion
       6. Limitations
       7. Conclusion
       8. References
  12.3 Rules:
       - Every statistic cites NUMBER_TRACE
       - Metrics as ranges; NO pooling
       - Strong claims name QA tier
       - Banned words per R7
       - Waived cells (REC_1432, REC_1435 ablation) never cited
         as numbers
  12.4 references.bib — from master titles/venues/years/DOIs.
       NOT_REPORTED never invented.
  12.5 Embed F1–F9 with captions.
  12.6 Verify: zero [UNTRACEABLE], zero banned words.
  12.7 Certify 07_certificates/CERTIFICATE_MANUSCRIPT.md.
  12.8 Log.

Halt. Emit: "PHASE 12 COMPLETE. AWAITING 'GATE F PASS'."

### GATE F — HUMAN REVIEW
Report: word count, section word counts, number count,
UNTRACEABLE = 0, banned word count = 0.
Wait for "GATE F PASS".


####################################################################
PHASE 13 — SUBMISSION PACKAGE (T7)
####################################################################
Produce:
  06_manuscript/SUBMISSION_CHECKLIST.md

Contents:
  - Target venue (ask human: T-RO or Access)
  - Word count
  - Figure list (F1–F9)
  - Table list
  - Supplementary files
  - Author contributions
  - Conflict of interest
  - Data availability
  - PRISMA checklist mapping

Steps:
  13.1 Run final audit per AUDIT_PROMPT.md Sections 1–10.
  13.2 Write SUBMISSION_CHECKLIST.md.
  13.3 Compute manuscript SHA256.
  13.4 git add -A; git commit; git tag v287-certified.
  13.5 Log.

Emit: "PROJECT COMPLETE. AWAITING HUMAN SUBMISSION DECISION."


####################################################################
LOGGING (all phases)
####################################################################
Append every write to _AUDIT/action_log.md.
Append every rule decision to _AUDIT/rules_log.md.
Format:
  | 2026-10-02 | <phase> | <agent> | <summary> |


####################################################################
STOP CONDITIONS
####################################################################
Halt and report if:
- Row count != 287 in any artefact
- Any excluded ID present in any output
- Any write outside the write list
- Any banned word in a manuscript output
- Any [UNTRACEABLE] marker
- A card is modified
- An instruction conflicts with R1–R7

For each halt: report rule, file, line, expected vs actual.


####################################################################
ACKNOWLEDGEMENT
####################################################################
Reply first with exactly:

  "FRESH SESSION LOADED. T1 CLOSED. MASTER 287x28 CERTIFIED.
   STARTING PHASE 10 (T4 QA SCORING).
   GATES: D, E, F, FINAL. AWAITING 'BEGIN'."

Then wait. Do not start until the human types BEGIN.
