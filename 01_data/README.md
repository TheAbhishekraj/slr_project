# 01_data — Systematic Literature Review Data Assets

This directory organizes all primary search and full-text data assets for:  
**"GPS-Denied Navigation for UAVs: A Systematic Literature Review of Multi-Sensor Fusion Approaches (2010–2026)"**.

---

## Directory Structure

- [`01_data_raw/`](file:///e:/slr_project/01_data/01_data_raw/) — Initial database export files (IEEE Xplore & Scopus, 2,000 total raw records).
- [`02_data_proceesed/`](file:///e:/slr_project/01_data/02_data_proceesed/) — Deduplication audit logs (`01_deduplicated_master.csv`), preliminary screening (`02_screened_included_v2.csv`), PRISMA full-text screening results (`03_screening_results.csv`), retrieved PDF manifest (`04_retrieved_pdfs_291.csv`), and master Excel review workbook (`PRISMA_MASTER_WORKBOOK_v2.xlsx`).
- [`03_pdfs/`](file:///e:/slr_project/01_data/03_pdfs/) — 291 full-text research paper PDFs (`REC_0001.pdf` to `REC_1715.pdf`). Canonical Bible Part 3 location; strictly PDF binaries. Status: FROZEN.

---

## Corpus Correspondence & PRISMA 2020 Flow

- **2,000 Harvested Records:** 1,000 IEEE Xplore + 1,000 Scopus.
- **1,716 Unique Records:** After automated deduplication (284 duplicates removed).
- **501 Screened Records:** Title and abstract candidate pool.
- **291 Full-Text Retrieved & Assessed:** 100% of candidate PDFs retrieved and preserved on disk.
- **287 Included Studies:** Exactly 287 studies formally included in the review corpus (291 assessed - 4 excluded = 287 included).
- **4 Excluded Studies:**
  - 3 Scope Exclusions (Rule E1: `REC_0053`, `REC_0693`, `REC_0866`).
  - 1 Foreign Language Exclusion (Rule E3: `REC_1688`, Chinese full-text; translation preserved in `01_data/02_data_proceesed/REC_1688_translated_EN.txt`).
- **291 Extraction Cards:** Exactly corresponds to the 291 markdown extraction cards in [`02_cards/`](file:///e:/slr_project/02_cards/).
- **Sl. No Parity:** Sl. No 1 to 291 in `PRISMA_MASTER_WORKBOOK_v2.xlsx` matches 1-to-1 with `pdf_file_name` on disk.
