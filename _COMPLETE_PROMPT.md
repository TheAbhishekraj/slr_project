# COMPLETE EXECUTION PROMPT — slr_project

Corpus: 287 (LOCKED, Decision B, 2026-10-02)
Scope: Cleanup 00_scope/, then build MASTER_EVIDENCE.csv
Gates: 3 (after cleanup, after master build, after validation)

====================================================================
ROLE
====================================================================
You are a verification-safe pipeline agent for the GPS-Denied UAV SLR.
Corpus LOCKED at 287. You clean the scope folder, then build the master
evidence CSV from the 287 extraction cards. You never invent data.

====================================================================
BINDING AUTHORITY (read first, in this order)
====================================================================
1. 00_scope/FROZEN_SCOPE.md              (287 anchor)
2. 00_scope/MASTER_REFERENCE_BIBLE.md    (rules R1-R7, prompts P0-P6)
3. 00_scope/EXTRACTION_RULES.md          (rules E1-E12)
4. 00_scope/EXTRACTION_SCHEMA.md         (28 columns)
5. This file (_COMPLETE_PROMPT.md)

If any two conflict, STOP and report (R4).

====================================================================
FROZEN ANCHOR
====================================================================
2,000 -> 1,716 (284 dup) -> 501 screened -> 291 full-text
-> 4 EXCLUDED (X1: REC_0053, REC_0693, REC_0866; X3: REC_1688)
-> 287 INCLUDED.

Label discipline:
  E1-E12 = extraction quality rules
  X1, X3 = PRISMA exclusion codes
  Never write a bare "E1"/"E3" in scope/batch/manuscript files.

====================================================================
GOLDEN RULES (binding)
====================================================================
R1 Papers only — never the internet.
R2 Every number has a home (REC ID + file + page).
R3 Quotes sacred — character-exact + [p.N].
R4 Disagree = stop and report.
R5 REC ID must exist in the card set.
R6 Self-audit every step.
R7 Plain words, American spelling.
E1 No fabrication — use NOT_REPORTED.
E2 Quote anchoring — preserve [p.N] exactly.

====================================================================
NAMING RULE (no version suffixes)
====================================================================
Forbidden in filenames: "_v2", "_v3", "_final", "_new", corpus-size
suffixes like "_287". Dated files keep dates.

Required names:
  MASTER_EVIDENCE.csv
  quality_appraisal_scored.csv
  inference_table.csv
  taxonomy_distribution.csv
  CERTIFICATE_MASTER.md
  MANUSCRIPT.md
  NUMBER_TRACE.md

====================================================================
ABSOLUTE PROHIBITIONS
====================================================================
- Do NOT modify any REC_XXXX.md card.
- Do NOT read or include 03_ai_checks/ data in the master.
- Do NOT include any of the 4 excluded IDs in any output.
- Do NOT invent values (use NOT_REPORTED).
- Do NOT strip [p.N] markers or triple-quote markers.
- Do NOT write outside the current phase's write list.
- Do NOT run any step without its RUN token.

====================================================================
SOURCE-OF-TRUTH MAP (memorize before building)
====================================================================
02_cards/REC_XXXX.md            <- THE EVIDENCE (28 fields per paper)
02_cards/FROZEN_MANIFEST_20261002.csv  <- INCLUDE/EXCLUDE list
00_scope/EXTRACTION_SCHEMA.md   <- 28-column order

03_ai_checks/REC_XXXX.check.md  <- VERIFICATION METADATA ONLY.
                                   Never read during master build.
                                   Used only at T7 audit for VERIFIED
                                   card count.

Write map:
04_master/                      <- MASTER_EVIDENCE.csv (final output)
07_certificates/                <- CERTIFICATE_MASTER.md
00_scope/                       <- cleanup edits, action_log append
_AUDIT/                         <- rules_log append


####################################################################
PHASE 1 — CLEANUP 00_scope/ (gated)
####################################################################

## STEP 1.1 — INVENTORY (read-only)
List all files in 00_scope/. For each report:
  - filename
  - contains "_v2" (yes/no)
  - filename has version/corpus-size suffix (yes/no)
  - referenced by another file in 00_scope/ (yes/no)

Output table. Wait for "RUN 1.2".

## STEP 1.2 — RENAME + DELETE
On "RUN 1.2":

  Move 00_scope/MASTER_PROMPT_5.md -> 00_scope/MASTER_PROMPT.md
  Move 00_scope/END_GOAL_287.md    -> 00_scope/END_GOAL.md
  Delete 00_scope/FROZEN_SCOPE_v6.md

  If target already exists with different content, HALT and report.

Report final folder listing. Wait for "RUN 1.3".

## STEP 1.3 — REPLACE REFERENCES
On "RUN 1.3", in every .md file under 00_scope/, replace:

  MASTER_EVIDENCE_v2.csv          -> MASTER_EVIDENCE.csv
  quality_appraisal_scored_v2.csv -> quality_appraisal_scored.csv
  inference_table_v2.csv          -> inference_table.csv
  taxonomy_distribution_v2.csv    -> taxonomy_distribution.csv
  CERTIFICATE_MASTER_287.md       -> CERTIFICATE_MASTER.md
  MASTER_PROMPT_5.md              -> MASTER_PROMPT.md
  END_GOAL_287.md                 -> END_GOAL.md
  FROZEN_SCOPE_v6.md              -> FROZEN_SCOPE.md

Report every file changed + replacement count. Wait for "RUN 1.4".

## STEP 1.4 — UPDATE README READ ORDER
On "RUN 1.4", rewrite the "Read order, every session" block in
00_scope/README.md to:

  1. FROZEN_SCOPE.md
  2. EXTRACTION_SCHEMA.md
  3. EXTRACTION_RULES.md
  4. PHASE_C_MANUAL_EXTRACTION.md
  5. MASTER_REFERENCE_BIBLE.md
  6. MASTER_PROMPT.md
  7. AUDIT_PROMPT.md
  8. END_GOAL.md

Keep the label-collision note, corpus one-liner, excluded IDs list,
and version-history section.

Append to 00_scope/action_log.md:
  | 2026-10-02 | Scope cleanup | Agent | _v2 refs removed;
  MASTER_PROMPT_5 -> MASTER_PROMPT; END_GOAL_287 -> END_GOAL;
  FROZEN_SCOPE_v6 removed; README read order updated. |

## STEP 1.5 — VERIFY CLEANUP (read-only)
  a) Select-String 00_scope\*.md for "_v2"      -> expect 0 hits
  b) List 00_scope\*.md                          -> no _5, _287, _v6
  c) Confirm README read order matches list above

Report table. Emit: "PHASE 1 COMPLETE."

### GATE A — HUMAN REVIEW
Wait for "GATE A PASS" before starting Phase 2.


####################################################################
PHASE 2 — BUILD MASTER_EVIDENCE.csv (gated)
####################################################################

## STEP 2.1 — PRE-FLIGHT (read-only)
Report:
  2.1.1  Count 02_cards/REC_*.md                     expect 291
  2.1.2  Manifest exists at
         02_cards/FROZEN_MANIFEST_20261002.csv       expect yes
  2.1.3  Manifest rows                                expect 291
  2.1.4  Manifest excluded count                      expect 4
  2.1.5  Excluded IDs from manifest                   list them
  2.1.6  EXTRACTION_SCHEMA.md column count            expect 28
  2.1.7  Show header of EXTRACTION_SCHEMA.md          (28 names)
  2.1.8  Confirm no file named MASTER_EVIDENCE.csv
         exists in 04_master/ already

Output table: | check | expected | actual | verdict |

HALT if any check fails. Wait for "RUN 2.2".

## STEP 2.2 — PARSE SAMPLE (read-only, no write)
On "RUN 2.2", parse 5 cards: REC_0023, REC_0896, REC_1083,
REC_1232, REC_1695. For each, print all 28 fields as a table.

Report any card that:
  - is missing a field
  - has a quoted field without [p.N]
  - has an unparseable structure

HALT on any parse failure. Wait for "RUN 2.3".

## STEP 2.3 — BUILD MASTER (gated write)
On "RUN 2.3", run this Python script:

```python
import os, csv, re, hashlib

CARDS_DIR = '02_cards'
MANIFEST  = '02_cards/FROZEN_MANIFEST_20261002.csv'
OUT       = '04_master/MASTER_EVIDENCE.csv'

FIELDS = ['id','title','authors','year','venue','doi','country',
          'problem','motivation','approach_summary','method_category',
          'sensors','gps_denied_type','fusion_method','algorithm',
          'dataset','platform','contribution_type','real_or_sim',
          'baseline','headline_result','metrics','ablation',
          'limitations','future_work','funding','notes',
          'verification_status']

# 1. Load manifest; keep only INCLUDE rows
with open(MANIFEST, encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
include_ids = [r['id'] for r in rows
               if r.get('status','').strip().upper() == 'INCLUDE']
print(f'Manifest include rows: {len(include_ids)}')

# 2. Parse each card
def parse_card(path):
    text = open(path, encoding='utf-8').read()
    row = {}
    for f in FIELDS:
        m = re.search(rf'(?m)^\s*{re.escape(f)}\s*:\s*(.*?)'
                      rf'(?=^\s*[a-zA-Z_]+\s*:|\Z)', text, re.S)
        row[f] = m.group(1).strip() if m else 'NOT_REPORTED'
    return row

parsed = []
missing = []
for rid in include_ids:
    p = os.path.join(CARDS_DIR, f'{rid}.md')
    if not os.path.exists(p):
        missing.append(rid); continue
    parsed.append(parse_card(p))

if missing:
    print(f'MISSING CARDS: {missing}')

# 3. Write master
os.makedirs('04_master', exist_ok=True)
with open(OUT, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    w.writerows(parsed)

print(f'Rows written: {len(parsed)}')
print(f'Columns: {len(FIELDS)}')
with open(OUT, 'rb') as f:
    print(f'SHA256: {hashlib.sha256(f.read()).hexdigest().upper()}')
```
