"""Case/encounter ORM model."""

from __future__ import annotations

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .mixins import SoftDeleteMixin, TimestampMixin
from ..database import Base


class Case(Base, TimestampMixin, SoftDeleteMixin):
    """Represents a routed case/encounter."""

    __tablename__ = "cases"

    id: Mapped[int] = mapped_column(primary_key=True)
    patient_id: Mapped[int] = mapped_column(ForeignKey("patients.id"), nullable=False)
    status: Mapped[str] = mapped_column(String(32), default="open")
    opened_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), default=None)
    summary: Mapped[str | None] = mapped_column(String(255))

    patient: Mapped["Patient"] = relationship(back_populates="cases")
    routing_decisions: Mapped[list["RoutingDecision"]] = relationship(
        back_populates="case", cascade="all, delete-orphan"
    )
