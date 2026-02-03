"""Mocked customer support tools."""

from typing import Any

from .data import ORDERS, PAYMENT_SCHEDULES


def get_order_details(order_id: str | None = None, user_id: str | None = None) -> dict[str, Any] | None:
    """
    Retrieves order information by order_id or user_id.

    Args:
        order_id: Order identifier (e.g. "SQ-12345").
        user_id: User identifier; returns most recent order if no order_id.

    Returns:
        Order data with status, or None if not found.
    """
    if order_id and order_id in ORDERS:
        return ORDERS[order_id]
    if user_id:
        for o in ORDERS.values():
            if o.get("user_id") == user_id:
                return o
    return None


def get_payment_schedule(order_id: str) -> list[dict[str, Any]] | None:
    """
    Shows remaining payments for an order.

    Args:
        order_id: Order identifier.

    Returns:
        List of pending payments (due_date, amount, status), or None if not found.
    """
    if order_id not in ORDERS:
        return None
    return PAYMENT_SCHEDULES.get(order_id, [])


def update_payment_method(order_id: str, payment_method: str) -> dict[str, Any] | None:
    """
    Updates the payment card for an order.

    Args:
        order_id: Order identifier.
        payment_method: New payment method identifier or description.

    Returns:
        Confirmation dict, or None if order not found.
    """
    if order_id not in ORDERS:
        return None
    return {
        "order_id": order_id,
        "updated": True,
        "message": f"Payment method updated to {payment_method}.",
    }


def request_payment_delay(order_id: str, days: int, reason: str) -> dict[str, Any] | None:
    """
    Requests a payment delay for an order.

    Args:
        order_id: Order identifier.
        days: Number of days to delay.
        reason: Reason code or description.

    Returns:
        Approval status, or None if order not found.
    """
    if order_id not in ORDERS:
        return None
    schedule = PAYMENT_SCHEDULES.get(order_id, [])
    next_payment = schedule[0] if schedule else {}
    return {
        "order_id": order_id,
        "approved": True,
        "days_delay": days,
        "original_due_date": next_payment.get("due_date"),
        "new_due_date": "2024-12-27",
        "message": "Delay request submitted. You will receive a confirmation email.",
    }


def escalate_to_human(order_id: str, issue_summary: str) -> dict[str, Any] | None:
    """
    Creates a support ticket for human handling.

    Args:
        order_id: Order identifier.
        issue_summary: Summary of the issue.

    Returns:
        Ticket ID and status, or None if invalid.
    """
    if order_id not in ORDERS:
        return None
    ticket_id = f"TKT-{order_id}-001"
    return {
        "ticket_id": ticket_id,
        "order_id": order_id,
        "status": "created",
        "message": f"Support ticket {ticket_id} created. Our team will follow up shortly.",
    }
