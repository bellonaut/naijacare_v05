"""Field note ORM model."""

from __future__ import annotations

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .mixins import TimestampMixin
from ..database import Base


class FieldNote(Base, TimestampMixin):
    """Structured Sokoto observations."""

    __tablename__ = "field_notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    visit_date: Mapped[Date]
    location: Mapped[str] = mapped_column(String(120))
    summary: Mapped[str] = mapped_column(String(255))
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    author: Mapped["User"] = relationship(back_populates="field_notes")
    stakeholder_feedback: Mapped[list["StakeholderFeedback"]] = relationship(
        back_populates="field_note", cascade="all, delete-orphan"
    )
