# Submission Checklist

## 1. Venue

IEEE Access (default; confirm before submission). The _FRESH_SESSION_PROMPT.md notes "Target venue (ask human: T-RO or Access)." SCOPE.md does not lock a venue. At 6,059 words with 5 tables, 9 figures, and 287 references, the manuscript falls within the typical IEEE Access systematic review length (5,000-10,000 words). If IEEE Transactions on Robotics (T-RO) is selected instead, the manuscript may require condensation to meet T-RO's stricter page limits.

## 2. Manuscript Statistics

| Metric | Value |
|---|---|
| Total words | 6,059 |
| Abstract | 191 words |
| 1. Introduction | 691 words |
| 2. Related Work (incl. misplaced §4.5 synthesis block) | 783 words |
| 3. Methods | 973 words |
| 4. Results | 1,496 words |
| 5. Discussion | 884 words |
| 6. Limitations | 519 words |
| 7. Conclusion | 422 words |
| Main-text tables | 5 (Tables I-V) |
| Figures | 9 (Fig. 1-9) |
| References | 287 |

## 3. Figures

| ID | Filename | Caption | DPI | SHA256 |
|---|---|---|---|---|
| F1 | F1_PRISMA_flow.png | PRISMA 2020 flow diagram showing the identification, screening, eligibility, and inclusion stages of the systematic review (frozen corpus: 287 studies) | 600 | C25FCB47D80B17F60B48D221B0A12EBFEF9F77A66156F8132FA1421D2DAF0A12 |
| F2 | F2_Method_Category.png | Method category distribution across the corpus | 300 | B802E97CD730B7030A05B8DA1CE3220146DBDA735D9197DF369EF599A9651F7A |
| F3 | F3_Sensor_Distribution.png | Primary sensor family distribution across the 287-study corpus | 300 | 7C2D6B13878C3E0A32349D7345251EC2D72737ECAE67DD701466B37407DE5915 |
| F4 | F4_Real_vs_Sim.png | Distribution of validation methods (real vs. simulation) across the corpus | 300 | 0C14488AAE5671407792C7A6CE6D079833348329D9EAFA17A1E5DF81119137EC |
| F5 | F5_Year_Trajectory.png | Publication year trajectory across 2010-2026 | 600 | 5FFCB8AFA0A18027B657A337BB3E211439809FA655CE666C3D05C0C11AB001D9 |
| F6 | F6_Geography.png | Geographic distribution of study origins | 300 | CFA207F0453610D216FD53B080A5CE526D62D36E21A71FDA322065C2870D9EC6 |
| F7 | F7_Quality_Tier.png | Methodological quality tier distribution across the 287-study corpus | 300 | 0C60471325D83152919A6A280FCBFC4BEDA015D3314E80003A61D1863BD67A61 |
| F8 | F8_Fusion_Method.png | Algorithmic fusion method distribution | 300 | 2FA5B20A4F9389F780F0D047829627AA2AC57C5001DEB3A16B87749D5222A292 |
| F9 | F9_Headline_Accuracy.png | Headline accuracy reporting distribution across the corpus | 300 | 663DA9CD74EECDC7CA6E65148C016E9063D6D20AC21376EA8550041F432DAD4B |

## 4. Tables

| ID | Caption | Location in manuscript |
|---|---|---|
| Table I | Primary sensor family distribution | Section 4.1 (L94) |
| Table II | Temporal distribution by year bucket | Section 4.1 (L111) |
| Table III | Environment distribution | Section 4.2 (L134) |
| Table IV | Platform distribution | Section 4.2 (L150) |
| Table V | Method category distribution | Section 4.3 (L184) |
| Table S1 | Included-study summary (287 rows) | Supplementary material (not in main text) |

## 5. Supplementary Files

- **Table S1** (287-row included-study table with columns: REC ID, First author, Year, Primary sensor, Method category, Environment, Platform, Validation type, QA tier, QA total): Generated in the agent artifact directory. **STATUS: NOT YET IN PROJECT TREE. Human must save to `06_manuscript/Table_S1.md` or convert to CSV/Excel before submission.**
- **PRISMA 2020 checklist**: **STATUS: NOT_PROVIDED.** Human must complete from the official PRISMA 2020 template (http://www.prisma-statement.org/). See Section 10 below for a draft mapping.

## 6. Author Contributions (CRediT)

HUMAN-PROVIDED. Fill author names for each role.

| CRediT Role | Author(s) |
|---|---|
| Conceptualization | [AUTHOR_NAMES] |
| Methodology | [AUTHOR_NAMES] |
| Software | [AUTHOR_NAMES] |
| Validation | [AUTHOR_NAMES] |
| Formal analysis | [AUTHOR_NAMES] |
| Investigation | [AUTHOR_NAMES] |
| Resources | [AUTHOR_NAMES] |
| Data curation | [AUTHOR_NAMES] |
| Writing — original draft | [AUTHOR_NAMES] |
| Writing — review & editing | [AUTHOR_NAMES] |
| Visualization | [AUTHOR_NAMES] |
| Supervision | [AUTHOR_NAMES] |
| Project administration | [AUTHOR_NAMES] |
| Funding acquisition | [AUTHOR_NAMES] |

## 7. Conflict of Interest

HUMAN-PROVIDED.

"The authors declare no conflict of interest. [CONFIRM OR AMEND]"

## 8. Funding

HUMAN-PROVIDED.

"[FUNDING_SOURCE_OR_NONE]"

## 9. Data Availability

The corpus, extraction records, quality appraisal, inference table, and trace documents are available in the project repository. Raw PDFs are not redistributed due to publisher copyright; study metadata and traceability records are provided in MASTER_EVIDENCE.csv and NUMBER_TRACE.md.

## 10. PRISMA 2020 Checklist Mapping

| PRISMA Item | # | Addressed in |
|---|---|---|
| Title | 1 | Title (H1 heading) |
| Abstract — structured summary | 2 | Abstract |
| Rationale | 3 | Section 1 (Introduction) |
| Objectives | 4 | Section 1 (Introduction, RQ1-RQ4) |
| Eligibility criteria | 5 | Section 3.4 (Inclusion and exclusion criteria) |
| Information sources | 6 | Section 3.2 (Information sources and search strategy) |
| Search strategy | 7 | Section 3.2 (Information sources and search strategy) |
| Selection process | 8 | Section 3.3 (Screening and selection) |
| Data collection process | 9 | Section 3.5 (Data extraction) |
| Data items | 10 | Section 3.5 (Data extraction) |
| Study risk of bias assessment | 11 | Section 3.6 (Quality appraisal) |
| Effect measures | 12 | NOT_ADDRESSED (narrative synthesis; no effect-size pooling) |
| Synthesis methods | 13 | Section 3.5 (Data extraction, synthesis method statement) |
| Reporting bias assessment | 14 | Section 6 (Limitations) |
| Certainty assessment | 15 | NOT_ADDRESSED (no GRADE or equivalent applied) |
| Study selection — results | 16a | Section 3.3 (PRISMA flow, Fig. 1) |
| Study characteristics | 17 | Section 4.1 (Tables I-II) |
| Risk of bias in studies | 18 | Section 4.4 (Fig. 7) |
| Results of individual studies | 19 | NOT_ADDRESSED (aggregate synthesis only) |
| Results of syntheses | 20 | Sections 4.1-4.5 |
| Reporting biases | 21 | Section 6 (Limitations) |
| Certainty of evidence | 22 | NOT_ADDRESSED (no GRADE) |
| Discussion — summary | 23a | Section 5 (Discussion) |
| Discussion — limitations | 23b | Section 6 (Limitations) |
| Discussion — interpretation | 23c | Section 5 (Discussion) |
| Other information — registration | 24 | Section 3.1 (Protocol and registration) |
| Other information — protocol | 25 | Section 3.1 (Protocol and registration) |
| Other information — funding | 26 | Section 8 (Funding, human-provided) |
| Other information — competing interests | 27 | Section 7 (Conflict of Interest, human-provided) |

## 11. SHA256 of Frozen Artifacts

| Artifact | SHA256 |
|---|---|
| MANUSCRIPT.md | 204CFEA266BCDE8D96BB8081974754401F0506D6AB36495BCB49FAC40BC1ACC6 |
| NUMBER_TRACE.md | B0D7D767F612B3C455F8CB5A5381E80743E98B373B0317E95ECAB1E80E63813D |
| references.bib | CAACA8A5142360EF4E17AA5AA7F18691828FCE4E595289D7411383AF34FF041B |

## 12. Human-Only Items Remaining

- Author names, order, affiliations, emails, and ORCIDs
- Corresponding author designation
- Funding statement (Section 8)
- Conflict of interest statement (Section 7)
- CRediT author contribution roles (Section 6)
- Venue confirmation: IEEE Access vs. T-RO (Section 1)
- Keywords (5-8 terms for IEEE submission)
- Save Table S1 from agent artifact directory to project tree
- Complete PRISMA 2020 checklist from official template
- Overleaf project setup with IEEEtran.cls conversion
- Final human proofread of all sections
- Figure DPI verification and upscaling if required (minimum 300 DPI for IEEE)
- ScholarOne or Editorial Manager submission
