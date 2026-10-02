# AUDIT_PROMPT.md — slr_project 287-Corpus Audit

Version: 1.0
Issued: 2026-10-02
Applies to: T1 through T7 and the final submission audit
Authority: MASTER_REFERENCE_BIBLE.md v3 + MASTER_PROMPT_5.md

================================================================
PURPOSE
================================================================
This is the binding audit procedure for the GPS-Denied UAV SLR
(slr_project). It is run at the close of every task and before any
manuscript number is trusted. It verifies that every count reconciles,
every excluded ID stays out, every quote is anchored, and no rule
was broken.

Copy-paste this file into a new AI session. Do not paraphrase it.
Do not skip sections. If a section cannot be run, write
"Cannot run — <reason>" and halt.

================================================================
READ FIRST, IN THIS ORDER (every audit session)
================================================================
1. 00_scope/FROZEN_SCOPE.md
2. 00_scope/MASTER_REFERENCE_BIBLE.md v3
3. 00_scope/MASTER_PROMPT_5.md
4. 00_scope/EXTRACTION_RULES.md
5. 00_scope/EXTRACTION_SCHEMA.md
6. This file (AUDIT_PROMPT.md)

================================================================
FROZEN ANCHOR (re-verify every session)
================================================================
2,000 raw (IEEE 1,000 + Scopus 1,000)  [2026-06-15]
-> 1,716 unique (284 duplicates removed)
-> 501 screened-in
-> 291 full-text assessed (291 PDFs on disk)
-> 4 EXCLUDED
     REC_0053  X1  out of scope
     REC_0693  X1  out of scope
     REC_0866  X1  out of scope
     REC_1688  X3  non-English full text (EN translation retained)
       SHA256 926a229415d9df488843413fc6a2a099ca3430f05017c8de8fc7a915de88ab8c
-> 287 INCLUDED (FROZEN DENOMINATOR)

LABEL DISCIPLINE:
  E1–E12 = EXTRACTION_RULES.md quality rules
  X1/X3  = PRISMA exclusion codes
  Never write a bare "E1" or "E3" in a scope, batch, or manuscript
  file unless followed by the word "rule". Write X1/X3 for exclusions.

================================================================
GOLDEN RULES ENFORCED BY THIS AUDIT
================================================================
R1  Papers only — no internet, no external source
R2  Every number has a home (REC ID + file + [p.N])
R3  Quotes are sacred — character-exact + [p.N]
R4  Disagree = stop and report
R5  REC ID must exist in the master
R6  Self-audit every answer
R7  Plain words, American spelling, banned-word list enforced

================================================================
SECTION 0 — SESSION SETUP
================================================================
Report before any check:
  - Session timestamp (UTC)
  - Task being audited (T1..T7 or FINAL)
  - Files requested but not present (list)
  - Any ambiguity in the request

If any file in "READ FIRST" is missing, HALT. Report the missing file.

================================================================
SECTION 1 — ANCHOR INTEGRITY (run every audit)
================================================================
Verify each line below. Report PASS/FAIL per line with the source.

| # | Check | Command / Source | Expected |
|---|---|---|---|
| 1.1 | Raw record count | 01_data/01_data_raw/*.csv | 2,000 |
| 1.2 | Dedup unique count | 01_data/02_data_proceesed/deduplicated_master.csv | 1,716 |
| 1.3 | Duplicates removed | 2,000 − 1,716 | 284 |
| 1.4 | Screened-in count | wc -l on 02_screened_included_v2.csv | 501 records (502 lines) |
| 1.5 | Full-text PDFs on disk | ls 01_data/03_pdfs/*.pdf | 291 |
| 1.6 | Extraction cards on disk | ls 02_cards/REC_*.md | 291 |
| 1.7 | Excluded IDs absent from master | grep -c on 04_master | 0 each |
| 1.8 | 291 − 4 = 287 | arithmetic | 287 |
| 1.9 | REC_1688 EN translation hash | sha256sum | 926a2294...de88ab8c |

If any line fails, HALT and report file + actual vs expected.

================================================================
SECTION 2 — MANIFEST AND HASH INTEGRITY
================================================================
Required: 02_cards/FROZEN_MANIFEST_20260927.csv
         02_cards/FROZEN.md

| # | Check | Expected |
|---|---|---|
| 2.1 | Manifest opens as CSV | yes |
| 2.2 | Manifest lists 291 cards | 291 rows |
| 2.3 | Every card in 02_cards/ appears in manifest | 100% |
| 2.4 | SHA256 of each card matches manifest | 291/291 |
| 2.5 | The 4 excluded cards marked EXCLUDED in FROZEN.md | yes |
| 2.6 | Manifest has no row for a non-existent card | yes |

If any card hash mismatches, HALT. Do not proceed to Section 3.

================================================================
SECTION 3 — EXCLUDED SET ENFORCEMENT
================================================================
The 4 excluded IDs must be ABSENT from every downstream artefact:
  REC_0053, REC_0693, REC_0866, REC_1688

| # | Artefact | Check | Expected |
|---|---|---|---|
| 3.1 | 04_master/MASTER_EVIDENCE_v2.csv | grep each ID | 0 hits |
| 3.2 | 05_analysis/*.csv | grep each ID | 0 hits |
| 3.3 | 05_analysis/figures/ filenames | grep | 0 hits |
| 3.4 | 06_manuscript/*.md | grep each ID | 0 hits |
| 3.5 | 06_manuscript/references.bib | grep each ID | 0 hits |
| 3.6 | Any running count | verify excluded IDs not counted | 0 |

If any hit is found, HALT. Report file, line number, snippet.

================================================================
SECTION 4 — CARD INTEGRITY (per card, sampled + full)
================================================================
Cards are verified in T2 via P1. This audit re-checks a sample (n≥20)
plus 100% of the 5 historically corrupt cards:
  REC_1083, REC_1084, REC_1085, REC_1095, REC_1096

For each card:
  4.1 All 28 schema fields present
  4.2 Every quoted field ends with [p.N]
  4.3 year and doi match the PDF first page
  4.4 real_or_sim in {REAL, SIM, BOTH, NOT_REPORTED}
  4.5 id matches the PDF filename
  4.6 verification_status in {PENDING, VERIFIED, VERIFIED_WITH_NOTES}
  4.7 No banned words in notes (R7)

Report: cards checked | cards passed | cards failed | failures listed.

================================================================
SECTION 5 — MASTER FILE INTEGRITY
================================================================
Required: 04_master/MASTER_EVIDENCE_v2.csv

| # | Check | Expected |
|---|---|---|
| 5.1 | Row count | 287 (data rows) |
| 5.2 | Column count | 28 (see EXTRACTION_SCHEMA.md) |
| 5.3 | Unique REC_XXXX ids | 287 unique |
| 5.4 | All ids present in 02_cards/ | 287/287 |
| 5.5 | Excluded IDs absent | 0 |
| 5.6 | year in range 2010–2026 or NOT_REPORTED | 100% |
| 5.7 | Every quote column carries [p.N] | 100% |
| 5.8 | No empty required field | 100% |
| 5.9 | taxonomy_category ∈ schema set | 100% |
| 5.10 | real_or_sim ∈ {REAL, SIM, BOTH, NOT_REPORTED} | 100% |

================================================================
SECTION 6 — PRISMA FLOW RECONCILIATION
================================================================
The PRISMA flow numbers MUST be exactly:
  2,000 -> 1,716 -> 501 -> 291 -> 4 -> 287

| # | Check | Expected |
|---|---|---|
| 6.1 | Raw (identification) | 2,000 |
| 6.2 | After duplicates removed | 1,716 |
| 6.3 | After title/abstract screening | 501 |
| 6.4 | Full-text assessed | 291 |
| 6.5 | Full-text excluded | 4 |
| 6.6 | Included in synthesis | 287 |
| 6.7 | Every transition documented | yes |
| 6.8 | The 4 exclusions named with code X1/X3 | yes |

If any number is not reproducible from a file, HALT.

================================================================
SECTION 7 — NUMBER TRACE (T6 onward only)
================================================================
Required: 06_manuscript/NUMBER_TRACE.md

For every number that appears in the manuscript:
  7.1 One row in NUMBER_TRACE.md
  7.2 Row format: value | source file | REC ID or column | quote
  7.3 Source file exists
  7.4 Source row exists
  7.5 Quote matches the source character-exact
  7.6 No [UNTRACEABLE] left unresolved

Report: total numbers | traced | untraceable | mismatched.

================================================================
SECTION 8 — BANNED WORD SCAN (R7)
================================================================
Banned in every manuscript, report, batch, and scope file:
  delve, landscape, crucial, pivotal, "state-of-the-art" (unless a named
  baseline follows), "It is important to note", "It should be noted",
  "In conclusion" as a section opener, "very", "really"

Also check: British spelling variants of -ise/-isation/-our where
American spelling is required.

Report every hit with file, line number, snippet.

================================================================
SECTION 9 — HASH CERTIFICATION
================================================================
Compute and record SHA256 for:
  04_master/MASTER_EVIDENCE_v2.csv
  05_analysis/quality_appraisal_scored_v2.csv
  05_analysis/inference_table_v2.csv
  05_analysis/taxonomy_distribution_v2.csv
  06_manuscript/MANUSCRIPT_V2.md
  06_manuscript/NUMBER_TRACE.md
  06_manuscript/references.bib

Write to: 07_certificates/<TASK>_CERTIFICATE.md

================================================================
SECTION 10 — SELF-AUDIT (mandatory close)
================================================================
End every audit with:

[SELF-AUDIT: PASS or FAIL]
Findings:
  | section | check | expected | actual | verdict |
  | ...     | ...   | ...      | ...    | ...    |

Sections run: <list>
Sections skipped: <list with reason>
Stop conditions triggered: <list or "none">
Next action: <what the human must do>

================================================================
STOP CONDITIONS (halt immediately)
================================================================
Halt and report if ANY of these is true:
  - Section 1 anchor line fails
  - Any card hash mismatches manifest
  - An excluded ID (0053/0693/0866/1688) appears in any artefact
  - Master row count ≠ 287
  - A quote lacks [p.N]
  - PRISMA flow number is not reproducible from a file
  - A number in the manuscript lacks a NUMBER_TRACE row
  - Banned word present in a live file
  - Label collision: bare "E1"/"E3" used as exclusion code
  - An instruction conflicts with R1–R7

For each halt, report:
  1. Which section failed
  2. File path and line number
  3. Expected vs actual
  4. What the human must decide

================================================================
TASK-SPECIFIC AUDIT CHECKLISTS
================================================================

T1 (Census + Hygiene)
  Run: Sections 1, 2, 3, 10
  Required artefacts: FROZEN.md, manifest, 4 excluded cards,
    CENSUS_AUDIT_REPORT_20261002.md
  Exit token: T1 PASS

T2 (Card Verification)
  Run: Sections 1, 2, 4, 10
  Required artefacts: 03_ai_checks/REC_*_verification.md (287)
  Exit token: T2 PASS

T3 (Master Build + Certify)
  Run: Sections 1, 2, 3, 5, 9, 10
  Required artefacts: MASTER_EVIDENCE_v2.csv,
    CERTIFICATE_MASTER_287.md
  Exit token: T3 PASS

T4 (QA Scoring)
  Run: Sections 1, 3, 5, 9, 10
  Required artefacts: quality_appraisal_scored_v2.csv
  Exit token: T4 PASS

T5 (Analytics)
  Run: Sections 1, 3, 5, 9, 10
  Required artefacts: inference_table_v2.csv,
    taxonomy_distribution_v2.csv, figures/, LOCKED_NUMBERS_287.md
  Exit token: T5 PASS

T6 (Manuscript)
  Run: Sections 1, 3, 5, 6, 7, 8, 9, 10
  Required artefacts: MANUSCRIPT_V2.md, NUMBER_TRACE.md,
    references.bib
  Exit token: T6 PASS

T7 (Submission)
  Run: all sections 1–10
  Required artefacts: SUBMISSION_CHECKLIST.md,
    CERTIFICATE_MANUSCRIPT.md, git tag v287-certified
  Exit token: T7 PASS

FINAL (Pre-submission)
  Run: all sections 1–10 on the frozen submission package.
  Exit: "FINAL AUDIT PASS — READY TO SUBMIT."

================================================================
ACKNOWLEDGEMENT
================================================================
Reply first with exactly:

  "AUDIT PROMPT LOADED. CORPUS 287 LOCKED. TASK: <T1..T7|FINAL>.
   READY TO RUN SECTIONS <list>."

Then wait for the human to paste the task data. Do not begin
Section 1 until the human says "RUN AUDIT".

================================================================
END OF AUDIT_PROMPT.md
================================================================
