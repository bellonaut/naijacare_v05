"""Audit logging (privacy-preserving)."""

from datetime import datetime
from .models import AuditEntry
from .privacy import hash_clinic_id


class AuditLog:
    """In-memory audit store (prototype)."""
    
    def __init__(self):
        self.entries = []
    
    def log(self, clinic_id: str, decision: str, message_text: str, has_emergency: bool):
        """Log a routing decision without storing raw message content."""
        entry = AuditEntry(
            clinic_id_hash=hash_clinic_id(clinic_id),
            decision=decision,
            timestamp=datetime.now(),
            message_length=len(message_text),
            has_emergency_flag=has_emergency
        )
        self.entries.append(entry)
    
    def to_list(self):
        """Export audit entries as list of dicts."""
        return [e.model_dump() for e in self.entries]
