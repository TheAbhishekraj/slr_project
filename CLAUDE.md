# CLAUDE.md — SLR PROJECT

## Project
- Repo: E:\slr_project
- Title: GPS-Denied Navigation for UAVs — Multi-Sensor Fusion (2010–2026)
- Corpus: 287 included studies, frozen 2026-10-02
- Protocol: PRISMA 2020
- Tags: v287-certified, pre-latex-cleanup-complete

## Layout
- 06_manuscript/source/   — MANUSCRIPT.md, references.bib
- 06_manuscript/ieee/     — LaTeX output
- 06_manuscript/presentation/ — slide deck
- _BIBLE/                 — project bible
- _INSTRUCTIONS/          — all prompts
- _PACKAGES/              — deliverables
- tools/venue_format.py   — LaTeX converter

## Rules
- Read disk only. No internet. No memory.
- Never modify source without confirmation.
- Never touch: REC_0053, REC_0693, REC_0866, REC_1688.
- Write only inside active output tree.
- One task per turn. Wait for CONFIRM.
- Every change cites file + line.
- Two sources conflict → STOP.

## Build
    cd E:\slr_project
    python tools\venue_format.py `
      --repo . `
      --format tools\formats\IEEE.conf `
      --profile tools\formats\slr_profile.generic.conf `
      --strict --confirm

## Content freeze
- Body text byte-for-byte.
- Every numeral traceable.
- Reference keys unchanged.
- PRISMA: 2000 → 1716 → 501 → 291 → 287.

## Language
American spelling. Banned words: delve, landscape (metaphor),
crucial, pivotal, state-of-the-art (unless named baseline follows),
very, really, It is important to note, It should be noted,
In conclusion. Banned openers: Moreover, Furthermore, Additionally.
