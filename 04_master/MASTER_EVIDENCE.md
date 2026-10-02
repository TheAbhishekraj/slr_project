# MASTER_EVIDENCE.md — Specification and Audit Record

Corpus: 287 (LOCKED)
File:   04_master/MASTER_EVIDENCE.csv
Schema: 28 columns (00_scope/EXTRACTION_SCHEMA.md)
Source: 02_cards/REC_XXXX.md
Built:  2026-10-02

---

## 1. What This File Is

The certified master evidence table for the GPS-Denied UAV SLR.
One row per included study. Every cell sourced from an extraction
card. No invented data. Every quote carries an anchor.

---

## 2. Schema — 28 Columns

### IDENTITY (7)
| # | Column | Type | Source |
|---|---|---|---|
| 1 | id | REC_XXXX | header |
| 2 | title | string | header |
| 3 | authors | string | header |
| 4 | year | int or NOT_REPORTED | header |
| 5 | venue | string | header |
| 6 | doi | string | header |
| 7 | country | string | ## 14. Country / Funding |

### CONTENT (11)
| # | Column | Source |
|---|---|---|
| 8 | problem | ## 2. Problem Statement |
| 9 | motivation | ## 3. Motivation |
| 10 | approach_summary | ## 5. Proposed Method |
| 11 | method_category | ## 5. "Category:" |
| 12 | sensors | ## 6. "Sensors:" |
| 13 | gps_denied_type | ## 4. first token |
| 14 | fusion_method | (schema field, often NOT_REPORTED) |
| 15 | algorithm | ## 5. "Method name:" |
| 16 | dataset | ## 7. "dataset:" |
| 17 | platform | ## 6. "Platform:" |
| 18 | contribution_type | ## 12. first token |

### EVIDENCE (10)
| # | Column | Source |
|---|---|---|
| 19 | real_or_sim | ## 7. "real_or_sim:" |
| 20 | baseline | ## 7. "baselines:" |
| 21 | headline_result | ## 8. prose |
| 22 | metrics | ## 8. table |
| 23 | ablation | ## 9. content |
| 24 | limitations | ## 10. content |
| 25 | future_work | ## 11. content |
| 26 | funding | ## 14. "Funding:" |
| 27 | notes | ## 15. content |
| 28 | verification_status | header |

### EXTENDED COLUMN (in MASTER_EVIDENCE_extended.csv only)
| 29 | real_or_sim_normalized | derived from column 19 |

---

## 3. Anchor Notation Accepted

Per ruling R-1 and R-1e:

| Form | Example | Where |
|---|---|---|
| Bracket | [p.4] | Section prose |
| Inline | p.4 | Inline quotes |
| Table column | p.4 (from bare `4` in page column) | Metrics table |

Every quote cell carries an anchor unless marked:
- `NOT_REPORTED` — field absent from card
- `[CARD_DEFECT_NO_ANCHOR] ...` — card-side paraphrase (see unanchored_fields_log.md)

---

## 4. Rules Applied

| Rule | Description |
|---|---|
| E1 | No fabrication — NOT_REPORTED for absent fields |
| E2 | Quote anchoring — [p.N] or p.N accepted |
| E10 | Taxonomy derived, not extracted |
| R-1 | Both anchor forms accepted |
| R-1e | Table page-column normalization |
| R-2 | real_or_sim_normalized derived column |
| R-3 | Enum fields carry only the enum token |
| R-4 | Missing sections 13–18 → NOT_REPORTED |
| R-5 | Card-side paraphrase flagged with prefix |

---

## 5. Certification

After Phase 8, this document is regenerated with:

- **Rows:** 287
- **Columns:** 28 (+ 1 extended)
- **SHA256 (master):** _(filled after build)_
- **SHA256 (extended):** _(filled after build)_
- **Manifest SHA256:** _(from FROZEN_MANIFEST_20261002.csv)_
- **Excluded IDs (absent):** REC_0053, REC_0693, REC_0866, REC_1688
- **Waived cells:** REC_1432 ablation, REC_1435 ablation
- **GB-5 fails:** 0
- **GB-6 AMBIGUOUS:** 0
- **Cards edited:** 0

Certificate file: `07_certificates/CERTIFICATE_MASTER.md`

---

## 6. Excluded Records — Never Referenced

| ID | Code | Reason |
|---|---|---|
| REC_0053 | X1 | Out of scope |
| REC_0693 | X1 | Out of scope |
| REC_0866 | X1 | Out of scope |
| REC_1688 | X3 | Chinese full text (EN translation retained) |

These IDs must not appear in any count, table, figure, or sentence.

---

## 7. Downstream Consumers

| Consumer | Uses |
|---|---|
| T4 QA scoring | Reads master, writes quality_appraisal_scored.csv |
| T5 Analytics | Reads master, writes inference_table.csv |
| T5 Figures | Reads master, generates F1–F9 |
| T6 Manuscript | Reads master + NUMBER_TRACE, writes MANUSCRIPT.md |
| T7 Submission | Certifies master SHA256 in final audit |

---

## 8. Regeneration

To rebuild from cards at any time:

```bash
python tools/build_master.py
```

This reads cards + manifest, writes MASTER_EVIDENCE.csv and
MASTER_EVIDENCE_extended.csv. It does not edit cards.

---

## 9. Audit Trail

Every build, fix, and waiver is logged in:
- `_AUDIT/action_log.md` — chronological write log
- `_AUDIT/rules_log.md` — rule decisions
- `_AUDIT/unanchored_fields_log.md` — waived cells
- `07_certificates/CERTIFICATE_MASTER.md` — final certification

---

_End of MASTER_EVIDENCE.md_
