# NaijaCare (Prototype) — WhatsApp-first consult routing, paused for legitimacy constraints

**Status:** paused at prototype stage • **Data:** synthetic only • **Use:** demo / portfolio • **Clinical use:** **NO**

This repository is intentionally modest in code and heavy in documentation: it demonstrates a low-bandwidth consult-routing workflow, *and* the governance constraints that stopped it from becoming anything more.

## What exists (truthfully)
- A small Python package (`src/naijacare`) with:
  - routing + red-flag detection
  - consent gate (prototype)
  - privacy-preserving audit logging (redaction + hashed clinic IDs)
- Two runnable demos:
  - **CLI:** `python prototype/cli.py --fixtures prototype/fixtures/sample_messages.jsonl`
  - **Web UI (Flask):** `python prototype/web/app.py` then open `http://localhost:5000`
- Documentation explaining why the project was paused.

## What does *not* exist
- No WhatsApp Business integration
- No production database
- No real patient data
- No deployment / pilot / approvals / partnerships

## Quickstart

### 1) Install
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
```

### 2) Run the CLI
```bash
python prototype/cli.py --fixtures prototype/fixtures/sample_messages.jsonl
```

### 3) Run the Web UI
```bash
python prototype/web/app.py
# open http://localhost:5000
```

### 4) Export an audit CSV
```bash
python prototype/cli.py --export-audit .audit/audit.csv
```

### 5) Run tests
```bash
pytest
```

See:
- `docs/01_problem_context.md` — Why this problem matters
- `docs/02_architecture.md` — What was built
- `docs/04_risk_legitimacy_memo.md` — What was missing (governance, partnerships, regulatory)
- `docs/05_pause_decision_log.md` — Why it paused (law > code)
- `docs/07_application_alignment.md` — What this teaches about tech policy
