"""Data models for NaijaCare (Pydantic)."""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Message(BaseModel):
    """Simulated incoming message."""
    sender: str = Field(..., description="Clinic/source ID")
    text: str = Field(..., description="Message content")
    timestamp: Optional[datetime] = None


class RoutingDecision(BaseModel):
    """Routing outcome."""
    decision: str = Field(..., description="ESCALATE_IMMEDIATELY | ROUTE_GENERAL | NON_CLINICAL")
    reason: Optional[str] = None
    flags: list[str] = Field(default_factory=list)


class AuditEntry(BaseModel):
    """Privacy-preserving audit log entry."""
    clinic_id_hash: str
    decision: str
    timestamp: datetime
    message_length: int
    has_emergency_flag: bool
