"""Consent gate (prototype)."""

from .models import Message


def has_consent(msg: Message) -> bool:
    """
    Prototype consent check. In production, this would check an explicit
    consent store keyed by clinic_id.
    
    For this prototype: assumes consent (always returns True).
    """
    # Placeholder: in production, query consent database
    return True
