# 00_scope — slr_project

Authoritative scope, rules, and active prompt for the GPS-Denied UAV SLR.
Corpus LOCKED at 287. Frozen 2026-10-02 (Decision B).

## Read order, every session

1. FROZEN_SCOPE.md
2. EXTRACTION_SCHEMA.md
3. EXTRACTION_RULES.md
4. PHASE_C_MANUAL_EXTRACTION.md
5. MASTER_REFERENCE_BIBLE.md
6. MASTER_PROMPT.md
7. AUDIT_PROMPT.md
8. END_GOAL.md

## LABEL COLLISION — READ THIS BEFORE WRITING ANY CARD
EXTRACTION_RULES.md uses E1–E12 for extraction quality rules.
FROZEN_SCOPE.md uses X1/X3 for PRISMA exclusion codes. These are DIFFERENT.

Disambiguation:
  E1–E12  = extraction quality rules (per EXTRACTION_RULES.md)
  X1, X3  = PRISMA exclusion codes

Exclusion code mapping:
  X1 = out of scope             -> REC_0053, REC_0693, REC_0866
  X3 = non-English full text    -> REC_1688 (EN translation retained)

## Corpus in one line
2,000 -> 1,716 (284 dup) -> 501 screened -> 291 full-text
-> 4 excluded (REC_0053, 0693, 0866 X1; REC_1688 X3)
-> 287 INCLUDED.

## Excluded — never cited in any count, table, figure, or sentence
REC_0053 | REC_0693 | REC_0866 | REC_1688

## X3 evidence
REC_1688 English translation retained at
01_data/02_data_proceesed/REC_1688_translated_EN.txt
SHA256 926a229415d9df488843413fc6a2a099ca3430f05017c8de8fc7a915de88ab8c

## Version history
- v2–v5  superseded (279 corpus, wrong excluded IDs, wrong dup count)
- v6     current — 287 corpus, 284 dups, 4 excluded
- FROZEN_SCOPE.md mirrors v6.

## Open defects
- D-A  OPEN — Rule E3 references `_source_pages`, not in the 28-column schema (Ruling R-B pending in _AUDIT/rules_log.md).
- D-B  CLOSED 2026-10-02 — `_AUDIT/rules_log.md` created; Rule E11 logging target exists.
- D-C  CLOSED 2026-10-02 — FROZEN_MANIFEST_20260927.csv had gone stale (291/291 mismatch) and was RETIRED to 07_certificates/old_manifests/. Current manifest: 02_cards/FROZEN_MANIFEST_20261002.csv — verified 291/291 match, 0 mismatches after X3 label edit re-stamp.


