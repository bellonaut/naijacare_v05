# In-Person Examination Requirement (Nigeria Medical & Dental Council Act §24)

**Date**: 2025-09-01  
**Prepared by**: Legal Research (NaijaCare)  
**Scope**: Telehealth diagnosis and triage

## Summary
Section 24 of the Medical & Dental Council Act requires a registered practitioner to
conduct a physical examination before issuing a diagnosis. The current NaijaCare
routing flow performs triage logic that could be interpreted as diagnostic in
practice. This creates a material compliance risk for any automated decisioning
that is not explicitly framed as non-diagnostic administrative triage.

## Key Findings
- Physical examination requirement is broadly framed and can be interpreted to
  include telehealth interactions that result in a diagnostic conclusion.
- Delegation to non-licensed staff or automated software is not explicitly covered.
- Counsel recommendation: limit system outputs to non-clinical routing guidance
  and require a licensed clinician review before any diagnostic or prescriptive
  action.

## Legal Opinion Excerpt (External Counsel)
> "Absent a physician-led physical examination, any system output that directly
> implies a diagnosis may be construed as unauthorized practice. Automated
> triage tools should be restricted to administrative routing and must be
> coupled with a documented clinician review step."

## Implications
- Automated routing must include human review gates.
- Product UI must explicitly state “not a diagnosis.”
- Clinical decision support features must remain disabled until legal clearance.
