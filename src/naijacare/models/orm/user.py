"""User ORM model for RBAC."""

from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .mixins import SoftDeleteMixin, TimestampMixin
from ..database import Base


class User(Base, TimestampMixin, SoftDeleteMixin):
    """Admin/reviewer/stakeholder accounts."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    full_name: Mapped[str | None] = mapped_column(String(120))
    role: Mapped[str] = mapped_column(String(32), default="reviewer")

    reviewed_decisions: Mapped[list["RoutingDecision"]] = relationship(
        back_populates="reviewer"
    )
    field_notes: Mapped[list["FieldNote"]] = relationship(
        back_populates="author", cascade="all, delete-orphan"
    )
