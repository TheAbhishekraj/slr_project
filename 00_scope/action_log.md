# 00_scope Action Log

| Date | Action | Performed By | Notes |
| :--- | :--- | :--- | :--- |
| 2026-10-02 | Initialized directory | System | Directory setup and log created. |
| 2026-10-02 | Census verified | Human | 291 PDFs, 291 cards, 501 screened. T1 sub-checks 1-4 pass. |
| 2026-10-02 | REC_1688 EN translation hash logged | Human | SHA256 926a2294...de88ab8c; X3 evidence record. |
| 2026-10-02 | Issue A ruled (Option A) | Human | 6 deferred records (REC_0023, 0035, 0244, 0363, 1217, 1667) are IN the 287; twin links to MERGE_DECISIONS.md. |
| 2026-10-02 | .txt files purged from 01_data/03_pdfs/ | Human | 6 .txt removed; translation moved to 02_data_proceesed/. PDF folder frozen at 291. |
| 2026-10-02 | Git commit 2ad5d0c pushed to main | Human | Corpus freeze committed. |
| 2026-10-02 | EXTRACTION_RULES.md received | Human | Rules E1–E12 read and audited. |
| 2026-10-02 | COLLISION FOUND | Agent | E1/E3 used for both extraction rules and exclusion codes. Resolved via X1/X3 rename. |
| 2026-10-02 | Defect D-A logged | Agent | Rule E3 cites `_source_pages`; field absent from 28-column schema. |
| 2026-10-02 | Defect D-B logged | Agent | Rule E11 requires `_AUDIT/rules_log.md`; file not yet created. |
| 2026-10-02 | Scope rename applied | Human | FROZEN_SCOPE.md and v6: E1/E3 -> X1/X3 in body. |
| 2026-10-02 | Bible v3 updated | Human | Part 2: X1/X3 codes; 501 verified; label disambiguation appended. |
| 2026-10-02 | MASTER_PROMPT_5 updated | Human | Frozen anchor uses X1/X3; label disambiguation block added. |
| 2026-10-02 | v2-v5 archived | Human | Moved to 07_certificates/old_scopes/ with archive README. |
| 2026-10-02 | _AUDIT/rules_log.md created | Agent | Defect D-B closed; Rule E11 logging target now exists. |
| 2026-10-02 | Repo-wide label sweep | Agent | E1/E3 exclusion labels renamed to X1/X3 in 12 live MDs (root README, 01_data x3, 02_cards x3, 03_ai_checks x5, 07_certificates x2, PRISMA_FLOWCHART node IDs). |
| 2026-10-02 | Stale facts corrected | Agent | 02_data_proceesed README: 280->284 dups; ghost MASTER_EVIDENCE.csv + evidence_batches/ marked REMOVED; stale REC_1688 translation paths fixed in 3 files; AUDIT_PROMPT file paths corrected. |
| 2026-10-02 | Defect D-C logged | Agent | FROZEN_MANIFEST_20260927.csv SHA256 mismatches disk for 291/291 cards (content rewritten post-freeze). T1 hash verification will FAIL until re-stamp or human ruling. |
| 2026-10-02 | Defect D-C closed | Human+Agent | Old manifest retired to 07_certificates/old_manifests/; FROZEN_MANIFEST_20261002.csv in force. REC_1688 row re-stamped after X3 label edit. Verified 291/291 match, 0 mismatches. FROZEN.md manifest SHA refreshed (BB0ABB67...22F9). |


| 2026-10-02 | Manifest regenerated | Agent | Old manifest retired to 07_certificates/old_manifests/. New manifest: 02_cards/FROZEN_MANIFEST_20261002.csv. Reason: card hashes changed after author-field anonymization. Cards unchanged. |
