# Plan: Add Mahjong Deployment Link

> Status: COMPLETED
> Created: 2026-07-22
> Last Updated: 2026-07-22

## Goal
Synchronise the deployed Mahjong URL across the compact HTML, generated PDF, and Compact Master Resume DOCX while preserving one-page layouts.

## Assumptions
- `https://mahjong.jiahengli.xyz` is the public deployment URL confirmed by the user.
- Existing project wording and project order remain unchanged.

## Open Questions
None.

## Spec-Lite
N/A — covered by Goal, Deliverables, and Validation.

## Design Decisions
None — no design-sensitive changes.

## Steps Overview
| Step | File | Status | Goal |
|------|------|--------|------|
| Step 1 | `steps/step-1.md` | COMPLETED | Add the Mahjong link, rebuild both generated documents, and verify one-page output. |

## Validation Commands

| Purpose | Command | Source | Required? |
|---|---|---|---|
| Content consistency | `rg -n "mahjong.jiahengli.xyz" compact-resume.html build_compact_resume_pdf.py build_compact_master_resume_docx.py` | Existing source files | Yes |
| PDF build | `/tmp/resume-pdf-env2/bin/python build_compact_resume_pdf.py` | Existing PDF builder | Yes |
| DOCX build | `/tmp/resume-docx-env2/bin/python build_compact_master_resume_docx.py` | Existing DOCX builder | Yes |
| PDF render | `pdftoppm -png -r 150 output/pdf/Jiaheng\ Li\ Compact\ Resume.pdf ...` | PDF workflow | Yes |
| DOCX render | `render_docx.py Compact\ Master\ Resume.docx --output_dir ... --emit_pdf` | Documents workflow | Yes |

## Context & Learnings
### Key Decisions
- Add Mahjong alongside the existing Gomoku, Chess, and Xiangqi links because it is another playable deployment of the same toolkit.
### Gotchas & Warnings
- Both generated formats must remain one page after adding the extra link.

> Append only. Never delete or rewrite existing entries below — only add new rows/facts as steps complete.
### Working Set
| Path | Role in this task | Evidence |
|------|-------------------|----------|
| `compact-resume.html` | Browser and print resume source | `rg` shows existing p2p deployment links. |
| `build_compact_resume_pdf.py` | Stable one-page PDF generator | Existing project link list drives clickable PDF annotations. |
| `build_compact_master_resume_docx.py` | Stable one-page DOCX generator | Existing p2p project extra-links list drives Word hyperlinks. |

### Verified Facts
- The compact resume currently lists Gomoku, Chess, and Xiangqi under p2p-lockstep-kit — verified by `rg`, 2026-07-22.
- The user confirmed Mahjong is deployed at `https://mahjong.jiahengli.xyz` — verified by user message, 2026-07-22.

## Implementation Log
| Date | Step | Summary |
|------|------|---------|
| 2026-07-22 | Step 1 | Added the live Mahjong link to HTML, PDF, and DOCX sources; rebuilt and visually verified all outputs as one A4 page. |
