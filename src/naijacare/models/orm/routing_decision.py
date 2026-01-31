"""Routing decision ORM model."""

from __future__ import annotations

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .mixins import TimestampMixin
from ..database import Base


class RoutingDecision(Base, TimestampMixin):
    """Audit trail for routing decisions."""

    __tablename__ = "routing_decisions"

    id: Mapped[int] = mapped_column(primary_key=True)
    case_id: Mapped[int] = mapped_column(ForeignKey("cases.id"), nullable=False)
    method: Mapped[str] = mapped_column(String(32), default="keyword")
    outcome: Mapped[str] = mapped_column(String(64))
    decided_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), default=None)
    reviewer_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))

    case: Mapped["Case"] = relationship(back_populates="routing_decisions")
    reviewer: Mapped["User"] = relationship(back_populates="reviewed_decisions")
