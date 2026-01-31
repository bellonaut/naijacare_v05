"""Consent audit logging."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class ConsentAuditEntry:
    """Represents a consent audit event."""

    subject_id: str
    action: str
    timestamp: datetime
    details: dict[str, str]


class ConsentAuditLog:
    """In-memory audit log for consent changes."""

    def __init__(self) -> None:
        self._entries: list[ConsentAuditEntry] = []

    def record(self, entry: ConsentAuditEntry) -> None:
        self._entries.append(entry)

    def entries(self) -> list[ConsentAuditEntry]:
        return list(self._entries)
