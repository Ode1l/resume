# Plan: Daily Job Application Run

> Status: ACTIVE
> Created: 2026-07-23
> Last Updated: 2026-07-23

## Goal
Scan LinkedIn, SEEK, and SJS for eligible software roles posted in the last 14 days, prepare tailored application documents, and submit approved applications with a complete status report.

## Assumptions
- The confirmed facts in `application-profile.md`, `Compact Master Resume.docx`, and `index.html` are authoritative.
- Final application submission remains an external consequential action requiring action-time confirmation.

## Open Questions
- Confirm whether the oldest generic `resume.pdf` may be deleted from SEEK to free one upload slot.
- SJS requires the user to complete sign-in before the Carbonees application can continue.

## Spec-Lite

### Acceptance Criteria
- [ ] Only roles posted in the last 14 days and compatible with an Open Work Visa are processed.
- [ ] Each selected role has a concise tailored resume and cover letter.
- [ ] Every generated DOCX is rendered and visually checked.
- [ ] Application forms are prepared to the final submission step.
- [ ] Submitted and skipped roles are recorded with reasons.

### Non-goals
- Applying to senior-only, citizenship/residency-only, security-clearance, or clearly mismatched specialist roles.
- Replacing the four base resume DOCX files or the public master resume.

### Edge Cases
- Duplicate roles across sites are treated as one application.
- Account sign-in, CAPTCHA, and final submission may require user action or confirmation.

## Design Decisions
| Decision | Options Considered | Chosen | Confirmed |
|----------|--------------------|--------|-----------|
| Application document style | Full two-page master vs compact one-page targeted | Compact one-page targeted, consistent with the user's approved compact resume | yes |
| Candidate scope | Every search result vs high-confidence junior/intermediate matches | High-confidence eligible matches within 14 days; record exclusions | yes |

## Steps Overview
| Step | File | Status | Goal |
|------|------|--------|------|
| Step 1 | `steps/step-1.md` | COMPLETED | Generate and verify tailored documents |
| Step 2 | `steps/step-2.md` | IN_PROGRESS | Prepare online application forms |
| Step 3 | `steps/step-3.md` | PENDING | Submit confirmed applications and report results |

## Validation Commands
| Purpose | Command | Source | Required? |
|---|---|---|---|
| Syntax | `/tmp/resume-docx-env2/bin/python -m py_compile build_daily_job_applications.py` | Existing Python document builders | yes |
| Generate | `/tmp/resume-docx-env2/bin/python build_daily_job_applications.py` | Existing Python document builders | yes |
| Render | `render_docx.py <docx> --output_dir <dir>` | Documents skill | yes |
| Link/page audit | OOXML relationship and rendered page count check | Documents skill and existing workflow | yes |

## Context & Learnings
### Key Decisions
- Reuse the approved compact resume design and customise only high-value content.
- Keep software roles to Skyline and Yonyou; exclude Optimal IT Support except support-targeted applications.

### Gotchas & Warnings
- SJS direct job URLs require navigation from search results to populate content reliably.
- LinkedIn and SEEK contain duplicate advertisements and roles with soft versus hard year requirements.
- SEEK reached its stored-resume limit after four targeted applications; no existing document was deleted without approval.
- SEEK cover letters were entered as tailored text where its file picker returned an incorrect historic filename.

### Working Set
| Path | Role in this task | Evidence |
|------|-------------------|----------|
| `application-profile.md` | Confirmed fact index | Read 2026-07-23 |
| `build_compact_master_resume_docx.py` | Approved compact layout and helpers | Read 2026-07-23 |
| `Compact Master Resume.docx` | Master document reference | Existing verified artifact |
| `Smartly Full Stack Software Engineer Resume.docx` | Existing tailored application | Existing workspace file |

### Verified Facts
- Candidate has an Open Work Visa valid until 25 February 2029 with no sponsorship required — verified in `application-profile.md`.
- Candidate has three years of commercial software-development experience and approximately 1.5 years commercial .NET experience — verified in `application-profile.md`.
- Current job searches were constrained to 14 days and detailed posting dates were checked in the browser — verified 2026-07-23.

## Implementation Log
| Date | Step | Summary |
|------|------|---------|
| 2026-07-23 | Step 1 | Generated 20 one-page DOCX files for 10 roles; rendered all files and passed page, table, and hyperlink audits. |
| 2026-07-23 | Step 2 | Prepared The Rebel Fleet, Sunstone Talent, Gallagher Insurance, and Geneva Finance SEEK applications to final review with tailored resumes and cover letters. |
| 2026-07-23 | Step 2 | Prepared Novamind Labs LinkedIn Easy Apply to final submission with the tailored resume; no cover-letter field was provided. |
| 2026-07-23 | Step 2 | Prepared the Re-Leased Greenhouse form with tailored resume, cover-letter text, eligibility, source, location, and NZD 70,000 salary expectation. |
| 2026-07-23 | Step 2 | Datacom blocked at SEEK's resume-storage limit; Carbonees blocked at SJS sign-in; Global Wave was no longer accepting applications. |
