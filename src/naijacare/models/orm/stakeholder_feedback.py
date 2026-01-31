"""Stakeholder feedback ORM model."""

from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .mixins import TimestampMixin
from ..database import Base


class StakeholderFeedback(Base, TimestampMixin):
    """Interview data schema."""

    __tablename__ = "stakeholder_feedback"

    id: Mapped[int] = mapped_column(primary_key=True)
    field_note_id: Mapped[int] = mapped_column(ForeignKey("field_notes.id"))
    stakeholder_name: Mapped[str] = mapped_column(String(120))
    organization: Mapped[str | None] = mapped_column(String(120))
    feedback: Mapped[str] = mapped_column(String(500))

    field_note: Mapped["FieldNote"] = relationship(back_populates="stakeholder_feedback")
