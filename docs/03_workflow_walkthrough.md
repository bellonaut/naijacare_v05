# Workflow Walkthrough (Prototype)

This walkthrough expands on how the prototype behaves end-to-end while keeping the same governance boundary: it is a demo of logic, not a deployable clinical system.

## 1) Intake and Context
- A clinic operator enters a message (from fixtures or custom text) in the demo UI.
- The sender field acts as a stand-in clinic identifier (e.g., `clinic_sokoto`).
- Timestamps are generated at runtime to simulate live intake.

## 2) Routing Logic
Routing decisions are intentionally simple and keyword-driven to keep the prototype transparent:
- **ESCALATE_IMMEDIATELY** when emergency keywords are detected.
- **ROUTE_GENERAL** for non-emergency clinical messages.
- **NON_CLINICAL** for logistics, greetings, or unrelated text.

The goal is to illustrate the flow and auditability, not to claim clinical accuracy.

## 3) Outcome Presentation
- The UI displays the routing decision, the rationale, and any red-flag keywords.
- Session statistics summarize how many decisions have been made and how many escalations occurred.

## 4) Audit Trail (Privacy-Preserving)
Each interaction produces an audit entry that logs:
- Hashed clinic ID
- Decision category
- Message length
- Emergency flag

Raw message text is never stored in the audit log.

## 5) Non-Goals (Deliberate Limits)
- No real patient enrollment or consent database
- No clinician review or validation
- No regulatory approvals or production infrastructure

This is a controlled demonstration of how a low-bandwidth routing workflow could be represented—paired with documentation that explains why it stopped where it did.
