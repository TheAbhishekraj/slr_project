# DEDUP_REPORT.md — Deduplication Report
# GPS_Denied_SLR | Phase 3 | PRISMA 2020

---

## Summary

| Metric | Value |
|--------|-------|
| Total input records | 2,000 |
| IEEE Xplore records | 1,000 |
| Scopus records | 1,000 |
| Duplicates removed | 284 |
| Removal rate | **14.2%** |
| Unique records retained | **1,716** |

---

## Deduplication Method (Verbatim)

**Step A — DOI Normalization:**  
All DOI values are converted to lowercase. The prefixes `https://doi.org/`, `http://doi.org/`, and `doi:` are stripped. Empty DOI fields are treated as missing (not matched by DOI).

**Step B — Exact DOI Match:**  
If two records share the same normalized DOI, the second occurrence is flagged as a duplicate with reason `DOI match`. Tie-break rule: keep the IEEE Xplore record; if both are from the same source, keep the record with the older publication year; if equal, keep the one with the lexicographically smaller DOI.

**Step C — Fuzzy Title Match:**  
For records without a DOI match, titles are normalized (lowercase, Unicode NFKD normalization, all punctuation replaced by spaces, consecutive whitespace collapsed). Levenshtein similarity ratio is computed as `1 - edit_distance / max(len(t1), len(t2))`. If the ratio ≥ 0.90, the record is flagged as a duplicate with reason `Title match`. The same tie-break rule applies.

**Step D — Tie-Break Priority:**  
1. Prefer IEEE Xplore source over Scopus  
2. Prefer older publication year  
3. Prefer lexicographically smaller DOI string  

---

## Output Files

| File | Rows | Description |
|------|------|-------------|
| `01_data/02_data_proceesed/deduplicated_master.csv` | 1,716 | Unique records, canonical 8-column schema |
| `01_data/02_data_proceesed/dedup_log.csv` | 284 | One row per removed duplicate; reasons: `DOI match` or `Title match` |

---

## Reproducibility

This deduplication process can be reproduced by running:
```
python tools/deduplicate_data.py
```

Input files: `01_data/01_data_raw/ieee_xplore_20260615.csv`, `01_data/01_data_raw/scopus_20260615.csv`  
No manual curation was applied; all removal decisions are logged in `dedup_log.csv`.