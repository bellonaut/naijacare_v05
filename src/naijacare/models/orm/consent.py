"""Consent record ORM model."""

from __future__ import annotations

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .mixins import SoftDeleteMixin, TimestampMixin
from ..database import Base


class ConsentRecord(Base, TimestampMixin, SoftDeleteMixin):
    """Consent records with versioning and withdrawal."""

    __tablename__ = "consent_records"

    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"), nullable=False)
    consent_version: Mapped[str] = mapped_column(String(16), default="v1")
    scope_data_collection: Mapped[bool] = mapped_column(default=False)
    scope_ai_processing: Mapped[bool] = mapped_column(default=False)
    scope_third_party: Mapped[bool] = mapped_column(default=False)
    consented_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), default=None)
    withdrawn_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), default=None)

    patient: Mapped["Patient"] = relationship(back_populates="consents")
