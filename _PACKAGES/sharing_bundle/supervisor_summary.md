# Executive Summary
**Project:** GPS-Denied Navigation for UAVs — Multi-Sensor Fusion (2010–2026)
**Target Audience:** Academic Supervisor

## 1. Problem Statement
Autonomous navigation in Global Positioning System (GPS)-denied environments is a critical capability for Unmanned Aerial Vehicles (UAVs). While single-sensor approaches often fail under varying conditions, multi-sensor fusion provides robustness. However, it remains unclear how current research is distributed across sensor modalities, platforms, and validation environments, and whether this distribution adequately addresses the operational demands of actively contested or degraded conditions.

## 2. Research Questions
This systematic literature review addresses four primary research questions:
- **RQ1:** How are primary sensor-fusion configurations distributed across the literature, and how has this distribution shifted over time?
- **RQ2:** What operational environments (e.g., indoor, underground, mixed) are predominantly targeted by current fusion architectures?
- **RQ3:** To what extent are algorithmic evaluations tied to specific UAV kinematic models (e.g., multirotor, fixed-wing) versus generic platform assumptions?
- **RQ4:** What proportion of current research evaluates navigation resilience under adversarial or actively contested conditions (e.g., spoofing, jamming)?

## 3. Method in Brief
The review strictly adheres to the PRISMA 2020 protocol. A Boolean search across IEEE Xplore and Scopus yielded a raw corpus of 2,000 records. After deduplication (to 1,716), screening (to 501), and full-text eligibility review, a final frozen corpus of 287 peer-reviewed English-language studies was established. Data was extracted using a 28-column schema, and studies were assessed using a 10-point methodological quality rubric. The entire pipeline is script-driven, token-audited, and traceable.

## 4. Corpus Statistics

| Metric | Value |
|---|---|
| Review Protocol | PRISMA 2020 |
| Date Range | 2010 – 2026 |
| Total Harvested Records | 2,000 |
| Unique Records Screened | 1,716 |
| Final Included Studies | 287 |
| High-Quality (Q-High) Studies | 145 (50.5%) |
| Pure Simulation Studies | 69 (24.0%) |

## 5. Key Findings
- **Shallow Environmental Testing:** A substantial majority of research tests broadly but shallowly, with MIXED environments accounting for 192/287 studies (66.9%), while dedicated challenging edge cases (like underground or explicit GNSS-denied) remain sparse.
- **Weak Platform Specificity:** Airframe-specific kinetic modeling is often ignored; GENERIC_UAV platforms account for 99/287 studies (34.5%), meaning roughly a third of the literature does not model specific flight dynamics.
- **Vision Dominance:** Camera-based systems heavily dominate the literature, serving as the primary sensor family in 182/287 studies (63.4%).
- **Significant Adversarial Gap:** The field is acutely under-prepared for actively contested environments. Only 5 of 287 studies (1.7%) evaluate systems under deliberate adversarial threat (e.g., GNSS spoofing, electronic warfare).
- **Validation Reality Gap:** Pure simulation remains heavily utilized, accounting for 69 of 287 studies, meaning nearly a quarter of the field concludes without physical flight validation.

## 6. Limitations
- **Search Scope:** The search was restricted to two databases (IEEE Xplore and Scopus) with a 1,000-record harvest cap per database, potentially omitting relevant lower-ranked studies.
- **Language Bias:** Only English-language publications were included, potentially underrepresenting contributions from non-English-speaking research communities.
- **Fusion Requirement:** The strict requirement for multi-sensor fusion (Criteria I6) excludes single-sensor navigation studies that may contain highly relevant algorithmic contributions.
- **Non-normalized Extraction:** Because sensor descriptions were extracted verbatim rather than normalized into a hardware inventory, fine-grained quantitative meta-analysis of specific sensor combinations is unsupportable.
- **In-text Citations:** Following narrative review conventions and PRISMA allowances, only 5 studies (the adversarial subset) are explicitly cited in the manuscript text, with the remaining 282 listed in Appendix A.

## 7. Contributions
- **Empirical Baseline:** Establishes a fully auditable, trace-recorded empirical baseline of multi-sensor UAV navigation research from 2010–2026 across 287 studies.
- **Identification of Strategic Gaps:** Highlights the critical absence of adversarial threat modeling and platform-specific aerodynamic integration in current navigation architectures.
- **Reproducible Framework:** Delivers a 100% reproducible, script-audited repository structure that prevents manual data-drift during manuscript compilation.

## 8. Next Steps
- **Target Adversarial Resilience:** Pivot primary lab research toward defining robustness against deliberate interference (spoofing/jamming) rather than just natural degradation.
- **Integrate Kinematics:** Develop state estimation architectures that strictly couple sensor fusion with platform-specific aerodynamic and kinetic models.
- **Standardize Hardware Reporting:** Adopt and advocate for explicit sensor inventories, noise, and calibration parameter reporting to ensure cross-study comparability and physical flight reproducibility.
