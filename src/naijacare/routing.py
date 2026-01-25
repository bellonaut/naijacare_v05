"""Routing logic with red-flag detection (non-clinical prototype)."""

from .models import Message, RoutingDecision


RED_FLAGS = ["bleeding", "unconscious", "seizure", "unresponsive", "severe"]


def route_message(msg: Message) -> RoutingDecision:
    """
    Route a simulated message.
    
    Args:
        msg: Incoming Message object
        
    Returns:
        RoutingDecision with decision and flags
        
    NOTE: This is prototype code. Red-flag lists and logic are simulated,
    not clinical guidance.
    """
    text = msg.text.lower()
    flags = [flag for flag in RED_FLAGS if flag in text]
    
    if flags:
        return RoutingDecision(
            decision="ESCALATE_IMMEDIATELY",
            reason="Emergency red-flag detected",
            flags=flags
        )
    elif any(k in text for k in ["pain", "fever", "cough", "weakness"]):
        return RoutingDecision(
            decision="ROUTE_GENERAL",
            reason="General symptoms",
            flags=[]
        )
    else:
        return RoutingDecision(
            decision="NON_CLINICAL",
            reason="No clinical keywords",
            flags=[]
        )
