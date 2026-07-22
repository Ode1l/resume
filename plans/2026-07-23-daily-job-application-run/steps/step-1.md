# Step 1: Generate Tailored Documents

> Status: COMPLETED
> Created: 2026-07-23

## Goal
Create concise role-specific resume and cover-letter DOCX files for every selected high-confidence vacancy and verify their layout.

## Prerequisites
- Candidate facts verified in `application-profile.md`.
- Compact layout verified in `build_compact_master_resume_docx.py`.
- Job descriptions captured from LinkedIn, SEEK, and SJS.

## Deliverables
- One tailored resume and one tailored cover letter per selected vacancy.
- Rendered one-page output with working external hyperlinks.

## Plan
- [x] `apply_patch` `build_daily_job_applications.py` — add a data-driven document generator reusing the compact layout.
- [x] `bash` generate all selected application documents.
- [x] `bash` render and audit every generated file.

## Quality Checklist
- [x] Evidence-before-edit: read `application-profile.md` and `build_compact_master_resume_docx.py`; impact is isolated to new application files; validation commands identified.
- [x] Existing pattern / reuse checked: compact builder and existing Smartly files.
- [x] Contract understood: one-page ATS-friendly DOCX files with hyperlinks and confirmed facts only.
- [x] Risk reviewed: factual overstatement, page overflow, broken hyperlinks.
- [x] Mitigation recorded: fact index, render QA, OOXML relationship audit.

## Validation Checklist
- [x] Builder compiles and exits 0.
- [x] All generated DOCX files render to one page without clipping or overlap.
- [x] All expected hyperlinks exist in OOXML relationships.

## Test Checklist
- [x] Batch generation and render/audit script completes without failures.

## Implementation Notes
Generated 10 tailored resumes and 10 tailored cover letters. Added a third relevant project to improve page balance without padding work history. All files rendered to exactly one page and passed external-link and table audits.

## Files Changed
- `build_daily_job_applications.py`
- `applications/2026-07-23/*.docx` (20 files)
- `applications/2026-07-23/rendered-qa2/*/page-1.png` (20 QA renders)
