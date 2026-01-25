"""Privacy-preserving transformations."""

import hashlib


def hash_clinic_id(clinic_id: str) -> str:
    """
    One-way hash of clinic identifier.
    Used in audit logs to avoid storing raw clinic IDs.
    """
    return hashlib.sha256(clinic_id.encode()).hexdigest()[:16]


def redact_message_text(text: str, max_length: int = 20) -> str:
    """
    Truncate message text in logs to avoid storing sensitive content.
    """
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text
