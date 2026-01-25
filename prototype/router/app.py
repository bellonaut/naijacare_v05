"""
NaijaCare Routing Prototype (Non-clinical)

Simulates WhatsApp-style messages using fixtures.
No real messaging, no patient data.
"""

import json
from pathlib import Path

FIXTURES = Path(__file__).parent.parent / "fixtures" / "sample_messages.jsonl"

def route_message(msg):
    text = msg.get("text", "").lower()
    if any(k in text for k in ["bleeding", "unconscious", "seizure"]):
        return "ESCALATE_IMMEDIATELY"
    if "pain" in text or "fever" in text:
        return "ROUTE_GENERAL"
    return "NON_CLINICAL"

def main():
    print("NaijaCare prototype (simulation)")
    with open(FIXTURES) as f:
        for line in f:
            msg = json.loads(line)
            decision = route_message(msg)
            print(f"[{msg['sender']}] -> {decision}")

if __name__ == "__main__":
    main()
