"""Consent validation logic."""

from __future__ import annotations

from datetime import datetime, timedelta

from .tracker import CONSENT_SCOPES, ConsentRecord

RECONSENT_WINDOW_DAYS = 90
MINIMUM_CONSENT_AGE = 16


class ConsentValidationError(ValueError):
    """Raised when consent is invalid or missing."""


def validate_consent(record: ConsentRecord, required_scopes: set[str]) -> None:
    """Validate consent for required scopes.

    Raises:
        ConsentValidationError if consent is missing or invalid.
    """
    if record.age_years < MINIMUM_CONSENT_AGE:
        raise ConsentValidationError("Minor requires guardian consent")

    if record.withdrawn_at is not None:
        raise ConsentValidationError("Consent has been withdrawn")

    if record.consented_at is None:
        raise ConsentValidationError("Consent has not been provided")

    if not required_scopes.issubset(CONSENT_SCOPES):
        raise ConsentValidationError("Unknown consent scope requested")

    if not required_scopes.issubset(record.granted_scopes):
        raise ConsentValidationError("Required consent scope missing")

    last_consent = record.last_reconsent_at or record.consented_at
    if datetime.utcnow() - last_consent > timedelta(days=RECONSENT_WINDOW_DAYS):
        raise ConsentValidationError("Consent expired; re-consent required")
