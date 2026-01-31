# Meta Europe Data Storage Conflict

**Date**: 2025-09-08  
**Prepared by**: Legal Research (NaijaCare)

## Summary
Meta’s WhatsApp Business API infrastructure currently routes message payloads
through EU-based data centers. Nigerian data sovereignty guidance (NITDA NDPR
and sectoral healthcare directives) strongly prefers local or regionally
approved storage for health-related data. This creates a conflict for any
pipeline that processes patient content outside Nigeria.

## Findings
- Meta’s contractual language does not guarantee Nigeria-only processing.
- Cross-border transfer clauses require explicit patient consent and legal
  safeguards that NaijaCare cannot currently implement end-to-end.
- Legal counsel recommends pausing any production deployment until a Nigerian
  data residency option or approved Standard Contractual Clauses are available.

## Impact
- Blocks production integration with WhatsApp API for clinical use cases.
- Requires alternative data channels or data localization commitments.
