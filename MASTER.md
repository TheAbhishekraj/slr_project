# SLR Project — Master Overview

> **Title:** GPS-Denied Navigation for Unmanned Aerial Vehicles: A Systematic Literature Review of Multi-Sensor Fusion Approaches (2010–2026)  
> **Author:** Abhishek Raj  
> **Protocol:** PRISMA 2020  
> **Corpus:** 287 included studies, frozen 2026-10-02  
> **Tag:** v287-certified, pre-latex-cleanup-complete

---

## 1. Project Objective

This repository contains the complete, audit-traced research pipeline for a Systematic Literature Review (SLR) investigating GPS-denied navigation for UAVs using multi-sensor fusion. The review covers 287 peer-reviewed studies published between 2010 and 2026, synthesized under the PRISMA 2020 framework. The work answers four research questions spanning sensor modalities, localization accuracy, algorithmic architectures, and adversarial resilience.

---

## 2. Key Statistics

| Metric | Value |
|---|---|
| Raw harvested records | 2,000 (1,000 IEEE Xplore + 1,000 Scopus) |
| Duplicates removed | 284 |
| Unique records screened | 1,716 |
| Title/abstract pass | 501 |
| Full-text retrieved | 291 |
| Excluded at full-text | 4 (REC_0053, REC_0693, REC_0866, REC_1688) |
| **Final frozen corpus** | **287** |
| Quality: Q-High (8–10) | 145 (50.5%) |
| Quality: Q-Medium (5–7) | 118 (41.1%) |
| Quality: Q-Low (0–4) | 24 (8.4%) |
| Evidence cards completed | 287 / 287 |
| Verification status | 287 / 287 VERIFIED |
| Corpus freeze date | 2026-10-02 |

### Research Questions

1. **RQ1 (Sensors & Trends):** Which primary sensor family dominates, and how has prevalence shifted between 2010 and 2026?
2. **RQ2 (Accuracy & Environments):** What localization accuracy and robustness metrics are reported across GPS-denied environments?
3. **RQ3 (Algorithms & Validation):** Which algorithmic approaches dominate, and how do they compare on validation type?
4. **RQ4 (Limitations & Adversarial):** What limitations exist, particularly regarding adversarial conditions and electronic warfare?

---

## 3. Repository Structure — Complete Directory Map

### `00_scope/` — Protocol and Operational Boundaries

Defines the project's scope, inclusion/exclusion criteria, extraction schema, and locked numbers. This is the project's constitutional document.

| File | Purpose |
|---|---|
| `SCOPE.md` | Full project scope: 4 RQs, PICO frame, I1–I7 / E1–E10 criteria, QA rubric, extraction schema |
| `FROZEN_SCOPE.md` | Immutable snapshot of scope locked before extraction began |
| `LOCKED_NUMBERS.md` | Canonical locked figures (PRISMA flow, sensor counts, QA tiers) — the single source of truth for every numeral in the manuscript |
| `EXTRACTION_SCHEMA.md` | 28-column extraction schema definition |
| `EXTRACTION_RULES.md` | Rules governing how fields are populated (verbatim quotes, NOT_REPORTED policy) |
| `PRISMA_FLOWCHART.md` | Textual PRISMA 2020 flow: 2000 → 1716 → 501 → 291 → 287 |
| `MASTER_PROMPT.md` | Master AI extraction prompt used for automated evidence card generation |
| `MASTER_REFERENCE_BIBLE.md` | Cross-reference bible linking all scope decisions to rationale |
| `AUDIT_PROMPT.md` | Prompt template for running audit passes on extracted data |
| `END_GOAL.md` | Project end-state definition and acceptance criteria |
| `PHASE_C_MANUAL_EXTRACTION.md` | Instructions for manual extraction fallback cases |
| `action_log.md` | Timestamped log of scope changes |
| `README.md` | Directory overview |

### `01_data/` — Raw and Processed Data

Contains the original search exports from IEEE Xplore and Scopus, plus any intermediate screening files. These are untouched archival records.

### `02_cards/` — Evidence Cards (287 files)

One Markdown file per included study (e.g., `REC_0010.md`, `REC_1208.md`). Each card contains YAML frontmatter (id, title, authors, year, venue, DOI, extraction date, verification status) and structured extraction fields with verbatim quotes from the source PDF.

- **Total cards:** 287
- **Format:** Markdown with YAML frontmatter
- **Verification:** All 287 cards carry `verification_status: VERIFIED`

### `03_ai_checks/` — AI Screening Logs

Automated screening and verification logs generated during the AI-assisted extraction process. Used for auditability to demonstrate that AI tools were supervised and outputs were human-verified.

### `04_master/` — Master Evidence Database

The single source of truth for all quantitative analysis.

| File | Purpose |
|---|---|
| `MASTER_EVIDENCE.csv` | Primary 287-row × 28-column evidence database (687 KB) |
| `MASTER_EVIDENCE_extended.csv` | Extended version with additional computed fields |
| `MASTER_EVIDENCE_original.csv` | Pre-cleanup backup of the original CSV |
| `MASTER_EVIDENCE.md` | Human-readable summary of the CSV schema and key statistics |
| `action_log.md` | Change log for the master database |
| `README.md` | Directory overview |

### `05_analysis/` — Analysis Scripts, Figures, and QA

Contains all Python scripts that generate figures, compute quality scores, and produce the analytical outputs cited in the manuscript.

| File | Purpose |
|---|---|
| `make_figures.py` | Generates all 9 figures (F1–F9) at 300/600 DPI from MASTER_EVIDENCE.csv |
| `analyze.py` | Core analysis: sensor counts, environment distribution, method categories, temporal buckets |
| `score_quality.py` | Computes 10-point QA scores and assigns Q-High/Q-Medium/Q-Low tiers |
| `quality_appraisal_scored.csv` | Full QA scoring output for all 287 studies |
| `inference_table.csv` | Inference table linking RQs to evidence |
| `taxonomy_distribution.csv` | Method category taxonomy counts |
| `KAPPA_CALIBRATION_README.md` | Documents the status of inter-rater reliability calibration (not verifiable in audit logs) |
| `figures/` | Output directory containing F1–F9 PNG files |
| `action_log.md` | Change log |
| `README.md` | Directory overview |

### `06_manuscript/` — Manuscript Source and Compiled Output

The full manuscript pipeline: Markdown source → LaTeX → PDF.

| Path | Purpose |
|---|---|
| `MANUSCRIPT.md` | Root-level copy of the manuscript Markdown (synced with source/) |
| `references.bib` | BibTeX file containing all 287 references (99 KB) |
| `source/MANUSCRIPT.md` | Canonical Markdown source for the manuscript |
| `source/SUBMISSION_CHECKLIST.md` | Pre-submission checklist with figure hashes |
| `source/MANUSCRIPT.md.bak` | Backup of the pre-cleanup manuscript |
| `ieee/main.tex` | Auto-generated LaTeX file (built by venue_format.py) |
| `ieee/main.pdf` | Compiled IEEE-format PDF (the deliverable) |
| `ieee/manuscript_ieee.tex` | Alternative LaTeX build |
| `ieee/references_ieee.bib` | IEEE-formatted reference copy |
| `ieee/FIGURES/` | Copies of all figures used by LaTeX |
| `presentation/` | Slide decks and supervisor summaries |
| `action_log.md` | Change log |
| `README.md` | Directory overview |

### `07_certificates/` — Verification and Integrity Certificates

Cryptographic and procedural verification records proving corpus integrity.

| File | Purpose |
|---|---|
| `CERTIFICATE_MASTER.md` | Master certificate confirming 287/287 verified |
| `CERTIFICATE_ANALYTICS.md` | Analytics verification: confirms figure/table numbers match LOCKED_NUMBERS.md |
| `CERTIFICATE_QA.md` | QA scoring certificate: tier distributions verified |
| `CERTIFICATE_QA_SCORING.md` | QA scoring methodology certificate |
| `CENSUS_AUDIT_REPORT_20261002.md` | Full census audit dated 2026-10-02 |
| `PHASE_D_VERIFICATION_REPORT_20261002.md` | Phase D verification report |
| `action_log.md` | Change log |
| `README.md` | Directory overview |
| `old_manifests/` | Archived previous manifest versions |
| `old_scopes/` | Archived previous scope versions |

### `_AUDIT/` — Governance Logs

Ongoing governance and compliance tracking.

| File | Purpose |
|---|---|
| `action_log.md` | Master audit action log (11 KB) |
| `rules_log.md` | Rules compliance log (12 KB) |
| `unanchored_fields_log.md` | Log of extraction fields lacking verbatim anchors |
| `README.md` | Directory overview |

### `_BIBLE/` — Project Bible and Standards

Core project guidelines and formatting standards.

| File | Purpose |
|---|---|
| `MASTER_PROJECT_BIBLE.md` | The project bible: all conventions, naming rules, and workflow standards |
| `FORMATTING_STANDARDS.md` | Formatting rules for Markdown, LaTeX, and CSV outputs |
| `REFERENCE_APPENDIX.md` | Appendix of reference formatting rules |
| `README.md` | Directory overview |

### `_INSTRUCTIONS/` — Agent and Human Prompts

Prompt templates organized by workflow phase.

| Subdirectory | Purpose |
|---|---|
| `audit/` | Audit-phase prompts |
| `general/` | General-purpose prompts |
| `latex/` | LaTeX formatting and compilation prompts |
| `presentation/` | Presentation and summary generation prompts |

### `_PACKAGES/` — Distributable Bundles

Ready-to-share packages for different audiences.

| Subdirectory | Purpose |
|---|---|
| `submission/` | IEEE submission package: `manuscript_ieee.pdf`, `manuscript_ieee.tex`, `references_ieee.bib`, `SUPERVISOR_SUMMARY.md`, `README.md` |
| `sharing_bundle/` | External review package: PDF, Q&A document, evidence index, slide deck, supervisor summary, formatting standards, Appendix A (all 287 studies) |
| `supervisor/` | Supervisor-facing summary package |

### `_REVIEW/` — Manuscript Review Reports

Post-processing review pipeline with phase-by-phase compliance reports.

| File | Purpose |
|---|---|
| `MANUSCRIPT_PROPOSED.md` | The proposed (reviewed) version of the manuscript |
| `MANUSCRIPT_PROPOSED_CHANGELOG.md` | Changelog documenting all changes from original to proposed |
| `REVIEW_REPORT.md` | Summary review report |
| `phase0_report.md` | Phase 0: Initial compliance scan |
| `phase1_report.md` | Phase 1: Deep content verification |
| `phase2_report.md` | Phase 2: Number tracing audit |
| `phase3_report.md` | Phase 3: Tone and banned-word scan |
| `phase4_report.md` | Phase 4: Figure and table verification |
| `phase5_report.md` | Phase 5: Final formatting check |

### Root Files

| File | Purpose |
|---|---|
| `MASTER.md` | This file — comprehensive project overview |
| `README.md` | GitHub-facing repository description |
| `AGENTS.md` | AI agent operating rules (read-only disk, no internet, banned words, content freeze) |
| `CLAUDE.md` | Stylistic rules and behavioral constraints for AI assistants |
| `AI_REVIEW_PROMPT.md` | Template prompt for external AI peer review of the manuscript |
| `_COMPLETE_PROMPT.md` | Full project context prompt for fresh AI sessions |
| `_FRESH_SESSION_PROMPT.md` | Shortened context prompt for new sessions |
| `PENDING_CLEANUP.txt` | List of pending cleanup tasks |

### `tools/` — Build and Automation

| Path | Purpose |
|---|---|
| `venue_format.py` | Entry point for the Markdown → LaTeX → PDF build pipeline |
| `venue_format/` | Core build module: `cli.py` (CLI), `latex_emit.py` (LaTeX generation), `floats.py` (figure/table handling), `read_manuscript.py` (Markdown parser), `card.py` (venue card), `sha_util.py` (hash verification) |
| `formats/IEEE.conf` | IEEE venue configuration (IEEEtran, 2-column, 10pt Times) |
| `formats/slr_profile.generic.conf` | Generic SLR profile mapping manuscript and bib paths |

---

## 4. Build Instructions

To compile the IEEE-formatted PDF from the Markdown source:

```powershell
cd E:\slr_project
python tools\venue_format.py `
  --repo . `
  --format tools\formats\IEEE.conf `
  --profile tools\formats\slr_profile.generic.conf `
  --strict --confirm
```

This will:
1. Parse `06_manuscript/MANUSCRIPT.md` and `06_manuscript/references.bib`
2. Generate `06_manuscript/ieee/main.tex` with proper IEEE formatting
3. Copy figures to `06_manuscript/ieee/FIGURES/`
4. Run `pdflatex` + `bibtex` + `pdflatex` × 2 to produce `main.pdf`
5. Verify SHA256 checksums and content drift tolerance

**Prerequisites:** Python 3.8+, MiKTeX (pdflatex), IEEEtran.cls

---

## 5. Quality Appraisal Summary

| Dimension | Max Points | What It Measures |
|---|---|---|
| A: Experimental Rigor | 4 | Real-world flight (+2), ground-truth comparison (+1), repeatability (+1) |
| B: Reporting Completeness | 3 | Trajectory error (+1), environment parameters (+1), robustness (+1) |
| C: Baseline Fairness | 2 | Benchmark comparison (+1), matched conditions (+1) |
| D: Reproducibility | 1 | Public code/data/hardware specs (+1) |

**Tier thresholds:** Q-High (8–10), Q-Medium (5–7), Q-Low (0–4)  
**Simulation cap:** Simulation-only studies scoring 8–10 are capped at Q-Medium.

---

## 6. PRISMA 2020 Flow

```
Identification:    2,000 records (1,000 IEEE + 1,000 Scopus)
                      ↓ −284 duplicates
Screening:         1,716 unique records
                      ↓ −1,215 excluded (title/abstract)
Eligibility:         501 candidates → 291 full-text retrieved
                      ↓ −4 excluded (3 out-of-scope, 1 non-English)
Included:            287 studies (frozen corpus)
```

---

## 7. Excluded Study IDs (Do Not Modify)

| ID | Reason |
|---|---|
| REC_0053 | Out of scope (X1) |
| REC_0693 | Out of scope (X1) |
| REC_0866 | Out of scope (X1) |
| REC_1688 | Non-English full text (X3) |

---

## 8. Governance Rules

1. **Read-only disk.** Never access internet or memory within AI sessions.
2. **No modifications** to source files without explicit CONFIRM.
3. **Never touch** excluded IDs: REC_0053, REC_0693, REC_0866, REC_1688.
4. **Write only** inside the active output tree.
5. **One task per turn.** Stop after each. Wait for CONFIRM.
6. **Every number** must cite file + line.
7. **Quotes** must be character-exact.
8. **Two sources conflict** → STOP and report.
9. **Missing info** = NOT_REPORTED.
10. **American spelling. Plain words.**

### Banned Words (Manuscript Only)

delve, landscape (metaphor), crucial, pivotal, state-of-the-art (unless named baseline follows), very, really, It is important to note, It should be noted, In conclusion

### Banned Paragraph Openers

Moreover, Furthermore, Additionally

---

## 9. Current Status (October 2026)

| Component | Status |
|---|---|
| Corpus extraction (287/287) | ✅ COMPLETE |
| Evidence card verification | ✅ VERIFIED (287/287) |
| Quality appraisal scoring | ✅ COMPLETE |
| MASTER_EVIDENCE.csv | ✅ FROZEN |
| Figures F1–F9 | ✅ GENERATED |
| Manuscript draft | ✅ COMPLETE |
| IEEE LaTeX compilation | ✅ CLEAN BUILD |
| Figure caption formatting | ✅ FIXED (no duplicate labels) |
| References (287 entries) | ✅ ALL INCLUDED (via \nocite{*}) |
| Ampersand escaping in .bib | ✅ FIXED |
| PRISMA checklist | ✅ ADDRESSED |
| Data integrity | ✅ VALIDATED |
| Submission package | ✅ READY |
| Sharing bundle | ✅ READY |
| Kappa calibration | ⚠️ NOT VERIFIABLE (disclosed in Limitations §6) |

---

## 10. Key Findings (Summary)

1. **Vision dominance:** 182/287 studies (63.4%) use camera-based primary sensors.
2. **Accelerating field:** Corpus grew from 9 studies (2010–2015) to 182 (2021–2026).
3. **Mixed environments:** 192/287 (66.9%) test in composite settings.
4. **Generic platforms:** 99/287 (34.5%) use generic UAV platforms without airframe-specific modeling.
5. **Adversarial gap:** Only 5/287 (1.7%) address contested conditions.
6. **Validation mix:** 123 REAL, 88 BOTH, 69 SIM, 7 NOT_REPORTED.

---

## 11. Contact

- **Repository:** https://github.com/TheAbhishekraj/slr_project
- **Author:** Abhishek Raj
