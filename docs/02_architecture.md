# Architecture

## High-Level Workflow
```
Patient (via WhatsApp)
    ↓
Clinic Operator (text message)
    ↓
Message Queue / Router
    ↓
Red-Flag Detection (keywords: "bleeding", "unconscious", etc.)
    ↓
Decision: [ESCALATE_IMMEDIATELY | ROUTE_GENERAL | NON_CLINICAL]
    ↓
Audit Log (hashed clinic IDs, message length only, no raw text)
    ↓
Response (async, via WhatsApp or other channel)
```

## Package Structure
```
src/naijacare/
├── models.py          # Pydantic models (Message, RoutingDecision, AuditEntry)
├── routing.py         # Red-flag logic + routing decisions
├── consent.py         # Consent gate (prototype: always True)
├── privacy.py         # Hash clinic IDs, redact message text
├── audit.py           # Privacy-preserving audit log
└── __init__.py
```

## Key Design Choices
1. **Privacy-First Audit:** Clinic IDs are hashed, messages are never stored in full
2. **Stateless Routing:** No database required; can run in-memory or on-device
3. **Consent Gate:** Checks (prototype) that clinic has opted in
4. **Simulated Data:** All fixtures are synthetic; no real patient data

## Decision Taxonomy (Prototype)
- **ESCALATE_IMMEDIATELY:** emergency keywords detected (red-flag terms)
- **ROUTE_GENERAL:** clinical but non-emergency
- **NON_CLINICAL:** logistics, greetings, or unrelated messages

## Audit Entry Schema (Privacy-Preserving)
Each audit entry captures minimal metadata for accountability:
- `clinic_id_hash`
- `decision`
- `timestamp`
- `message_length`
- `has_emergency_flag`

No raw message content or patient identifiers are stored.

## Prototype Interfaces
- **CLI** (`prototype/cli.py`): route fixture messages, export audit CSV
- **Web UI** (`prototype/web/app.py`): demo routing decisions, view stats, view audit log

## What's *Not* Built
- WhatsApp Business API integration (would require credentials & compliance)
- Production database (SQLAlchemy, migration tools)
- Real clinical training, approvals, partnerships
- Deployment infrastructure (Docker, cloud hosting, CI/CD beyond basic tests)

## Scope Boundary
This prototype is intentionally minimal:
- Demonstrates workflow logic
- Shows governance concerns (audit, consent, privacy)
- **Does not** claim readiness for pilot, partnership, or clinical use
