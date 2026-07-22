# Step 1: Add and Verify Mahjong Deployment

> Status: COMPLETED
> Created: 2026-07-22

## Goal
Add the Mahjong live deployment link to all compact resume formats and verify the regenerated PDF and DOCX remain clean one-page documents.

## Prerequisites
- User-confirmed URL: `https://mahjong.jiahengli.xyz`.
- Files to modify: `compact-resume.html`, `build_compact_resume_pdf.py`, `build_compact_master_resume_docx.py`.
- Existing PDF and DOCX builders remain the source of generated artifacts.

## Deliverables
- Mahjong appears as a clickable link in HTML, PDF, and DOCX.
- After this step: both generated documents render as one clean A4 page.

## Plan
- [x] `edit` `compact-resume.html` — append Mahjong to the p2p project links.
- [x] `edit` `build_compact_resume_pdf.py` — append Mahjong to the PDF project link list.
- [x] `edit` `build_compact_master_resume_docx.py` — append Mahjong to the DOCX project extra-links list.
- [x] `bash` builders and renderers — regenerate and visually inspect PDF and DOCX outputs.
- [x] `bash` structural checks — confirm link targets, page counts, and absence of DOCX tables/text boxes.

## Quality Checklist
- [x] Evidence-before-edit: targets read through prior compact-resume work; impact search confirms three source locations; validation commands recorded in `plan.md`.
- [x] Existing pattern / reuse checked: reuse the existing project link lists in all three sources.
- [x] Contract understood: input is one confirmed public URL; outputs are three clickable resume links.
- [x] Risk reviewed: layout overflow and broken hyperlink targets.
- [x] Mitigation recorded: rebuild, page-count checks, hyperlink inspection, and PNG review.

## Validation Checklist
- [x] PDF builder exits 0 and produces one A4 page.
- [x] DOCX builder and renderer exit 0 and produce one A4 page.
- [x] `rg` finds the exact URL in all three sources.

## Test Checklist
- [x] N/A — document generation is validated through structural checks and visual rendering.

## Implementation Notes
Added Mahjong after Xiangqi in each existing link list. The live URL returned HTTP 200. Generated PDF, browser-print PDF, and rendered DOCX each remained one A4 page; the DOCX contains no tables or text boxes.

## Files Changed
- `compact-resume.html`
- `build_compact_resume_pdf.py`
- `build_compact_master_resume_docx.py`
- `output/pdf/Jiaheng Li Compact Resume.pdf`
- `Compact Master Resume.docx`
