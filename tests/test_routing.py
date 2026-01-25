"""Tests for routing logic."""

import pytest
from src.naijacare.models import Message
from src.naijacare.routing import route_message


def test_emergency_escalation():
    """Test that emergency keywords trigger escalation."""
    msg = Message(sender="clinic_001", text="Patient unconscious after fall")
    decision = route_message(msg)
    assert decision.decision == "ESCALATE_IMMEDIATELY"
    assert "unconscious" in decision.flags


def test_general_routing():
    """Test that general symptoms route normally."""
    msg = Message(sender="clinic_001", text="Patient has fever and weakness")
    decision = route_message(msg)
    assert decision.decision == "ROUTE_GENERAL"


def test_non_clinical():
    """Test that non-clinical messages are marked as such."""
    msg = Message(sender="clinic_001", text="Hello, testing system")
    decision = route_message(msg)
    assert decision.decision == "NON_CLINICAL"
