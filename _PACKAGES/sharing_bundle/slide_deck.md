---
# Slide 1: Title
**GPS-Denied Navigation for Unmanned Aerial Vehicles:**
*A Systematic Literature Review of Multi-Sensor Fusion Approaches (2010–2026)*

**Presenter:** Abhishek Raj
**Audience:** Academic Supervisor

---
# Slide 2: The Problem
**Autonomous Navigation in GPS-Denied Environments**
- UAVs increasingly operate where Global Positioning Systems (GPS/GNSS) are degraded or actively denied.
- Single-sensor navigation methods (e.g., IMU-only or Vision-only) are brittle to environmental edge cases.
- **Solution:** Multi-sensor fusion provides necessary robustness, but the true state of the field's operational readiness is unmapped.

---
# Slide 3: The Research Gap
**What We Don't Know**
- How are fusion architectures distributed across modalities (e.g., Vision, LiDAR, IMU)?
- Are researchers testing on realistic platform kinetics or just generic models?
- Are systems being built and validated for natural degradation or *active adversarial denial*?
- We need an empirical, trace-recorded baseline to direct our lab's future research.

---
# Slide 4: Research Questions
**Guiding the Systematic Literature Review**
- **RQ1:** How are primary sensor-fusion configurations distributed, and how have they shifted?
- **RQ2:** What operational environments are predominantly targeted?
- **RQ3:** To what extent are algorithmic evaluations tied to specific UAV kinematic models?
- **RQ4:** What proportion of current research evaluates resilience under adversarial conditions?

---
# Slide 5: Methodology Overview
**Strict adherence to PRISMA 2020**
- **Protocol:** Pre-defined inclusion/exclusion criteria.
- **Data Source:** IEEE Xplore & Scopus.
- **Extraction:** 28-column schema, strictly anchored to verbatim quotes.
- **Appraisal:** 10-point methodological quality rubric.
- **Automation:** Fully script-driven extraction and PDF compilation to prevent data-drift.

---
# Slide 6: Search Strategy
**Boolean Queries & Strict Filters**
- **Groups:** (1) GPS-denial terminology, (2) UAV platforms, (3) Navigation tasks.
- **Filters:** 2010–2026 window, English language, Journal & Conference Proceedings.
- **Harvest:** Capped at 1,000 top-relevance records per database.
- **Total Initial Harvest:** 2,000 records.

---
# Slide 7: PRISMA Flow
**From Harvest to Final Corpus**
- **Identification:** 2,000 raw records.
- **Deduplication:** 1,716 unique records.
- **Screening:** 501 candidate studies.
- **Eligibility:** 291 full-texts retrieved, 4 excluded (out of scope / non-English).
- **Included:** **287 studies** in the frozen corpus.
*(See Fig. 1 in manuscript for the flow diagram)*

---
# Slide 8: Corpus Statistics
**At a Glance**
- **Total Included:** 287 peer-reviewed studies.
- **Temporal Growth:** 9 studies (2010–2015) ➔ 182 studies (2021–2026).
- **Physical Validation:** 218 studies feature real-world flight or ground-robot surrogate tests.
- **Simulation-Only:** 69 studies (24%) conclude without physical validation.

---
# Slide 9: Quality Appraisal
**10-Point Rigor Assessment**
- **Dimensions:** Experimental Rigor, Reporting Completeness, Baseline Fairness, Reproducibility.
- **Q-High (8-10 pts):** 145 studies (50.5%)
- **Q-Medium (5-7 pts):** 118 studies (41.1%)
- **Q-Low (0-4 pts):** 24 studies (8.4%)
- *Note: Simulation-only studies scoring 8-10 were capped at Q-Medium.*

---
# Slide 10: Sensor Distribution (RQ1)
**Vision Dominates the Literature**
- **VISION:** 182 studies (63.4%)
- **IMU_ONLY:** 35 studies (12.2%)
- **OTHER:** 27 studies (9.4%)
- **LIDAR:** 22 studies (7.7%)
- **UWB / RADAR:** 14 (4.9%) / 7 (2.4%)

---
# Slide 11: Algorithm Distribution
**Maturation of Estimation Architectures**
- **HYBRID:** 78 studies (27.2%)
- **VISION_OBJECT:** 55 studies (19.2%)
- **COOPERATIVE:** 41 studies (14.3%)
- **FILTERING (EKF/UKF):** 36 studies (12.5%)
- **FACTOR_GRAPH:** 29 studies (10.1%)
- *Takeaway:* Factor graphs and hybrid learning methods are actively displacing classical filtering.

---
# Slide 12: Environment Distribution (RQ2)
**Shallow Broad Testing**
- **MIXED:** 192 studies (66.9%)
- **INDOOR:** 72 studies (25.1%)
- **UNDERGROUND / GNSS_DENIED (Explicit):** 7 (2.4%) / 8 (2.8%)
- *Takeaway:* The field overwhelmingly validates in benign or mixed environments rather than dedicated, harsh edge cases.

---
# Slide 13: The Adversarial Gap (RQ4)
**Crucial Vulnerability Identified**
- **The Metric:** Only **5 of 287 studies (1.7%)** test under adversarial threat.
- **The Threats:** GNSS spoofing, electronic warfare, and long-term jamming.
- **The Reality:** 98.3% of the literature models GPS-denial as a natural degradation (e.g., flying indoors), failing to prepare for contested airspace.

---
# Slide 14: Cross-Cutting Findings
**Weak Platform Specificity (RQ3)**
- **GENERIC_UAV:** 99 studies (34.5%) model generic kinematics.
- **MULTI_ROTOR:** 134 studies (46.7%) assume multirotor dynamics.
- *Issue:* Over a third of the field ignores airframe-specific aerodynamic constraints, making their algorithms brittle for agile or fixed-wing deployment.

---
# Slide 15: Limitations
**Honest Boundaries of the Review**
- **Search Cap:** 1,000-record cap per database may have missed lower-ranked studies.
- **Single Sensor:** I6 criteria excluded single-sensor papers with potentially relevant algorithms.
- **Granular Meta-analysis:** Unsupportable due to heterogeneous metric definitions and non-normalized sensor hardware reporting.
- **Citations:** Only 5 adversarial studies are explicitly cited in the narrative body; the rest are compiled in Appendix A.

---
# Slide 16: Contributions
**What This Project Delivers**
- **Empirical Proof:** Proves that the UAV navigation field is under-prepared for adversarial environments.
- **Standardized Baseline:** Provides an explicit, quantified baseline of sensors, platforms, and algorithms over the last 15 years.
- **Methodological Blueprint:** Demonstrates a highly rigorous, script-driven review pipeline immune to manual data drift.

---
# Slide 17: Audit Trail
**Trust Through Traceability**
- **Evidence Cards:** Every study has an individual markdown card linked to exact verbatim quotes.
- **Data Freezes:** The 287-study corpus is locked (`v287-certified`).
- **Token Audits:** Python scripts verify the compiled LaTeX token count exactly matches the validated markdown source.

---
# Slide 18: Reproducibility
**Open Science Commitment**
- **Repository:** All data, scripts, cards, and certificates are tracked in GitHub.
- **Automation:** The IEEE-formatted PDF is compiled entirely via custom Python scripts, not manual LaTeX editing.
- **Tag:** `pre-latex-cleanup-complete` / `v-final-pdf`.

---
# Slide 19: Next Steps for the Lab
**Moving Forward**
1. **Adversarial Resilience:** Pivot our primary research to spoofing/jamming resilience.
2. **Coupled Kinematics:** Integrate specific aerodynamic constraints directly into state estimation.
3. **Hardware Standards:** Lead the field by establishing standardized sensor noise and calibration reporting in our upcoming papers.

---
# Slide 20: Thank You
**Questions & Discussion**

*Abhishek Raj*
*GPS-Denied Navigation SLR*
*Corpus: 287 Studies | 2010–2026*
---
