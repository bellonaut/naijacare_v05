"""Consent status persistence helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Iterable


CONSENT_SCOPES = {"data_collection", "ai_processing", "third_party_sharing"}


@dataclass
class ConsentRecord:
    """Represents a user's consent state."""

    subject_id: str
    age_years: int
    granted_scopes: set[str] = field(default_factory=set)
    consented_at: datetime | None = None
    withdrawn_at: datetime | None = None
    last_reconsent_at: datetime | None = None
    consent_version: str = "v1"
    metadata: dict[str, str] = field(default_factory=dict)

    def grant(self, scopes: Iterable[str], consented_at: datetime | None = None) -> None:
        self.granted_scopes.update(scopes)
        self.consented_at = consented_at or datetime.utcnow()
        self.last_reconsent_at = self.consented_at

    def withdraw(self, withdrawn_at: datetime | None = None) -> None:
        self.withdrawn_at = withdrawn_at or datetime.utcnow()

    def anonymize(self) -> None:
        self.subject_id = "ANONYMIZED"
        self.metadata.clear()


class ConsentStore:
    """In-memory consent store for prototype workflows."""

    def __init__(self) -> None:
        self._records: dict[str, ConsentRecord] = {}

    def upsert(self, record: ConsentRecord) -> None:
        self._records[record.subject_id] = record

    def get(self, subject_id: str) -> ConsentRecord | None:
        return self._records.get(subject_id)

    def withdraw(self, subject_id: str, withdrawn_at: datetime | None = None) -> ConsentRecord | None:
        record = self._records.get(subject_id)
        if record:
            record.withdraw(withdrawn_at)
        return record
