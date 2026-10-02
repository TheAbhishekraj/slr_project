# MASTER REFERENCE BIBLE v3 — DECISION B EDITION (287 CORPUS LOCK)

Repo: slr_project
Frozen: 2026-10-02
One file = everything. Copy-paste only; do not edit prompt text,
only [PASTE] slots.

====================================================================
PART 1 — THE GOAL (paste at the top of every AI session, with P0)
====================================================================
"I am running a PRISMA 2020 systematic literature review 'GPS-Denied
Navigation for UAVs: Multi-Sensor Fusion Approaches (2010-2026)'.
Corpus is LOCKED at 287 papers (Decision B, frozen 2026-10-02). Goal:
100% authentic data — every number traceable to a paper and page. You
verify, you do not invent. Golden rules R1-R7 are in effect."

THE 7 GOLDEN RULES:
R1 PAPERS ONLY: my repo files and PDFs only. Never the internet.
R2 EVERY NUMBER HAS A HOME: number must exist in a file with a REC ID,
   else write [UNTRACEABLE] and stop.
R3 QUOTES ARE SACRED: character-exact + [p.N] page anchor. Not stated =
   NOT_REPORTED. Never guess.
R4 DISAGREE = STOP: two sources conflict -> stop, report both, ask me.
R5 ID CHECK: use a REC ID only if it exists in the master file.
R6 SELF-AUDIT: end every answer with [SELF-AUDIT: PASS/FAIL + findings
   table].
R7 PLAIN WORDS: banned: delve, landscape, crucial, pivotal,
   state-of-the-art (without named baseline), "It is important to note".
   American spelling.

====================================================================
PART 2 — FROZEN ANCHOR (Decision B — this REPLACES all old anchors)
====================================================================
2,000 raw (IEEE 1,000 + Scopus 1,000, searched 2026-06-15)
-> 1,716 unique (284 duplicates removed)
-> 501 screened-in            [VERIFIED 2026-10-02: file count of
   01_data/02_data_proceesed/02_screened_included_v2.csv = 501 records
   (502 lines incl. header). Authority:
   07_certificates/CENSUS_AUDIT_REPORT_20261002.md]
-> 291 full-text assessed (291 PDFs on disk)
-> 4 EXCLUDED:
     REC_0053 (X1 — out of scope)
     REC_0693 (X1 — out of scope)
     REC_0866 (X1 — out of scope)
     REC_1688 (X3 — Chinese full text; English translation kept at
              01_data/02_data_proceesed/REC_1688_translated_EN.txt
              SHA256 926a229415d9df488843413fc6a2a099ca3430f05017c8de8fc7a915de88ab8c)
-> 287 FINAL CORPUS — LOCKED. No additions, no removals, ever, without
   a new signed FROZEN_SCOPE version.

EXCLUSION CODES (distinct from EXTRACTION_RULES E1-E12):
   X1 = out of scope
   X3 = non-English full text (translation retained)
   X2, X4+ = reserved, unused

OLD NUMBERS NOW DEAD (do not carry forward; they were computed on the
old 279 corpus): epochs 26/79/174 | validation 111/83/62/23 | QA 3/98/178
| China 66 / USA 40 | camera 171. New analytics are DERIVED from the
verified 287-corpus master, then frozen as the new locked numbers.

====================================================================
PART 3 — REPO MAP (slr_project — what exists, what each part is for)
====================================================================
00_scope/                       scope, rules, active prompt
01_data/01_data_raw/            2,000 raw export rows (frozen)
01_data/02_data_proceesed/      dedup + screening CSVs (folder typo
                                kept as-is, do not rename)
01_data/03_pdfs/                291 PDFs (frozen)
02_cards/                       291 extraction cards (REC_XXXX.md) +
                                FROZEN.md + FROZEN_MANIFEST_20260927.csv
03_ai_checks/                   AI verification reports (one per card)
04_master/                      the certified master file (built in T3)
05_analysis/                    tables + figures output
06_manuscript/                  manuscript + NUMBER_TRACE + references
07_certificates/                hashes + signed decisions + old_scopes/
tools/                          pipeline scripts

THE 4 EXCLUDED CARDS (REC_0053, 0693, 0866, 1688) stay in 02_cards/ as
records of the decision, but their verification_status = EXCLUDED and
they MUST NOT enter 04_master/ or any count.

====================================================================
PART 4 — AI-GENERATED DATA POLICY
====================================================================
Never delete AI-generated content. Keep it, label it, verify it field by
field against the PDF with prompt P1. AI text without a [p.N] anchor is
never trusted. AI reports live forever in 03_ai_checks/.

====================================================================
PART 5 — THE FROZEN PROMPT PACK (targets updated for 287)
====================================================================
PROMPT P0 — session opener (already in Part 1; always first).

PROMPT P1 — CARD VERIFICATION (once per card; the 4 excluded cards are
skipped — no verification, they are out):
----
You are a verification agent. Golden rules R1-R7 apply; corpus is locked
at 287. I paste (1) an extraction card for REC_XXXX, then (2) the PDF
text in chunks. Wait for my DONE.
After DONE, check the card field by field:
1. QUOTE CHECK: every quoted field must be character-exact from the PDF
   with a correct [p.N] page. List every mismatch.
2. FACT CHECK: year, doi, real_or_sim, sensors, algorithm, dataset vs
   PDF.
3. MISSING CHECK: information the PDF gives but the card says
   NOT_REPORTED.
4. LABEL CHECK: method_category, gps_denied_type, fusion_method,
   contribution_type must be short labels, not paragraphs.
Do NOT fix the card; only report. Missing pages in my text ->
PAGES_MISSING.
End with: verdict = VERIFIED | VERIFIED_WITH_NOTES | FAILED, findings
table (field | card says | PDF says | issue), and [SELF-AUDIT].
[PASTE card]
[PASTE PDF text chunks, then DONE]
----

PROMPT P2 — BATCH FIXES (junk titles / authors / venues / DOIs):
----
Golden rules R1, R3, R5. Task: [TITLES | AUTHORS_VENUES | DOIS]. Inputs
below. Character-exact values only, with source quote + [p.N]. Missing =
NOT_REPORTED. Never use outside sources. Output table: id | field |
corrected_value | source quote. End with [SELF-AUDIT].
[PASTE: affected IDs + their cards / PDF first pages]
----

PROMPT P3 — QA SCORING (new run for the 287 corpus):
----
Golden rules R2, R6. Score each pasted card 0-10 with rubric: rigor 0-4,
reporting 0-3, baseline 0-2, reproducibility 0-1. Tiers: 8-10 Q-High,
5-7 Q-Medium, 0-4 Q-Low; simulation-only capped at Q-Medium. Score ONLY
from what the card quotes show; quote evidence per score. Output: id |
four subscores | total | tier | evidence quote. End with [SELF-AUDIT].
[PASTE: cards in batches]
----

PROMPT P4 — MANUSCRIPT SECTION:
----
Golden rules R1-R7; corpus 287. Write the [SECTION NAME] section of my
IEEE SLR "GPS-Denied Navigation for UAVs: Multi-Sensor Fusion
Approaches (2010-2026)". Hard rules:
1. Cite only REC IDs from this approved list: [PASTE IDs].
2. Every statistic must come from the pasted analysis tables AND exist
   in my NUMBER_TRACE.md. Missing = [UNTRACEABLE], stop that sentence.
3. Strong claims name the QA tier (cite Q-High IDs by name).
4. Metrics as ranges exactly as extracted. No pooling, no averaging.
5. Banned words: delve, landscape, crucial, pivotal, state-of-the-art
   (unless a named baseline follows), "It is important to note".
   American spelling.
End: list every cited REC ID + supporting sentence + [SELF-AUDIT].
[PASTE analysis tables + NUMBER_TRACE.md]
----

PROMPT P5 — REFERENCES: same as before (title/authors/venue/year/DOI
from master + verified cards only; NOT_REPORTED never invented; no
orphan citations). End with [SELF-AUDIT].
[PASTE cited ID list]

PROMPT P6 — FINAL AUDIT:
----
Golden rule R6; corpus 287. Audit the pasted manuscript: (1) every number
vs NUMBER_TRACE.md; (2) every REC ID exists in the master and is not one
of the 4 excluded; (3) every quote has [p.N]; (4) banned-word scan;
(5) PRISMA flow numbers exactly 2,000/1,716/501/291/4/287. Output
findings + [SELF-AUDIT].
[PASTE full manuscript]
----

====================================================================
PART 6 — THE 9 STEPS FOR slr_project (in order; each ends with sign-off)
====================================================================
STEP 1 CENSUS — count 291 PDFs, 291 cards, manifest opens. Verify
  02_screened_included_v2.csv row count = 501.
STEP 2 EXCLUSION HYGIENE — in the 4 excluded cards, set
  verification_status: EXCLUDED. Confirm 291 - 4 = 287.
STEP 3 VERIFY CARDS — run P1 on all 287 in-corpus cards (start with the
  5 historically corrupt: REC_1083, 1084, 1085, 1095, 1096). Reports to
  03_ai_checks/.
STEP 4 BUILD MASTER — python tools/build_master.py 02_cards
  04_master/MASTER_EVIDENCE_v2.csv (script reads only VERIFIED cards;
  expected count 287). Then validate_master.py (expected 287; the 4
  excluded IDs must be ABSENT). Then certify.py.
STEP 5 CROSS-CERTIFY — python tools/compare_masters.py new vs old
  279-row master -> every difference gets a written decision in
  07_certificates/MERGE_DECISIONS.md.
STEP 6 QA SCORE 287 — run P3.
STEP 7 ANALYZE — python tools/analyze.py with corpus target 287. Freeze
  results as LOCKED_NUMBERS_287.md.
STEP 8 MANUSCRIPT — NUMBER_TRACE.md first, then P4 section by section,
  P5 references, P6 final audit.
STEP 9 SUBMIT — certify manuscript, venue format, push to git.

====================================================================
PART 7 — VERIFICATION MATRIX
====================================================================
You: census counts | exclusion review | verdict review per card | every
  compare_masters diff decided in writing | 2 percentages recomputed by
  hand | 3 citations per section vs PDF | 10 DOIs resolve | all
  LOCKED_CHECK MATCH
Scripts: counts | validation | hash stamps | diffs | analysis
AI: card verification (P1) | QA scoring (P3) | drafting (P4-P6) with
  self-audit
NOBODY: invents data, averages conflicts, cites missing/excluded IDs.

====================================================================
LABEL DISAMBIGUATION
====================================================================
EXTRACTION_RULES.md E1-E12  = extraction quality rules
FROZEN_SCOPE.md X1/X3       = PRISMA exclusion codes
Never write a bare "E1" or "E3" in a scope, batch, or manuscript file —
write X1/X3 for exclusions, or "Rule E1/E3" for the rule.

====================================================================
END OF MASTER REFERENCE BIBLE v3
====================================================================


