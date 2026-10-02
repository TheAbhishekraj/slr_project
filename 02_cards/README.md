# 02_cards — Extraction Evidence Cards Repository

This directory contains the standardized, per-paper markdown extraction evidence cards for the systematic literature review:  
**"GPS-Denied Navigation for UAVs: A Systematic Literature Review of Multi-Sensor Fusion Approaches (2010–2026)"**.

---

## 1. Directory Summary

- **Total Extraction Cards:** **291** (`REC_0001.md` through `REC_1715.md`).
- **Schema Compliance:** All cards strictly conform to the 18-section extraction schema defined in [`00_scope/EXTRACTION_SCHEMA.md`](file:///e:/slr_project/00_scope/EXTRACTION_SCHEMA.md).
- **Cryptographic Audit Manifest:** Every card is tracked with file byte sizes, section counts, and SHA256 hashes in [`FROZEN_MANIFEST_20260927.csv`](file:///e:/slr_project/02_cards/FROZEN_MANIFEST_20260927.csv).
- **Governance:** Governed under [`FROZEN.md`](file:///e:/slr_project/02_cards/FROZEN.md) and [`00_scope/FROZEN_SCOPE_v6.md`](file:///e:/slr_project/00_scope/FROZEN_SCOPE_v6.md).

---

- **287 Included Full-Text Studies:**
  - Formally included in the systematic review corpus (291 assessed - 4 excluded = 287 included).
  - Every included study has a corresponding extraction card in this directory and full-text PDF on disk.
  - Mapped 1-to-1 with Sl. No 1 to 291 in `PRISMA_MASTER_WORKBOOK_v2.xlsx`.
- **4 Excluded Full-Text Studies:**
  - `REC_0053`: Excluded under **Rule E1** (General non-empirical deep learning survey).
  - `REC_0693`: Excluded under **Rule E1** (Isolated ToF camera optical bench metrology).
  - `REC_0866`: Excluded under **Rule E1** (High-level conceptual search-and-rescue survey).
  - `REC_1688`: Excluded under **Rule E3** (Foreign language: Full text in Chinese; complete English translation provided in `01_data/03_pdfs/REC_1688_translated_EN.txt`).
