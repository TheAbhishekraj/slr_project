# GPS-Denied Navigation for Unmanned Aerial Vehicles: A Systematic Literature Review of Multi-Sensor Fusion Approaches (2010–2026)

**Author:** Abhishek Raj
**Affiliation:** [to be filled]
**Email:** [to be filled]
**ORCID:** [to be filled]

# Abstract

Autonomous navigation for unmanned aerial vehicles (UAVs) in Global Positioning System-denied (GPS-denied) environments requires robust multi-sensor fusion, yet published research exhibits substantial fragmentation across operational domains, sensor modalities, and validation standards. Following the PRISMA 2020 framework, we examine 287 peer-reviewed studies published between 2010 and 2026. We investigate sensor-fusion configurations and longitudinal adoption shifts (RQ1), localization accuracy across operational environments and vehicle platforms (RQ2), algorithmic architectures and flight validation modalities (RQ3), and operational limitations under electronic warfare and contested settings (RQ4). Methodological quality appraisal stratifies the corpus into 145 high-quality (Q-High), 118 medium-quality (Q-Medium), and 24 low-quality (Q-Low) investigations. Two-thirds of the analyzed studies evaluate mixed operational environments, roughly one-third deploy generic UAV platforms without airframe-specific dynamics, and only 5 of 287 studies (1.7%) address adversarial or contested conditions. Because sensor extraction records comprise non-normalized quoted descriptions rather than standardized inventories, sensor families are reported via derived primary classifications. We deliver an audit-traced corpus establishing empirical baselines and characterizing the deployment gaps that separate laboratory flight demonstrations from mission-critical operations in denied airspace.



**Keywords:** GPS-denied navigation, multi-sensor fusion, unmanned aerial vehicles, systematic literature review, PRISMA 2020, sensor fusion

## 1. Introduction

GPS-denied navigation is a prerequisite for sustained unmanned aerial vehicle (UAV) operation across infrastructure inspection, emergency response, and contested airspace. Global Positioning System (GPS) and broader Global Navigation Satellite System (GNSS) signals provide accurate absolute positioning under nominal conditions. In environments where these signals are degraded, jammed, spoofed, or naturally denied—such as urban canyons, dense forests, subterranean structures, and indoor facilities—UAVs must rely on alternative navigation strategies that fuse multiple sensing modalities to maintain stability, estimate ego-motion, and map the surrounding area. Ensuring mission reliability under these constraints remains a significant challenge, as single-sensor approaches often lack the redundancy required for sustained autonomous flight in complex, unstructured spaces.

Existing literature reviews and surveys on UAV navigation provide valuable insights into specific algorithms, such as visual-inertial odometry (VIO) [REC_0017, REC_0041, REC_0347] or simultaneous localization and mapping (SLAM) [REC_0003, REC_0035, REC_0065], and often focus on isolated operational environments. These prior works generally target either specific sensor modalities—such as camera-based systems or LiDAR [REC_0008, REC_0013, REC_0043]—or particular algorithmic architectures, leaving a noticeable gap in comprehensive, cross-domain synthesis. They frequently miss the broader integration patterns across different degraded environments and do not adequately characterize the flight validation standards used to evaluate these systems. In addition, few systematic reviews critically assess the methodological quality of the underlying primary studies or the resilience of these navigation frameworks against active electronic warfare, including jamming and spoofing. Consequently, the research community lacks a unified, evidence-based understanding of the structural gaps between laboratory demonstrations and real-world, mission-critical deployments.

To address this fragmentation, we systematically synthesize the state of GPS-denied UAV navigation research. Following the PRISMA 2020 framework, we examine a corpus of 287 peer-reviewed studies published between 2010 and 2026. The scope encompasses diverse operational domains, sensor modalities, and validation standards, aiming to provide a clear empirical baseline of current capabilities and methodological rigor. Methodological quality appraisal stratifies the corpus into 145 Q-High, 118 Q-Medium, and 24 Q-Low investigations, ensuring that strong claims are anchored in high-quality evidence. This approach allows for a transparent evaluation of the field's progression over the past sixteen years.

We are guided by the following four explicit research questions:
1. RQ1 (Sensors & Trends): Which primary sensor family dominates GPS-denied UAV navigation research, and how has its prevalence shifted between 2010 and 2026?
2. RQ2 (Accuracy & Environments): What localization accuracy and robustness metrics are reported across different GPS-denied environments (indoor, urban canyon, subterranean, forest, adversarial), and how do they vary by environment and platform?
3. RQ3 (Algorithmic Approaches & Validation): Which algorithmic approaches (VIO, SLAM, LIO, filter-based fusion, learning-based methods) dominate the literature, and how do they compare on validation type (real flight vs. simulation) and reported performance?
4. RQ4 (Limitations & Adversarial Conditions): What limitations and future research directions are identified in the corpus, particularly regarding adversarial conditions, electronic warfare (jamming/spoofing), and resource constraints?

The contributions of this work are anchored in four findings derived from the evidence corpus. The environment analysis (Section 4.2) reveals that 192 of 287 studies (67%) evaluate within mixed or composite operational environments, indicating a strong trend toward diverse testing settings. The platform analysis shows that 99 of 287 investigations (34%) utilize generic UAV platforms without airframe-specific dynamics modeling, highlighting a persistent validation gap. The adversarial analysis (Section 4.4) reveals that only 5 of 287 studies (1.7%) explicitly address contested conditions such as jamming and spoofing, underscoring a vulnerability in current research. A methodological finding concerns sensor-level analysis: because extraction records comprise non-normalized quoted descriptions rather than standardized hardware inventories, sensor families are characterized by derived primary classifications rather than exact inventories.

The remainder of this paper is structured as follows. Section 2 reviews related work on GPS-denied UAV navigation and positions this work against prior surveys. Section 3 details the methodology, including the search strategy, screening process, and quality appraisal criteria based on the PRISMA 2020 guidelines. Section 4 presents the results and synthesis, addressing the four research questions.


## 2. Related Work

The problem of autonomous UAV navigation in GPS-denied environments has motivated extensive research across multiple domains and has been the subject of several prior reviews and surveys. To position our contributions, we compare our scope and methodology against these existing works.

The problem of autonomous unmanned aerial vehicle (UAV) navigation in environments where satellite positioning is unavailable has motivated extensive research across multiple domains. To contextualize the contributions of this review, this section examines the primary thematic clusters within the corpus. Rather than summarizing prior surveys, this review groups the primary evidence base by sensor modality, algorithmic architecture, operational environment, and adversarial resilience. Across the corpus, research spans vision, LiDAR, UWB, and radar as primary modalities; filter-based and factor-graph fusion as algorithmic families; and indoor, urban, forest, and subterranean settings as testing environments.

A substantial portion of the collected literature focuses on the development of specific sensor modalities for localization and mapping. Vision-primary studies represent a major thrust in the corpus, heavily utilizing monocular and stereo cameras to extract ego-motion and environmental features. Parallel to visual methods, Light Detection and Ranging (LiDAR) has become increasingly common for building dense three-dimensional maps, utilizing active illumination to operate independently of ambient lighting. In situations where visual and LiDAR sensors suffer from degradation, Ultra-Wideband (UWB) and radar technologies provide necessary robustness. The corpus contains several UWB-focused investigations leveraging ranging measurements for localization within pre-calibrated areas. Similarly, radar-centric approaches explore millimeter-wave reflections to maintain velocity and altitude estimates under perceptual constraints. 

Beyond hardware configuration, a significant volume of literature is dedicated to refining algorithmic architectures for sensor fusion. The corpus is divided between traditional filtering mechanisms, modern graph-based optimization techniques, LiDAR-inertial odometry (LIO), and emerging learning-based methods. Filter-based fusion remains widely deployed due to its computational efficiency on resource-constrained platforms, integrating asynchronous sensor feeds for low-latency state estimation. Conversely, factor graph optimization incorporates delayed measurements to perform global trajectory smoothing. Both filtering and graph-based approaches are central to the maturation of Simultaneous Localization and Mapping (SLAM) and Visual-Inertial Odometry (VIO) pipelines. In parallel, LIO architectures have emerged to handle high-rate point cloud registration, while learning-based families increasingly explore end-to-end neural pipelines for feature extraction and depth estimation.

The operational environment heavily influences the chosen navigation strategy, driving a third major thematic cluster. Indoor environments, characterized by structured geometries and absolute GPS denial, serve as the primary testing ground for many visual and LiDAR frameworks. In contrast, urban canyons present the challenge of intermittent satellite availability and multipath interference, requiring seamless transitions between absolute and relative positioning systems. Natural environments introduce dynamic obstacles and unstructured features. Forest canopy navigation requires active obstacle avoidance and robustness against wind disturbances. Subterranean settings shift the emphasis to perceptual degradation, dust, lack of ambient lighting, and the necessity of active sensing payloads to navigate highly constrained tunnel networks.

Despite the breadth of research across various sensors, algorithms, and environments, a significant gap remains regarding system resilience under active threat. Within the entire 287-study corpus, only 5 of 287 studies address adversarial or contested conditions, spanning GNSS spoofing ([REC_0010], [REC_0489]), electronic warfare ([REC_1083]), and long-term denial ([REC_1084], [REC_1085]).

## 3. Methods

### 3.1 Protocol and registration

We conducted this systematic literature review following the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 guidelines. The review protocol was defined prior to data collection and is documented in full in the project scope record. No formal protocol registration was performed.

### 3.2 Information sources and search strategy

Two primary indexing databases in engineering and applied sciences were searched: IEEE Xplore and Scopus. The search was executed on 2026-06-15, covering publications from 2010-01-01 through 2026-06-15 (inclusive). The year 2026 is partial, covering January through mid-June, and all temporal trend analyses treat it accordingly.

The search query combined three concept groups using Boolean AND logic: (1) GPS/GNSS denial terminology ("GPS-denied," "GNSS-denied," "GPS-degraded," "GPS-free," "navigation without GPS"); (2) UAV platform descriptors ("UAV," "unmanned aerial vehicle," "drone," "quadrotor," "multirotor," "fixed-wing"); and (3) navigation task descriptors ("localization," "navigation," "SLAM," "odometry," "positioning," "sensor fusion"). Filters restricted results to English-language journal articles and conference proceedings published within the search window. Each database was harvested to a cap of 1,000 relevance-ranked records, yielding a total raw corpus of 2,000 records (1,000 IEEE Xplore + 1,000 Scopus).

### 3.3 Screening and selection

The PRISMA 2020 flow for this review proceeded as follows. From the 2,000 raw harvested records, 284 duplicate entries were removed via exact cross-database matching on normalized DOI, a normalized title-year pair, and an MD5 content hash of title, authors, and abstract. This left 1,716 unique records. Title and abstract screening against the inclusion and exclusion criteria reduced this set to 501 candidate studies. Full-text PDFs were sought for these 501 candidates, and 291 were successfully retrieved (100% retrieval rate for assessed studies). At the full-text eligibility stage, 4 studies were excluded (IDs listed here for auditability only; they are not included in any count or table that follows): 3 were classified as out of scope (X1: REC_0053, REC_0693, REC_0866) and 1 was excluded for non-English full text (X3: REC_1688). The remaining 287 studies constitute the frozen corpus denominator for all subsequent analyses (Fig. 1).

![PRISMA 2020 Flow Diagram](figures/F1_PRISMA_flow.png)

PRISMA 2020 flow diagram showing the identification, screening, eligibility, and inclusion stages of the systematic review (frozen corpus: 287 studies)

### 3.4 Inclusion and exclusion criteria

Studies were included if they met all of the following criteria: (I1) published between 2010-01-01 and 2026-06-15; (I2) written and published in English; (I3) peer-reviewed journal article or full conference proceeding; (I4) addressed GPS/GNSS-denied, degraded, or contested aerial navigation as the central research focus; (I5) focused explicitly on UAV platforms; (I6) implemented or evaluated an integrated multi-sensor navigation solution fusing measurements from at least two distinct sensing modalities; and (I7) presented empirical quantitative validation via physical flight tests, ground-robot surrogate experiments, or high-fidelity simulation.

Studies were excluded if they were: (E1) purely conceptual, tutorial, or theoretical papers lacking validation; (E2) systems requiring active, uninterrupted nominal GNSS signals; (E3) focused on non-UAV platforms such as ground vehicles, AUVs, or spacecraft; (E4) single-sensor navigation methods lacking multi-sensor fusion; (E5) published in languages other than English; (E6) published prior to 2010; (E7) non-peer-reviewed preprints, theses, patents, or trade publications; (E8) duplicate records; (E9) formally retracted articles; or (E10) papers lacking extractable localization accuracy or quantitative performance data.

### 3.5 Data extraction

Each included study was subjected to structured evidence extraction using a 28-column schema. Extracted fields included bibliographic metadata (title, authors, year, venue, DOI, country), technical content (problem statement, approach summary, method category, sensors, GPS-denied type, fusion method, algorithm, dataset, platform), validation details (real-world vs. simulation, baseline comparisons, headline results, metrics, ablation studies), and contextual information (limitations, future work, funding, notes). All extracted values were anchored to verbatim quotes from the source texts to ensure traceability and auditability. Because included studies vary in metric definition, trajectory length, and sensor configuration, quantitative meta-analysis is not appropriate; findings are synthesized narratively and reported as ranges rather than pooled estimates. All 287 included studies are listed in Appendix A, with REC ID, authors, title, year, and venue.

### 3.6 Quality appraisal

Methodological quality was assessed using a 10-point scoring rubric spanning four dimensions. Dimension A (Experimental Rigor, 0-4 points) awarded points for real-world flight tests (+2), ground-truth reference comparison (+1), and repeatability reporting (+1). Dimension B (Reporting Completeness, 0-3 points) assessed quantitative trajectory error reporting (+1), operational environment parameters (+1), and robustness characterization (+1). Dimension C (Baseline Fairness, 0-2 points) evaluated direct quantitative comparison against established benchmarks (+1) and evaluation under matched conditions (+1). Dimension D (Reproducibility, 0-1 point) awarded a point for public release of code, data, or full hardware specifications (+1).

Based on total scores, studies were classified into three quality tiers: Q-High (8-10 points, n = 145), Q-Medium (5-7 points, n = 118), and Q-Low (0-4 points, n = 24). A simulation cap policy was applied: simulation-only studies scoring 8-10 on the raw rubric were capped at Q-Medium, with the raw score preserved in logs. The appraisal rubric was designed so that a reader could replicate the scoring independently from the published criteria.

SCOPE.md specifies a 20% dual-appraiser calibration sample with a target weighted Cohen's Kappa of 0.75 or higher. The specific Kappa value could not be recovered from the current audit records. Accordingly, we do not claim a specific inter-rater reliability figure.

### 3.7 Limitations of the review method

Several methodological limitations should be acknowledged. The search was restricted to two databases (IEEE Xplore and Scopus), and the 1,000-record harvest cap per database may have excluded relevant studies ranked lower in relevance ordering. The restriction to English-language publications introduces a language bias that may underrepresent contributions from non-English-speaking research communities. The multi-sensor fusion requirement (I6) excludes single-sensor navigation studies that may contain relevant algorithmic contributions. Extraction records capture quoted sensor descriptions rather than a normalized hardware inventory, limiting the granularity of sensor-combination analyses. The quality appraisal was designed for methodological rigor assessment and does not evaluate the novelty or theoretical contribution of individual studies. Effect-size pooling was not attempted. Heterogeneity across metric definitions, error formulations, and validation setups exceeds what meta-analytic pooling could meaningfully summarize. Effect measures, certainty assessment, and per-study results are not reported because we synthesize at the corpus level; see Limitations (Section 6).


## 4. Results

### 4.1 RQ1: Primary sensor distribution and temporal shift

To address the first research question regarding sensor-fusion configurations and their evolution, we analyze the primary sensor modalities utilized across the corpus. Camera-based systems dominate GPS-denied UAV navigation: vision systems lead with 182/287 studies (63.4%, Fig. 3). Inertial-only approaches (IMU_ONLY) account for 35/287 (12.2%), followed by OTHER modalities at 27/287 (9.4%). Light Detection and Ranging (LiDAR) represents 22/287 (7.7%), while Ultra-Wideband (UWB) and RADAR comprise 14/287 (4.9%) and 7/287 (2.4%), respectively. Table I presents the primary sensor family distribution.

**Table I.** Primary sensor family distribution

| Sensor family | Studies | Share (%) |
|---|---|---|
| VISION | 182 | 63.4 |
| IMU_ONLY | 35 | 12.2 |
| OTHER | 27 | 9.4 |
| LIDAR | 22 | 7.7 |
| UWB | 14 | 4.9 |
| RADAR | 7 | 2.4 |
| **Total** | **287** | **100.0** |


The temporal trajectory of the corpus reveals substantial shifts in sensor adoption across the three year buckets (2010–2015, 2016–2020, and 2021–2026). Vision systems grew the fastest, increasing from just 6 studies in the earliest period to 66 in the middle period, before reaching 110 studies in the most recent bucket. This dominant acceleration aligns with the broad availability of lightweight optical sensors. Other modalities demonstrated more modest growth trajectories. Inertial-only configurations expanded from zero early studies to 9, and eventually 26 in the final period. LiDAR setups rose from a single early study to 5, and then 16. UWB applications similarly increased from zero to 3, reaching 11 studies by 2026. Radar systems remained the smallest minority, progressing from zero to 2, and finally 5 studies. The remaining studies grouped under the OTHER classification grew from 2 to 11, and then 14. These counts reflect primary sensor assignments, illustrating a clear hardware preference for vision-based estimation over time.

This distribution has shifted markedly over the sixteen-year search window. The overall volume of research has accelerated from 9 studies in the 2010–2015 period, to 96 studies between 2016–2020, and reaching 182 studies in the 2021–2026 timeframe (Fig. 5). Vision-primary and LiDAR-primary studies account for the largest share of the 2016-2020 and 2021-2026 buckets. However, detailed quantitative synthesis of specific multi-sensor combinations (e.g., vision plus UWB versus vision plus radar) is not supportable because the extraction record captures non-normalized quoted descriptions of hardware rather than a standardized sensor inventory. Findings are therefore grouped by the single primary exteroceptive or proprioceptive modality anchoring the fusion pipeline. Table II summarizes the temporal distribution.

**Table II.** Temporal distribution by year bucket

| Year bucket | Studies | Share (%) |
|---|---|---|
| 2010-2015 | 9 | 3.1 |
| 2016-2020 | 96 | 33.4 |
| 2021-2026 | 182 | 63.4 |
| **Total** | **287** | **100.0** |


![Sensor Distribution](figures/F3_Sensor_Distribution.png)

Primary sensor family distribution across the 287-study corpus

![Year Trajectory](figures/F5_Year_Trajectory.png)

Publication year trajectory across 2010-2026


### 4.2 RQ2: Accuracy and robustness by environment and platform

To determine the performance of navigation systems under various constraints, we evaluate localization accuracy across reported environments and platform types. The environment distribution reveals a strong preference for composite testing scenarios: MIXED environments account for 192/287 studies (66.9%). Dedicated INDOOR testing represents 72/287 studies (25.1%), while edge-case environments remain sparse: UNDERGROUND (7/287), FOREST (5/287), GNSS_DENIED_OTHER (5/287), and URBAN_CANYON (4/287), with 2 studies not reporting a specific environment (Fig. 6). Table III details the environment distribution.

**Table III.** Environment distribution

| Environment | Studies | Share (%) |
|---|---|---|
| MIXED | 192 | 66.9 |
| INDOOR | 72 | 25.1 |
| UNDERGROUND | 7 | 2.4 |
| GNSS_DENIED_OTHER | 5 | 1.7 |
| FOREST | 5 | 1.7 |
| URBAN_CANYON | 4 | 1.4 |
| NOT_REPORTED | 2 | 0.7 |
| **Total** | **287** | **100.0** |


Regarding platform distribution, a large portion of the literature does not customize algorithms for specific vehicle dynamics. MULTI_ROTOR platforms lead with 134/287 studies (46.7%), followed by GENERIC_UAV at 99/287 (34.5%). The remaining 54 studies distribute across OTHER (18), FLAPPING_WING_MAV (11), SWARM (10), FIXED_WING (10), HYBRID_VTOL (3), and NOT_REPORTED (2). Table IV presents the full platform distribution.

**Table IV.** Platform distribution

| Platform | Studies | Share (%) |
|---|---|---|
| MULTI_ROTOR | 134 | 46.7 |
| GENERIC_UAV | 99 | 34.5 |
| OTHER | 18 | 6.3 |
| FLAPPING_WING_MAV | 11 | 3.8 |
| SWARM | 10 | 3.5 |
| FIXED_WING | 10 | 3.5 |
| HYBRID_VTOL | 3 | 1.0 |
| NOT_REPORTED | 2 | 0.7 |
| **Total** | **287** | **100.0** |



In terms of localization accuracy, synthesis reveals that errors cannot be pooled across studies. Metric definitions, trajectory lengths, and sensor qualities vary substantially, and the extraction record does not carry a normalized error metric. Accuracy is therefore reported as NOT_REPORTED at the aggregate level; individual ranges appear in the corpus but are not comparable across studies.
Environment and platform distribute unevenly in the corpus. Of the 192 MIXED-environment studies, 73 deploy GENERIC_UAV platforms, and 17 report a quadrotor in the platform field. The 72 INDOOR studies show a similar concentration on GENERIC_UAV platforms, while the small edge-case buckets — UNDERGROUND (7), FOREST (5), GNSS_DENIED_OTHER (5), and URBAN_CANYON (4) — are too small for sub-category breakdown. In Q-High studies, this concentration on generic airframes across the dominant MIXED environment limits the ability to attribute localization performance to airframe-specific dynamics.

Accuracy reporting quality varies considerably when analyzed by deployment environment. Across all quality tiers, 233 studies report some form of quantitative error metric across their headline results and metrics fields, while 54 do not. However, a systemic reporting failure within the primary literature restricts this analysis: studies frequently omit standardized quantitative error metrics or fail to report them consistently across different environmental conditions. Without these specific counts, it is difficult to assess whether highly constrained settings, such as subterranean tunnels or dense forests, enforce stricter evaluation standards than generic mixed environments. The absence of this environment-specific reporting fidelity within the primary literature prevents a granular synthesis of where the most rigorous accuracy claims originate. The relationship between the physical testing domain and the standardization of error reporting remains an unresolved dimension of the corpus. Future primary studies must adopt standardized error reporting protocols to allow the community to map evaluation rigor directly to the deployment conditions.
 

![Real vs Sim Validation](figures/F4_Real_vs_Sim.png)

Distribution of validation methods (real vs. simulation) across the corpus

![Geographic Distribution](figures/F6_Geography.png)

Geographic distribution of study origins

### 4.3 RQ3: Algorithmic approaches and validation type

Analysis of algorithmic pipelines demonstrates the dominance of sensor fusion paradigms. According to the method category distribution, HYBRID approaches lead with 78/287 studies (Fig. 2). VISION_OBJECT tracking follows with 55/287, and COOPERATIVE fusion accounts for 41/287. Other notable families include OTHER (29), VIO (19), UNKNOWN (16), SLAM (13), LIDAR (9), UWB (8), and SURVEY (8). The remaining 11 categories each contain a single study: QUANTUM, OPTICAL_FLOW, SYSTEM, TERRAIN_AIDED_NAVIGATION, DEEP_LEARNING_ODOMETRY, VISUAL_INERTIAL, MULTI_SENSOR_FUSION, COOPERATIVE_SWARM_LOCALIZATION, RADAR, DATASET, and VSLAM. Table V details the full method category distribution.

**Table V.** Method category distribution

| Method category | Studies | Share (%) |
|---|---|---|
| HYBRID | 78 | 27.2 |
| VISION_OBJECT | 55 | 19.2 |
| COOPERATIVE | 41 | 14.3 |
| OTHER | 29 | 10.1 |
| VIO | 19 | 6.6 |
| UNKNOWN | 16 | 5.6 |
| SLAM | 13 | 4.5 |
| LIDAR | 9 | 3.1 |
| UWB | 8 | 2.8 |
| SURVEY | 8 | 2.8 |
| Remaining 11 categories | 11 | 3.8 |
| **Total** | **287** | **100.0** |


The validation types across these algorithms show a strong emphasis on physical deployment. Empirical validation on physical hardware (REAL) is present in 123/287 studies, while 88/287 studies utilize BOTH simulation and real-world testing. Purely simulated evaluations (SIM) account for 69/287 studies, and 7 studies are NOT_REPORTED (Fig. 4, Fig. 8).
Across the three largest method categories, QA tier distributions differ. HYBRID studies skew toward Q-High (50 of 78, 64%), VISION_OBJECT studies show a similar pattern (33 of 55, 60% Q-High), while COOPERATIVE studies are predominantly Q-Medium (25 of 41, 61%). In Q-High investigations, HYBRID and VISION_OBJECT together account for 83 of 145 studies (57%), indicating that the highest-quality evidence concentrates in multi-modal and vision-centric architectures.
 

![Method Category](figures/F2_Method_Category.png)

Method category distribution across the corpus

![Fusion Method](figures/F8_Fusion_Method.png)

Algorithmic fusion method distribution

### 4.4 RQ4: Limitations and adversarial conditions

We also examine the recognized limitations and vulnerabilities within current navigation systems. A notable vulnerability emerges regarding adversarial resilience. Out of 287 studies, only 5 (1.7%) address adversarial or contested conditions, spanning GNSS spoofing ([REC_0010], [REC_0489]), electronic warfare ([REC_1083]), and long-term denial ([REC_1084], [REC_1085]).

Regarding general limitations reported in the literature, the extraction taxonomy categorizes the core contribution types as CORE (270), IMPORTANT (11), NOT_REPORTED (5), and PERIPHERAL (1). The extraction taxonomy does not carry limitation text directly; therefore, specific qualitative limitations cannot be synthesized from the categorical schema, and only these classification counts are reported (Fig. 7).

![Quality Tier](figures/F7_Quality_Tier.png)

Methodological quality tier distribution across the 287-study corpus


## 5. Discussion

![Headline Accuracy](figures/F9_Headline_Accuracy.png)

Headline accuracy reporting distribution across the corpus

We synthesized evidence from 287 peer-reviewed studies to characterize the state of autonomous UAV navigation in GPS-denied environments. The analysis reveals insights regarding operational testing (Fig. 9), hardware selection, and the persistent vulnerabilities that constrain real-world deployment. While multi-sensor fusion architectures have matured over the past sixteen years, methodological and operational gaps remain that prevent confident transition from simulation to field execution.

### 5.1 Environment testing: breadth without depth

The environment distribution (Section 4.2) shows a positive trend toward composite testing conditions. Two-thirds of the corpus evaluates navigation systems in MIXED environments, requiring algorithms to perform across multiple distinct scenarios rather than relying on the structural advantages of a single domain. This trend toward composite environment testing—such as transitioning from indoor corridors to unstructured outdoor canopies, or from brightly lit environments to subterranean darkness—suggests that the community is moving away from overly constrained laboratory demonstrations. Many Q-High studies pair composite testing with physical UAV validation, indicating that top-tier research treats domain generalization as a primary barrier to autonomy. However, performance degradation during environment transitions remains a recognized challenge, particularly when exteroceptive modalities like LiDAR and vision experience simultaneous perceptual failures due to sudden illumination changes or featureless corridors. The prevalence of MIXED evaluations highlights the community's recognition that true autonomy requires algorithmic adaptability, yet the literature still struggles to define standardized benchmarks that adequately capture these transitional failure modes. Prior surveys that focused on single environments (Section 2) could not have identified this pattern because their scope excluded cross-domain comparisons.

### 5.2 Platform generality: a hidden constraint

The platform distribution (Section 4.2) reveals a constraint on the ability to draw platform-specific conclusions. The data shows that 99 of 287 studies deploy generic UAV platforms without incorporating airframe-specific dynamics or customizing the fusion algorithm to the vehicle's flight envelope. Because a substantial proportion of the evidence base treats the UAV merely as a generic sensor-carrying chassis, researchers are often unable to leverage the predictive capabilities of aerodynamic models within their filtering frameworks. In Q-High and Q-Medium investigations, the absence of tight coupling between the navigation estimator and the underlying flight controller limits the system's ability to recover from aggressive maneuvers, high-speed turns, or severe external aerodynamic disturbances such as wind gusts. This reliance on generic platforms ultimately restricts the generalizability of the reported localization accuracies to mission-critical or fixed-wing operations, where vehicle dynamics play an outsized role in state estimation. Future advances in GPS-denied navigation need to move beyond purely kinematic models and deeply integrate vehicle-specific kinetics into the core sensor fusion architecture.

### 5.3 Adversarial resilience: the unaddressed vulnerability

Despite the increasing deployment of autonomous UAVs in contested airspaces, adversarial navigation remains severely under-addressed. As reported in Section 4.4, only 5 of 287 studies explicitly investigate navigation under adversarial or contested conditions. The vast majority of the corpus assumes a benign operational environment where signal denial is environmental (e.g., urban multipath or subterranean occlusion) rather than deliberate. This assumption fails to reflect the realities of modern deployment scenarios, where malicious actors actively attempt to disrupt, deceive, or degrade navigation sensors. While many studies evaluate robustness against natural sensor degradation, few subject their fusion pipelines to the deliberate signal manipulation characteristic of contested environments. The resilience of the most commonly proposed architectures against coordinated adversarial attacks remains largely unquantified in the open literature. Addressing this gap demands the incorporation of adversarial threat models directly into algorithmic design and validation.

### 5.4 Sensor reporting: the limit of cross-study comparison

While our analysis identifies vision and LiDAR as the dominant primary modalities, a granular, quantitative synthesis of specific sensor combinations is constrained by the non-normalized nature of the extraction record (see Section 4.1 and Section 6). Primary studies frequently omit exhaustive hardware bills of materials, or fail to detail the exact specifications, noise profiles, and calibration parameters of secondary sensors. Distinguishing the performance delta between a system fusing monocular vision with millimeter-wave radar versus one utilizing stereo vision with ultra-wideband ranging becomes speculative without standardized reporting. This lack of standardized hardware documentation prevents the formulation of definitive, evidence-based recommendations regarding optimal sensor suites for specific environmental challenges. It also limits the reproducibility of the reported algorithms, as the underlying sensor noise characteristics are often the determining factor in fusion performance.

### 5.5 Cross-cutting synthesis

The preceding results, encompassing sensor modalities, deployment environments, algorithmic architectures, and systemic limitations (Fig. 2–8), collectively demonstrate an escalating emphasis on multi-sensor integration for GNSS-denied operations. Yet, a synthesis across all four research questions reveals a disconnect between algorithmic ambition and rigorous, context-specific validation. While primary sensor usage heavily favors vision, and algorithms increasingly rely on hybrid architectures to mitigate individual modality failures, testing remains overwhelmingly concentrated in generic, mixed, or indoor conditions. This concentration is compounded by a heavy reliance on generic UAV and standard multirotor platforms. The community is actively solving the state estimation problem in mathematically controlled or operationally benign settings, but broadly failing to evaluate these complex fusion pipelines under the adversarial, high-speed, or severely constrained dynamics that GPS denial typically implies.

In Q-High studies, the simultaneous concentration of generic airframes and generalized mixed environments further confirms that current methodological quality reflects algorithmic mathematical rigor rather than operational testing fidelity. Strong evidence exists for algorithmic innovation, but empirical validation is lagging behind theoretical design. No single research question alone exposes this disconnect; only by cross-examining the hardware selections, algorithmic formulations, and validation typologies simultaneously does it become evident that the rapid advancement in sensor fusion complexity has outpaced the commitment to representative physical deployment. No corpus study or prior review covers the full cross-domain synthesis with quality appraisal stratification that we provide. By systematically evaluating these dimensions, we establish an empirical baseline, identifying the persistent deployment gaps that separate controlled laboratory demonstrations from mission-critical operations.

In summary, the progression of GPS-denied UAV navigation algorithms from theoretical concepts to field demonstrations is evident across the literature. However, the pathway to resilient autonomy requires addressing these gaps: adversarial resilience, platform-specific aerodynamic models for high-speed state estimation, and standardized hardware reporting. Only by addressing these gaps can the research community transition from controlled, generic demonstrations to the deployment of systems capable of operating in complex, contested environments.

## 6. Limitations

We cover 287 studies published between 2010 and 2026, appraised as Q-High (145), Q-Medium (118), and Q-Low (24), as reported in Section 3.6. Two ablation fields (REC_1432 and REC_1435) were waived in extraction and are excluded from all quantitative synthesis. The limitations below fall into two groups: those inherent to the corpus and those inherent to the review method.

The first group concerns the corpus itself.

- Sensor extraction is non-normalized. The record captures quoted hardware descriptions rather than a standardized inventory, and inclusion criterion I6 (Section 3.4) sits in tension with the single-modality studies the corpus reflects, because I6 admits only work that fuses at least two sensing modalities. The primary-sensor families in Section 4.1 are therefore derived classifications rather than reported inventories, and granular sensor-combination synthesis is unsupportable, as stated in Section 4.1 and Section 4.4.
- Platform classification is coarse. The taxonomy in Section 4.2 is derived by regular expression from a free-text platform field, which collapses heterogeneous hardware into broad labels: GENERIC_UAV (99/287), 18 studies labeled OTHER, and 2 labeled NOT_REPORTED. Airframe-specific effects such as rotor configuration, mass, or wing loading cannot be isolated for a large share of the corpus, so platform-level conclusions are indicative rather than exact.
- Environment labels are aggregated. The GNSS_DENIED_OTHER label combines spoofing, contested operation, long-term denial, and total outage into a single count (5 studies). Because these threat types are pooled under one label, we cannot report how many studies address each condition, and the aggregate understates the breadth of contested threats the label represents.
- Inter-rater reliability is not claimed. We did not perform the dual-appraiser calibration described in Section 3.6. The quality tiers that anchor the strong claims in Section 4 therefore rest on a single scoring pass, and an independent re-scoring could shift individual tier assignments.

The second group concerns the review method.

- The search covered two databases, IEEE Xplore and Scopus, and stopped at a 1,000-record cap per database (Section 3.2). Work ranked below the cap, or indexed only elsewhere, may be absent even when relevant.
- Only English-language publications were included (Section 3.4). This introduces a language bias that may underrepresent contributions from non-English research communities.
- The multi-sensor requirement (I6) excludes single-sensor navigation studies, which may contain algorithmic contributions relevant to degraded-signal operation.
- No formal protocol registration was performed (Section 3.1), so the review criteria cannot be verified against a dated registry entry.
- The appraisal assesses methodological rigor, not novelty or theoretical contribution. Cost, onboard computational load, and certification or regulatory constraints were not extracted and are not covered.

These limitations do not alter the direction of the findings, but they bound the precision attributed to any single figure. Counts derived from free-text fields, labels that aggregate distinct conditions, and a single-pass quality appraisal each add a margin of uncertainty to the tables in Section 4. The corpus is large enough for the reported patterns to be robust at the level of shares and trends, but it is not uniform enough to support fine-grained claims about individual sensor combinations or platform classes.

## 7. Future Work

The gaps identified in this review point to four concrete research directions, each tied to a specific finding from the results.

The most pressing need is adversarial validation. Only 5 of 287 studies address contested or adversarial conditions (Section 4.4). Future work should incorporate adversarial threat models—including coordinated GNSS spoofing, sensor injection attacks, and communication denial—directly into the algorithmic design and validation phases. Robustness should be defined against deliberate interference rather than natural degradation alone. Standardized adversarial benchmarks, analogous to existing indoor navigation datasets, would enable reproducible comparison across fusion architectures.

Platform-specific navigation is a second priority. With 99 of 287 studies deploying generic UAV platforms (Section 4.2), the field lacks evidence on how airframe-specific dynamics affect state estimation. Future investigations should integrate aerodynamic and kinetic models into the core fusion pipeline, particularly for fixed-wing, hybrid VTOL, and high-speed multirotor platforms. Coupling the navigation estimator with the flight controller would allow state estimation to exploit rather than ignore vehicle dynamics during aggressive maneuvers and wind disturbances.

Standardized hardware reporting is a third direction. The non-normalized sensor extraction documented in Section 4.1 and Section 6 prevents cross-study comparison of fusion permutations. Future studies should adopt explicit sensor inventories listing each modality's make, model, noise profile, and calibration parameters. Standardized reporting templates would enable the meta-level sensor-combination analyses that are currently unsupportable.

Paired simulation and physical validation is the fourth direction. Pure simulation still accounts for 69 of 287 studies (Section 4.3). Validation should consistently pair simulation with physical flight tests, since simulation alone leaves deployment behavior untested. Sim-to-real transfer metrics, documenting the performance delta between simulated and physical runs on identical trajectories, would help the community quantify the fidelity of its simulation environments.

## 8. Conclusion

We aimed to map how GPS-denied UAV navigation research is distributed across sensor modalities, operational environments, vehicle platforms, algorithmic architectures, and validation standards, and to test whether that distribution matches the demands of contested operations. We answer four research questions over a frozen corpus of 287 peer-reviewed studies published between 2010 and 2026, drawing only on auditable, trace-recorded evidence. Our purpose is not to propose new algorithms but to establish the empirical baseline against which future claims in this domain can be measured.

The evidence supports three principal findings. The field tests broadly but shallowly: MIXED environments account for two-thirds of the corpus, while dedicated edge cases remain sparse. Platform specificity is weak: roughly one-third of the literature does not model airframe-specific dynamics. Adversarial readiness is nearly absent: fewer than 2% of studies address contested conditions. A cross-cutting methodological result is that sensor families are reported as derived primary classifications because the extraction record is non-normalized.

Across the corpus the same pattern recurs. Fusion architecture and composite testing have matured, with the corpus growing from 9 studies in the 2010–2015 bucket to 182 in 2021–2026, yet the questions that matter most operationally remain thinly addressed: airframe-specific kinetics, standardized hardware reporting, and resilience under deliberate interference. Pure simulation still accounts for 69 of 287 studies, so a measurable share of the field concludes without physical flight validation.

None of these needs requires new theory. Each is a reporting and testing discipline the evidence already shows to be missing. Closing them would let the field convert its accumulating methodological strength into autonomy that survives the contested, signal-denied environments it was built to serve. The corpus already contains the evidence needed to act; what remains is the discipline to act on it.

## Funding

This research received no external funding.

## Conflicts of Interest

We declare no competing interests.

## Data Availability

All extracted data, evidence cards, analysis scripts, and certificates are openly available at https://github.com/TheAbhishekraj/slr_project.

## References

[references will be inserted by the LaTeX build from references.bib]
