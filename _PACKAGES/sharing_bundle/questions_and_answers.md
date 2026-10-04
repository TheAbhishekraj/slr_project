# Supervisor Presentation: Anticipated Q&A

**Q1: Why limit the search to only IEEE Xplore and Scopus?**
A: These two databases provide the highest concentration of peer-reviewed aerospace, robotics, and control systems literature, capturing the core of UAV navigation research. While adding databases like Web of Science might yield marginal duplicates, the 1,000-record relevance cap per database ensured we extracted the highest-impact studies. This decision balances exhaustive coverage with feasible manual extraction for a single reviewer.

**Q2: What exactly does "MIXED environment" mean in your results?**
A: "MIXED" refers to studies where the environment was either unspecified, generic, or consisted of both indoor and outdoor components without dedicating the evaluation to a specific challenging edge case. It accounts for 67% of the corpus, highlighting that most algorithms are tested under relatively benign or broad conditions. This demonstrates a lack of rigorous, domain-specific environmental stress testing in the field.

**Q3: Why are there only 5 adversarial studies out of 287?**
A: Historically, the robotics community has treated GPS-denial as a natural degradation problem (e.g., flying under a canopy or indoors) rather than an active electronic warfare threat. Consequently, threat models like GNSS spoofing or intentional jamming are rarely integrated into standard sensor fusion pipelines. This is the most critical operational gap identified by the review.

**Q4: How did you define "Quality" in your appraisal rubric?**
A: Quality was defined strictly as methodological rigor, not algorithmic novelty or theoretical brilliance. We scored studies out of 10 points based on experimental rigor (e.g., physical flight vs. simulation), reporting completeness, baseline fairness, and open-source reproducibility. A high score indicates a highly reproducible and empirically validated study.

**Q5: Why did you cap simulation-only studies at Q-Medium?**
A: Pure simulation cannot fully capture unmodeled aerodynamics, sensor noise, or unexpected real-world physical perturbations. Even a perfectly designed simulation study leaves the critical deployment step unvalidated. Therefore, to reward empirical reality, physical flight validation was required to achieve a Q-High rating.

**Q6: What is meant by "Weak Platform Specificity"?**
A: Over a third of the studies validate their algorithms using a generic kinematic model (`GENERIC_UAV`), ignoring specific aerodynamic constraints. In reality, a quadrotor flies very differently from a fixed-wing UAV, especially under wind disturbances or aggressive maneuvers. Algorithms that ignore these kinematics are often brittle when ported to physical hardware.

**Q7: Why does Vision dominate the sensor distributions?**
A: Cameras are lightweight, power-efficient, and provide incredibly rich spatial data, making them ideal for Size, Weight, and Power (SWaP)-constrained UAVs. Furthermore, the explosion of open-source Visual-Inertial Odometry (VIO) and SLAM frameworks over the last decade has significantly lowered the barrier to entry for vision-based research.

**Q8: You mention Factor Graphs are displacing classical filtering. Why?**
A: Factor graphs formulate state estimation as an optimization problem over a window of past states, rather than strictly relying on the Markov assumption of the previous state like an EKF. This allows them to better handle delayed measurements, non-linearities, and asynchronous multi-sensor data. They have become the architectural standard for modern robust fusion.

**Q9: Why are only 5 studies cited in the manuscript body?**
A: The manuscript follows a narrative synthesis approach, focusing deeply on the operational gaps—specifically the 5 adversarial studies—rather than dryly listing all 287. This complies with PRISMA 2020 Item 17, as the full list of 287 studies is rigorously cited and presented in Appendix A. 

**Q10: What were the four excluded studies at the full-text stage?**
A: Three studies (REC_0053, REC_0693, REC_0866) were excluded for being out of scope after a deeper full-text review, failing to meet our strict multi-sensor or UAV-specific criteria. One study (REC_1688) was excluded because the full text was not available in English. These are documented purely for PRISMA auditability.

**Q11: How do we know the data extraction is reliable with only one reviewer?**
A: To mitigate single-reviewer bias, every extracted data point was strictly anchored to verbatim quotes from the source texts. The entire extraction database (`MASTER_EVIDENCE.csv`) and the individual evidence cards are publicly available in our repository. Any contested data point can be traced back to the exact paragraph in the original PDF.

**Q12: Why didn't you perform a quantitative meta-analysis?**
A: The corpus exhibits massive heterogeneity in metric definitions, trajectory lengths, and sensor hardware combinations. For example, comparing Absolute Trajectory Error (ATE) across a 10-meter indoor flight and a 2-kilometer outdoor flight is statistically invalid. Therefore, the findings were synthesized narratively.

**Q13: How did you ensure the LaTeX compilation didn't alter the data?**
A: We implemented an automated token-count freeze check via our custom Python build script (`cli.py`). It strips the formatting from both the Markdown source and the compiled LaTeX output and compares the literal word tokens. The build fails automatically if any data drift or content alteration is detected.

**Q14: Are you going to publish the custom Python build tools?**
A: Yes, the tools are included in the GitHub repository. They demonstrate a novel, reproducible workflow for writing academic papers in Markdown and programmatically generating IEEE-compliant LaTeX without manual formatting errors.

**Q15: What specific sensor hardware is most common?**
A: Unfortunately, the field suffers from poor hardware reporting standards, often listing "a camera and IMU" without specifying noise densities, biases, or exact models. Because sensor extraction was non-normalized due to this poor reporting, we could only confidently classify sensors into broad families (e.g., VISION, IMU_ONLY) rather than specific hardware models.

**Q16: How do we translate this SLR into our lab's next research project?**
A: The SLR provides a clear mandate: the field needs navigation architectures built specifically for contested environments. Our next project should focus on sensor fusion that explicitly models GNSS spoofing as an adversarial state, validating it on a specific airframe (e.g., fixed-wing) rather than a generic model.

**Q17: Did you find any trends in the use of Artificial Intelligence/Deep Learning?**
A: While deep learning is increasingly used for specific perception tasks (like object detection or feature matching), the core sensor fusion architectures still heavily rely on probabilistic state estimation (Factor Graphs, EKF). "End-to-end" AI navigation remains a minority approach due to its lack of interpretability and safety guarantees.

**Q18: What was the most surprising finding in the review?**
A: The sheer volume of pure-simulation studies (24%) was unexpected. Despite the accessibility of commercial off-the-shelf UAVs, nearly a quarter of the field still publishes sensor fusion algorithms without ever testing them against real-world aerodynamic disturbances or physical sensor noise.

**Q19: How did you handle studies that used multiple UAVs (swarm navigation)?**
A: Studies focusing on cooperative or swarm navigation were categorized under the "COOPERATIVE" method category (14.3% of the corpus). These were included as long as they met the core criteria of multi-sensor fusion in a GPS-denied context, as cooperative localization is a valid fusion strategy.

**Q20: Why is PROSPERO registration missing, and does it matter?**
A: PROSPERO is primarily designed for health and social care reviews, and robotics SLRs frequently bypass it. While pre-registration is best practice for transparency, our complete Git version history and immutable data freezes (`v287-certified`) serve as a robust, mathematically verifiable alternative to a traditional registry.
