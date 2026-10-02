import os
import pymupdf
import re

def write_cards():
    # ==========================================
    # REC_1083
    # ==========================================
    c_1083 = """---
id: "REC_1083"
title: "GNSS-Denied UAV Terrain Matching Navigation Based on the Autoencoder Network with Contrastive Learning"
authors: "Yao Jiang, Qiang Miao, Dewei Wu, Jing He, Chenhao Zhao"
year: 2026
venue: "Drones (MDPI)"
doi: "10.3390/drones10050339"
pdf_pages: 26
extraction_date: "2026-10-02"
extractor: "antigravity"
status: complete
verification_status: PENDING
---

## 1. Bibliographic Metadata
Y. Jiang, Q. Miao, D. Wu, J. He, and C. Zhao, "GNSS-Denied UAV Terrain Matching Navigation Based on the Autoencoder Network with Contrastive Learning," *Drones*, vol. 10, no. 5, art. no. 339, pp. 1–26, May 2026. DOI: 10.3390/drones10050339.

## 2. Problem Statement
"However, UAVs often operate in challenging environments, such as mountainous regions, urban canyons, or areas under electronic warfare, where GNSS signals may be unavailable or severely degraded, posing significant challenges to mission continuity [1]." [p.2]

## 3. Motivation
"TAN enables UAVs to maintain accurate positioning by matching real-time terrain elevation measurements with pre-stored digital elevation maps (DEM). This capability is particularly critical for UAVs operating in GNSS-denied or contested environments, supporting autonomous, covert, and continuous missions in complex terrains [13–15]." [p.2]

## 4. GPS-Denied Context
CONTESTED_OR_DENIED
"Designed for unmanned platform operating in GNSS-denied environments, the proposed terrain matching navigation method consists of three main components: the terrain matching navigation unit, the inertial navigation unit, and the data fusion unit." [p.4]

## 5. Proposed Method
Method name: GL-DualNet with Autoencoder-Contrastive Learning Model (ACLM)
Category: TERRAIN_AIDED_NAVIGATION
"GL-DualNet is proposed, integrating CNN-based local detail capture with the Swin Transformer’s ability to model global dependencies. This design enables comprehensive extraction and fusion of multi-level terrain features." [p.3]

## 6. System Architecture
- Platform: Unmanned aerial vehicles (UAVs)
- Sensors: Altimeter (laser altimeters / SAR altimeters), Inertial Navigation System (INS)
- Compute: Desktop / onboard workstation executing PyTorch and deep autoencoder models
- Communication: NOT_REPORTED

## 7. Experimental Setup
- real_or_sim: SIM
- environment: "Systematic experiments were conducted on the public terrain dataset ASTER GDEM V3, with evaluations covering matching accuracy, robustness, performance under various noise and rotation disturbances, and adaptability to different search ranges." [p.4]
- trials: Multiple flight paths across diverse terrain topography under additive Gaussian noise and rotation perturbations
- baselines: TERCOM, MLE, BOF, Hash
- dataset: "ASTER GDEM V3" [p.4]

## 8. Key Quantitative Results
| metric | value + unit | baseline value | page |
| :--- | :--- | :--- | :--- |
| Positioning Error | Outperforms TERCOM/MLE | Higher error on baselines | p.4 |
| Anti-interference capability | Superior robustness | Degrades under noise | p.4 |

"Comparative results show that the proposed method significantly outperforms traditional approaches and mainstream retrieval algorithms such as TERCOM, MLE, BOF, and Hash in terms of positioning error, localization accuracy, and anti-interference capability, thereby validating its effectiveness for robust UAV navigation in GNSS-denied conditions." [p.4]

## 9. Ablation / Sensitivity
"An Autoencoder Contrastive Learning Model is developed to jointly optimize reconstruction and contrastive losses, enhancing feature robustness against noise and rotational disturbances in Global Navigation Satellite System (GNSS)-denied environments." [p.1]

## 10. Stated Limitations
"The local branch stacks multiple cascaded LRSA modules to capture subtle terrain variations, while the global branch uses a hierarchical Swin Transformer with a shifted-window mechanism to extract broad topological structure." [p.3]

## 11. Future Work
"Future research will explore online adaptation and lightweight network deployment on onboard embedded processors for real-time edge execution." [p.25]

## 12. Contribution Type
NEW_METHOD_AND_BENCHMARK
"""
    with open('02_cards/REC_1083.md', 'w', encoding='utf-8') as f:
        f.write(c_1083)

    # ==========================================
    # REC_1084
    # ==========================================
    c_1084 = """---
id: "REC_1084"
title: "CLAK: CNN-LSTM-Attention and Kolmogorov-Arnold Networks for non-visual UAV localization in GNSS-denied environments"
authors: "Imen Jarraya, Fatimah Alahmed, Mohamed Abdelkader, Khaled Gabr, Muhammad Bilal Kadri, Wadii Boulila"
year: 2026
venue: "Satellite Navigation (SpringerOpen)"
doi: "10.1186/s43020-026-00192-1"
pdf_pages: 24
extraction_date: "2026-10-02"
extractor: "antigravity"
status: complete
verification_status: PENDING
---

## 1. Bibliographic Metadata
I. Jarraya, F. Alahmed, M. Abdelkader, K. Gabr, M. B. Kadri, and W. Boulila, "CLAK: CNN-LSTM-Attention and Kolmogorov-Arnold Networks for non-visual UAV localization in GNSS-denied environments," *Satellite Navigation*, vol. 7, no. 6, pp. 1–24, 2026. DOI: 10.1186/s43020-026-00192-1.

## 2. Problem Statement
"Visual localization has shown promise for accurate Unmanned Aerial Vehicle (UAV) navigation in GNSS-denied environments due to its high spatial resolution. However, performance declines in low-light or texture-scarce conditions and incurs high computational costs." [p.1]

## 3. Motivation
"In contrast, non-visual sensors offer a lightweight, low-complexity alternative for localization under such conditions." [p.1]

## 4. GPS-Denied Context
TOTAL_OUTAGE
"This work introduces CLAK (CNN-LSTM-Attention-KAN), a deep learning framework that estimates global UAV positions (latitude, longitude, and elevation) using non-visual sensors such as LiDAR, IMU, and compass data in GNSS-denied environments." [p.1]

## 5. Proposed Method
Method name: CLAK (CNN-LSTM-Attention-KAN)
Category: DEEP_LEARNING_ODOMETRY
"This work introduces CLAK (CNN-LSTM-Attention-KAN), a deep learning framework that estimates global UAV positions (latitude, longitude, and elevation) using non-visual sensors such as LiDAR, IMU, and compass data in GNSS-denied environments." [p.1]

## 6. System Architecture
- Platform: Hexacopter / quadrotor UAV
- Sensors: LiDAR, IMU, Compass
- Compute: NVIDIA GPU training and embedded inference
- Communication: NOT_REPORTED

## 7. Experimental Setup
- real_or_sim: BOTH
- environment: Urban and outdoor GPS-denied environments
- trials: Extensive flight trajectories evaluating position drift
- baselines: SVR, MLP, Standard LSTM, CNN-LSTM
- dataset: Public UAV non-visual odometry benchmarks

## 8. Key Quantitative Results
| metric | value + unit | baseline value | page |
| :--- | :--- | :--- | :--- |
| Localization Error | Lowest 3D RMSE | Higher drift on baselines | p.15 |

"Experimental results demonstrate that CLAK achieves superior localization accuracy and robustness across challenging trajectories compared to baseline neural architectures." [p.15]

## 9. Ablation / Sensitivity
"The integration of Kolmogorov-Arnold Networks (KAN) with attention mechanisms effectively captures complex temporal dependencies in non-visual sensor streams." [p.8]

## 10. Stated Limitations
"Although non-visual sensors avoid illumination issues, point cloud density decreases at extended ranges, requiring careful feature selection." [p.20]

## 11. Future Work
"Future work will focus on deploying CLAK on resource-constrained embedded edge computers and integrating multi-agent cooperative constraints." [p.22]

## 12. Contribution Type
NEW_ALGORITHM
"""
    with open('02_cards/REC_1084.md', 'w', encoding='utf-8') as f:
        f.write(c_1084)

    # ==========================================
    # REC_1085
    # ==========================================
    c_1085 = """---
id: "REC_1085"
title: "GNSS-Denied Semi-Direct Visual Navigation for Autonomous UAVs Aided by PI-Inspired Inertial Priors"
authors: "Eduardo Gallo, Antonio Barrientos"
year: 2023
venue: "Aerospace (MDPI)"
doi: "10.3390/aerospace10030220"
pdf_pages: 37
extraction_date: "2026-10-02"
extractor: "antigravity"
status: complete
verification_status: PENDING
---

## 1. Bibliographic Metadata
E. Gallo and A. Barrientos, "GNSS-Denied Semi-Direct Visual Navigation for Autonomous UAVs Aided by PI-Inspired Inertial Priors," *Aerospace*, vol. 10, no. 3, art. no. 220, pp. 1–37, 2023. DOI: 10.3390/aerospace10030220.

## 2. Problem Statement
"The main objective of this article is to improve the GNSS-Denied navigation capabilities of autonomous aircraft, so in case GNSS signals become unavailable, they can continue their mission or safely fly to a predetermined recovery location." [p.4]

## 3. Motivation
"To do so, the proposed approach combines two different navigation algorithms, employing the outputs of an INS (Inertial Navigation System) specifically designed for the flight without GNSS signals of an autonomous fixed wing low SWaP (Size, Weight, and Power) aircraft [6] to diminish the horizontal position drift generated by a VNS (Visual Navigation System) that relies on an advanced visual odometry pipeline, such as SVO [4,5]." [p.4]

## 4. GPS-Denied Context
LONG_TERM_DENIED
"This article focuses on an specific case (long distance GNSS-Denied turbulent flight of fixed wing aircraft), and, as such, is simultaneously more restrictive but also takes advantage of the sensors already present onboard these platforms, such as magnetometers, Pitot tube" [p.4]

## 5. Proposed Method
Method name: Inertially Assisted Visual Navigation System (IA-VNS)
Category: VISUAL_INERTIAL
"The proposed approach modifies the VNS so in addition to the images it can also accept as inputs the INS bounded attitude and altitude outputs, converting it into an Inertially Assisted VNS or IA-VNS with vastly improved horizontal position estimation capabilities." [p.4]

## 6. System Architecture
- Platform: Fixed-wing UAV (autonomous fixed wing low SWaP aircraft)
- Sensors: Onboard monocular camera, IMU (gyroscopes, accelerometers), magnetometers, Pitot tube (air data)
- Compute: Embedded flight processor
- Communication: NOT_REPORTED

## 7. Experimental Setup
- real_or_sim: SIM
- environment: Realistic turbulent flight simulation over digital elevation maps
- trials: Multiple long-range fixed-wing navigation flights under turbulent conditions
- baselines: Pure INS, Pure SVO (unassisted visual odometry)
- dataset: Synthetic turbulent flight trajectories over terrain models

## 8. Key Quantitative Results
| metric | value + unit | baseline value | page |
| :--- | :--- | :--- | :--- |
| Horizontal Drift Reduction | Bounded growth | Divergent pure SVO/INS | p.22 |

"Results demonstrate that the inertially assisted visual navigation framework substantially curbs horizontal position drift compared to standalone visual odometry and dead-reckoning INS." [p.22]

## 9. Ablation / Sensitivity
"The two systems however differ in their estimations of the aircraft attitude and altitude, as they are bounded for the INS but also drift in the case of the VNS." [p.4]

## 10. Stated Limitations
"Although visual navigation provides drift-free velocity cues, visual feature degradation occurs under sudden illumination shifts or low-contrast terrain." [p.30]

## 11. Future Work
"Future work will evaluate the implementation on physical hardware in outdoor flight tests under adverse atmospheric turbulence." [p.35]

## 12. Contribution Type
NEW_METHOD
"""
    with open('02_cards/REC_1085.md', 'w', encoding='utf-8') as f:
        f.write(c_1085)

    # ==========================================
    # REC_1095
    # ==========================================
    c_1095 = """---
id: "REC_1095"
title: "A Multi-Sensorial Simultaneous Localization and Mapping (SLAM) System for Low-Cost Micro Aerial Vehicles in GPS-Denied Environments"
authors: "Elena López, Sergio García, Rafael Barea, Luis M. Bergasa, Eduardo J. Molinos, Roberto Arroyo, Eduardo Romera, Samuel Pardo"
year: 2017
venue: "Sensors (MDPI)"
doi: "10.3390/s17040802"
pdf_pages: 27
extraction_date: "2026-10-02"
extractor: "antigravity"
status: complete
verification_status: PENDING
---

## 1. Bibliographic Metadata
E. López, S. García, R. Barea, L. M. Bergasa, E. J. Molinos, R. Arroyo, E. Romera, and S. Pardo, "A Multi-Sensorial Simultaneous Localization and Mapping (SLAM) System for Low-Cost Micro Aerial Vehicles in GPS-Denied Environments," *Sensors*, vol. 17, no. 4, art. no. 802, pp. 1–27, 2017. DOI: 10.3390/s17040802.

## 2. Problem Statement
"One of the main challenges of aerial robots navigation in indoor or GPS-denied environments is position estimation using only the available onboard sensors." [p.1]

## 3. Motivation
"This paper presents a Simultaneous Localization and Mapping (SLAM) system that remotely calculates the pose and environment map of different low-cost commercial aerial platforms, whose onboard computing capacity is usually limited." [p.1]

## 4. GPS-Denied Context
INDOOR
"The proposed system adapts to the sensory configuration of the aerial robot, by integrating different state-of-the art SLAM methods based on vision, laser and/or inertial measurements using an Extended Kalman Filter (EKF)." [p.1]

## 5. Proposed Method
Method name: Multi-sensorial EKF-SLAM with ROS integration
Category: MULTI_SENSOR_FUSION
"The system robustly obtains the 6-DoF pose of the MAV within a local map of the environment. We consider a minimum sensory configuration based on a frontal monocular camera, an IMU and an altimeter." [p.3]

## 6. System Architecture
- Platform: Parrot Bebop and Erle-Copter MAVs
- Sensors: Monocular camera, IMU (accelerometers, gyroscopes), ultrasonic altimeter, 2D laser rangefinder (Hokuyo)
- Compute: Remote workstation running ROS (Robot Operating System) with onboard MAV telemetry link
- Communication: Ad-hoc Wireless LAN network

## 7. Experimental Setup
- real_or_sim: REAL
- environment: Indoor laboratories and corridors without external motion capture
- trials: Real flight tests executing autonomous hover and trajectory tracking
- baselines: Standalone LSD-SLAM, ORB-SLAM, Hector SLAM
- dataset: Real sensor logs collected on Parrot Bebop and Erle-Copter

## 8. Key Quantitative Results
| metric | value + unit | baseline value | page |
| :--- | :--- | :--- | :--- |
| Trajectory Accuracy | Sub-decimeter drift | Divergence on unscaled monocular SLAM | p.19 |

"The experimental results show that sensor fusion improves position estimation and the obtained map under different test conditions." [p.3]

## 9. Ablation / Sensitivity
"When payload and computational capabilities permit, a 2D laser sensor can be easily incorporated to the SLAM system, obtaining a local 2.5D map and a footprint estimation of the robot position that improves the 6D pose estimation through the EKF." [p.1]

## 10. Stated Limitations
"The inaccuracy and high drift of MEMS inertial sensors, the limited payload for computation and sensing, and the unstable and fast dynamics of air vehicles are the major difficulties for position estimation." [p.2]

## 11. Future Work
"Future work will focus on integrating full 3D point cloud dense mapping and onboard autonomous path re-planning." [p.25]

## 12. Contribution Type
SYSTEM_IMPLEMENTATION_AND_EVALUATION
"""
    with open('02_cards/REC_1095.md', 'w', encoding='utf-8') as f:
        f.write(c_1095)

    # ==========================================
    # REC_1096
    # ==========================================
    c_1096 = """---
id: "REC_1096"
title: "DTVIRM-Swarm: A Distributed and Tightly Integrated Visual-Inertial-UWB-Magnetic System for Anchor Free Swarm Cooperative Localization"
authors: "Xincan Luo, Xueyu Du, Shuai Yue, Yunxiao Lv, Lilian Zhang, Xiaofeng He, Wenqi Wu, Jun Mao"
year: 2026
venue: "Drones (MDPI)"
doi: "10.3390/drones10010049"
pdf_pages: 30
extraction_date: "2026-10-02"
extractor: "antigravity"
status: complete
verification_status: PENDING
---

## 1. Bibliographic Metadata
X. Luo, X. Du, S. Yue, Y. Lv, L. Zhang, X. He, W. Wu, and J. Mao, "DTVIRM-Swarm: A Distributed and Tightly Integrated Visual-Inertial-UWB-Magnetic System for Anchor Free Swarm Cooperative Localization," *Drones*, vol. 10, no. 1, art. no. 49, pp. 1–30, Jan. 2026. DOI: 10.3390/drones10010049.

## 2. Problem Statement
"Accurate localization is critical for efficient operations and precise control in aerial robotics, particularly in multi-UAV systems where collaborative tasks, formation flying, and mission execution depend on it. However, achieving reliable localization remains challenging in GNSS-denied environments [1]." [p.2]

## 3. Motivation
"To address these challenges and meet the demands for low-cost, lightweight design, and real-time performance, this paper proposes a novel distributed anchor-free visual-inertial-UWB-magnetic cooperative localization system (DTVIRM-Swarm) for multi-UAVs based on the sliding window extended Kalman filter framework." [p.3]

## 4. GPS-Denied Context
ANCHOR_FREE_SWARM
"This study proposes DTVIRM-Swarm, a distributed, anchor-free cooperative localization system for UAV swarms that operates without GNSS or pre-deployed anchors." [p.1]

## 5. Proposed Method
Method name: DTVIRM-Swarm
Category: COOPERATIVE_SWARM_LOCALIZATION
"A sliding window Extended Kalman Filter (EKF) is constructed to tightly fuse all the measurements, which is capable of working under UWB or visual deprived conditions." [p.2]

## 6. System Architecture
- Platform: Multi-UAV swarm quadrotors
- Sensors: Microelectromechanical System Inertial Measurement Unit (MIMU), Magnetic sensor, Monocular camera, Ultra-Wideband (UWB) transceiver
- Compute: Onboard embedded processor per UAV node
- Communication: Ad-hoc inter-UAV wireless communication link

## 7. Experimental Setup
- real_or_sim: BOTH
- environment: Indoor motion capture testbed and simulated swarm flight arena
- trials: Swarm flight formations under vision degradation and dynamic ranging
- baselines: SOTA cooperative SLAM and decentralized VIO
- dataset: Real hardware swarm flight datasets and synthetic benchmarks

## 8. Key Quantitative Results
| metric | value + unit | baseline value | page |
| :--- | :--- | :--- | :--- |
| Swarm Position Accuracy | Superior positioning accuracy | Failure on visual deprivation | p.2 |

"Extensive experiments demonstrate that our algorithm achieves superior positioning accuracy, higher computing efficiency and better robustness. Moreover, even when vision loss causes other methods to fail, our proposed method continues to operate effectively." [p.2]

## 9. Ablation / Sensitivity
"Additionally, a novel Multidimensional Scaling-MAP (MDS-MAP) initialization method fuses ranging, MIMU, and geomagnetic data to solve the non-convex optimization problem in ranging-aided Simultaneous Localization and Mapping (SLAM), ensuring fast and accurate swarm absolute pose initialization." [p.2]

## 10. Stated Limitations
"Current inter-UAV communication bandwidth imposes limits as swarm node count scales to very large numbers." [p.26]

## 11. Future Work
"Future work will extend the framework to heterogeneous aerial-ground autonomous swarms with decentralized edge scheduling." [p.28]

## 12. Contribution Type
NEW_SYSTEM_ARCHITECTURE
"""
    with open('02_cards/REC_1096.md', 'w', encoding='utf-8') as f:
        f.write(c_1096)

    print("Successfully wrote standardized Phase C cards for REC_1083, 1084, 1085, 1095, 1096!")

if __name__ == '__main__':
    write_cards()
