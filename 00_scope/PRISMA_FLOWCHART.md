# PRISMA 2020 Flowchart

This document provides a visual representation of the systematic literature review (SLR) pipeline census for the GPS-Denied UAV project.

```mermaid
graph TD
    %% Identification
    subgraph Identification
        A1["Records identified from<br/>Databases (n = 2,000)<br/>• IEEE Xplore: 1,000<br/>• Scopus: 1,000"] --> A2["Records removed before screening:<br/>Duplicate records removed (n = 284)"]
        A1 --> B1
    end

    %% Screening
    subgraph Screening
        B1["Records screened<br/>(n = 1,716)"] --> B2["Records excluded based on<br/>Title/Abstract (n = 1,215)"]
        B1 --> C1["Reports sought for retrieval<br/>(n = 501)"]
        C1 --> C2["Reports not retrieved<br/>(n = 210)"]
        C1 --> D1["Reports assessed for eligibility<br/>Full-text PDFs (n = 291)"]
        D1 --> D2["Reports excluded (n = 4):<br/>• Out of scope [X1] (n = 3)<br/>• Non-English full text [X3] (n = 1)"]
    end

    %% Included
    subgraph Included
        D1 --> INC1["Studies included in review<br/>Frozen Denominator (n = 287)"]
    end
    
    style A1 fill:#f9f2f4,stroke:#333,stroke-width:2px
    style B1 fill:#e2f0d9,stroke:#333,stroke-width:2px
    style C1 fill:#e2f0d9,stroke:#333,stroke-width:2px
    style D1 fill:#e2f0d9,stroke:#333,stroke-width:2px
    style INC1 fill:#d9e1f2,stroke:#333,stroke-width:4px
```

## Census Breakdown
* **Raw:** 2,000
* **Unique:** 1,716
* **Screened-in (Title/Abstract):** 501
* **Full-text Retrieved:** 291
* **Final Included:** 287
