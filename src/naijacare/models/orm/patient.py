"""Patient ORM model."""

from __future__ import annotations

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .mixins import SoftDeleteMixin, TimestampMixin
from ..database import Base


class Patient(Base, TimestampMixin, SoftDeleteMixin):
    """Represents a patient profile."""

    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True)
    external_reference: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    preferred_name: Mapped[str | None] = mapped_column(String(120))
    age_years: Mapped[int | None]
    gender: Mapped[str | None] = mapped_column(String(32))

    cases: Mapped[list["Case"]] = relationship(
        back_populates="patient", cascade="all, delete-orphan"
    )
    consents: Mapped[list["ConsentRecord"]] = relationship(
        back_populates="patient", cascade="all, delete-orphan"
    )
