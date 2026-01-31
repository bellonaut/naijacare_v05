"""Consent management package."""

from .audit import ConsentAuditEntry, ConsentAuditLog
from .tracker import CONSENT_SCOPES, ConsentRecord, ConsentStore
from .validator import ConsentValidationError, validate_consent
from .withdrawal import withdraw_and_anonymize

__all__ = [
    "CONSENT_SCOPES",
    "ConsentAuditEntry",
    "ConsentAuditLog",
    "ConsentRecord",
    "ConsentStore",
    "ConsentValidationError",
    "validate_consent",
    "withdraw_and_anonymize",
]
