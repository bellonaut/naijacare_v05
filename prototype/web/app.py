"""
NaijaCare Web UI (Flask) — Non-clinical prototype demo

Provides a minimal interface to route simulated messages.
"""

import sys
import json
from pathlib import Path
from datetime import datetime

from flask import Flask, render_template, request, jsonify

# Add src/ to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.naijacare.models import Message
from src.naijacare.routing import route_message
from src.naijacare.audit import AuditLog
from src.naijacare.privacy import hash_clinic_id

app = Flask(__name__, template_folder="templates", static_folder="static")
audit_log = AuditLog()

# Load fixtures
FIXTURES = Path(__file__).parent.parent / "fixtures" / "sample_messages.jsonl"

def load_fixtures():
    """Load sample messages."""
    messages = []
    with open(FIXTURES) as f:
        for line in f:
            data = json.loads(line)
            messages.append(data)
    return messages


@app.route("/")
def index():
    """Render main page."""
    fixtures = load_fixtures()
    return render_template("index.html", samples=fixtures)


@app.route("/api/route", methods=["POST"])
def api_route():
    """Route a message and return decision."""
    data = request.json
    msg = Message(
        sender=data.get("sender", "unknown"),
        text=data.get("text", ""),
        timestamp=datetime.now()
    )
    
    decision = route_message(msg)
    is_emergency = decision.decision == "ESCALATE_IMMEDIATELY"
    
    # Log to audit
    audit_log.log(
        clinic_id=msg.sender,
        decision=decision.decision,
        message_text=msg.text,
        has_emergency=is_emergency
    )
    
    return jsonify({
        "decision": decision.decision,
        "reason": decision.reason,
        "flags": decision.flags
    })


@app.route("/api/audit")
def api_audit():
    """Return audit log (privacy-preserving)."""
    return jsonify(audit_log.to_list())


@app.route("/api/stats")
def api_stats():
    """Return session statistics."""
    decisions = {}
    for entry in audit_log.entries:
        decisions[entry.decision] = decisions.get(entry.decision, 0) + 1
    
    return jsonify({
        "total_messages": len(audit_log.entries),
        "decisions": decisions,
        "emergency_count": sum(1 for e in audit_log.entries if e.has_emergency_flag)
    })


if __name__ == "__main__":
    print("NaijaCare Web UI (Non-clinical prototype)")
    print("Starting on http://localhost:5000")
    app.run(debug=True, host="127.0.0.1", port=5000)
