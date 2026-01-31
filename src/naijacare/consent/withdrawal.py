"""Right-to-be-forgotten flows."""

from __future__ import annotations

from datetime import datetime

from .tracker import ConsentRecord


def withdraw_and_anonymize(record: ConsentRecord, withdrawn_at: datetime | None = None) -> None:
    """Withdraw consent and anonymize personal data in the record."""
    record.withdraw(withdrawn_at)
    record.anonymize()
