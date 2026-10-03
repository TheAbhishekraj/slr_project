# AGENTS.md — SLR PROJECT

Universal rules for any AI agent working in this repo.

## Project
- Repo: E:\slr_project
- Title: GPS-Denied Navigation for UAVs — Multi-Sensor Fusion (2010–2026)
- Protocol: PRISMA 2020
- Corpus: 287 included studies, frozen 2026-10-02
- Tags: v287-certified, pre-latex-cleanup-complete

## Absolute rules
1. Read disk only. Never internet. Never memory.
2. Never modify any source file without explicit CONFIRM.
3. Never touch excluded IDs: REC_0053, REC_0693, REC_0866, REC_1688.
4. Write only inside the active output tree.
5. One task per turn. Stop after each. Wait for CONFIRM.
6. Every number cites file + line.
7. Quotes character-exact.
8. Two sources conflict → STOP and report.
9. Missing info = NOT_REPORTED.
10. American spelling. Plain words.

## Content freeze
- Body sentences byte-for-byte.
- Every numeral traceable.
- Reference keys unchanged.
- PRISMA: 2000 → 1716 → 501 → 291 → 287.

## Banned words (manuscript only)
delve, landscape (metaphor), crucial, pivotal,
state-of-the-art (unless named baseline follows), very, really,
It is important to note, It should be noted, In conclusion.

Banned paragraph openers: Moreover, Furthermore, Additionally.

## Folder map
- 00_scope/       Protocol, locked numbers
- 01_data/        Raw and processed data
- 02_cards/       Evidence cards
- 03_ai_checks/   AI screening
- 04_master/      MASTER_EVIDENCE.csv
- 05_analysis/    QA and figures
- 06_manuscript/  source/, ieee/, presentation/
- 07_certificates/ Certificates
- _AUDIT/         Governance logs
- _BIBLE/         Project bible
- _INSTRUCTIONS/  Prompts
- _PACKAGES/      Deliverables
- tools/          Automation

## Build
    cd E:\slr_project
    python tools\venue_format.py `
      --repo . `
      --format tools\formats\IEEE.conf `
      --profile tools\formats\slr_profile.generic.conf `
      --strict --confirm
