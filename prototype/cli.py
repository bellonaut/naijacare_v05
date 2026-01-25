"""
NaijaCare CLI Demo (Non-clinical prototype)

Simulates WhatsApp-style messages using fixtures.
No real messaging, no patient data.
"""

import json
import csv
import sys
from pathlib import Path
import argparse

# Add src/ to path for importing naijacare
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.naijacare.models import Message
from src.naijacare.routing import route_message
from src.naijacare.audit import AuditLog
from src.naijacare.privacy import hash_clinic_id

FIXTURES = Path(__file__).parent / "fixtures" / "sample_messages.jsonl"


def load_fixtures(path):
    """Load sample messages from JSONL."""
    messages = []
    with open(path) as f:
        for line in f:
            data = json.loads(line)
            messages.append(Message(**data))
    return messages


def main():
    parser = argparse.ArgumentParser(description="NaijaCare routing CLI demo")
    parser.add_argument("--fixtures", default=str(FIXTURES), help="Path to JSONL fixtures")
    parser.add_argument("--export-audit", help="Export audit log to CSV")
    args = parser.parse_args()

    audit_log = AuditLog()
    
    print("NaijaCare prototype (simulation)\n")
    messages = load_fixtures(args.fixtures)
    
    for msg in messages:
        decision = route_message(msg)
        is_emergency = decision.decision == "ESCALATE_IMMEDIATELY"
        
        # Log to audit (privacy-preserving)
        audit_log.log(
            clinic_id=msg.sender,
            decision=decision.decision,
            message_text=msg.text,
            has_emergency=is_emergency
        )
        
        # Display output
        print(f"[{msg.sender}] {msg.text}")
        print(f"  → {decision.decision} | Reason: {decision.reason}")
        if decision.flags:
            print(f"  → Flags: {', '.join(decision.flags)}")
        print()
    
    # Export audit if requested
    if args.export_audit:
        export_path = Path(args.export_audit)
        export_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(export_path, 'w', newline='') as f:
            fieldnames = ["clinic_id_hash", "decision", "timestamp", "message_length", "has_emergency_flag"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for entry in audit_log.entries:
                writer.writerow(entry.model_dump())
        
        print(f"Audit log exported to: {export_path}")


if __name__ == "__main__":
    main()
