"""Tests for consent validation."""

from datetime import datetime, timedelta

import pytest

from src.naijacare.consent import (
    ConsentRecord,
    ConsentValidationError,
    validate_consent,
)


def test_valid_consent_passes():
    record = ConsentRecord(subject_id="patient-1", age_years=20)
    record.grant({"data_collection", "ai_processing"})

    validate_consent(record, {"data_collection"})


def test_expired_consent_raises():
    record = ConsentRecord(subject_id="patient-1", age_years=20)
    record.grant({"data_collection"})
    record.last_reconsent_at = datetime.utcnow() - timedelta(days=91)

    with pytest.raises(ConsentValidationError):
        validate_consent(record, {"data_collection"})


def test_withdrawn_consent_raises():
    record = ConsentRecord(subject_id="patient-1", age_years=20)
    record.grant({"data_collection"})
    record.withdraw()

    with pytest.raises(ConsentValidationError):
        validate_consent(record, {"data_collection"})


def test_minor_requires_guardian():
    record = ConsentRecord(subject_id="patient-1", age_years=14)
    record.grant({"data_collection"})

    with pytest.raises(ConsentValidationError):
        validate_consent(record, {"data_collection"})
