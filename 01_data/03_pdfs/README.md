# 03_pdfs — Full-Text PDF & Extracted Text Corpus

This directory holds the **291 full-text research paper PDFs** and extracted text assets collected for the systematic literature review:  
**"GPS-Denied Navigation for UAVs: A Systematic Literature Review of Multi-Sensor Fusion Approaches (2010–2026)"**.

---

## 1. Corpus Summary

* **Total PDF Files:** **291** (`REC_0001.pdf` to `REC_1715.pdf`)
* **Total PDF Directory Size:** **1,613,079,524 bytes (~1.50 GB)**
* **Naming Convention:** `REC_XXXX.pdf` matching the canonical Paper ID.
* **Corpus Correspondence:**
  * **287 Included Studies:** Formally included in the systematic review corpus (291 assessed - 4 excluded = 287 included).
  * **4 Excluded Studies:**
    * 3 Domain / Scope Exclusions (E1: `REC_0053`, `REC_0693`, `REC_0866`).
    * 1 Foreign Language Exclusion (E3: `REC_1688`, Chinese full-text; complete translation provided in `REC_1688_translated_EN.txt`).
  * **1-to-1 Serial Number Parity:** Sl. No 1 to 291 in `PRISMA_MASTER_WORKBOOK_v2.xlsx` matches 1-to-1 with every physical `REC_XXXX.pdf` file in this directory.
  * Exactly matches the 291 extraction markdown files in [`02_cards/`](file:///e:/slr_project/02_cards/).

---

## 2. Text Assets & Translation

* **Raw Text Extractions (`.txt`):** Text extracted via PyMuPDF for automated ingestion and semantic validation (e.g., `REC_1582.txt`, `REC_1688.txt`, `REC_1715.txt`).
* **English Translation (`REC_1688_translated_EN.txt`):** Complete section-by-section translation of the Chinese full text of `REC_1688` (Tianjin University) to support auditability.

---

## 3. Governance Note
Per `.gitignore`, individual `.pdf` binaries are excluded from Git version control to prevent repository bloat, while this repository manifest tracks their status. All 291 PDFs and text extracts are permanently preserved on local disk.
