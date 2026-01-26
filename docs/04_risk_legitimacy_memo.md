# Risk & Legitimacy Memo (Early-Stage Assessment)

**Disclaimer:** This memo is from early-stage exploration and is *not* legal advice.

## Risks Identified (Early 2025)

### 1. Unbounded Professional Liability
- Routing algorithm is heuristic (keyword-based), not clinically validated
- Emergency flags could be missed; false negatives could cause harm
- No malpractice insurance, no clinical supervision, no liability cap
- **Status:** Unresolved → No pathway to mitigation without formal clinical partnership

### 2. Missing Infrastructure
- **Consent & Enrollment:** No formal opt-in process, no consent database
- **Audit Trail:** Logs exist but no compliance framework (HIPAA, GDPR, NDPR alternatives)
- **Data Handling:** No encryption, backup, or disaster recovery
- **Escalation Protocol:** Who receives urgent calls? Where's the SOP?

### 3. Regulatory Uncertainty
- Nigeria's health tech regulations (NDPR, standards from FeHWAC) unclear for this use case
- No pre-approval pathway identified
- Risk of operating outside legal bounds without realizing it

### 4. No Clinical Partnership
- No partnership with a hospital, clinic network, or regulatory body
- Unclear if any organization would endorse or take responsibility

## What Would Be Required to De-Risk
1. **Clinical Validation:** Work with licensed clinicians to test red-flag logic
2. **Legal Review:** Engage health law expert (Nigeria-focused)
3. **Formal Partnership:** Explicit agreement with a clinic/NGO that has liability insurance
4. **Regulatory Engagement:** Contact relevant regulatory bodies
5. **Robust Infrastructure:** Production database, encryption, RBAC, audit logging
6. **Consent & Privacy:** Formal consent process, data retention policy

## Pause Decision
Given the gaps above, continuing without these in place would be **irresponsible**.

The prototype code is sound, but the governance scaffold is not. Law ≠ code; it requires domain experts and partnerships.
