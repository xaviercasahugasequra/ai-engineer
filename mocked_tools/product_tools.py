"""Mocked product discovery tools."""

from typing import Any, Optional

from .data import MERCHANTS, PRODUCTS


def search_products(
    query: str,
    category: Optional[str] = None,
    price_range: Optional[dict[str, Any]] = None,
) -> list[dict[str, Any]]:
    """
    Searches for products across merchants.

    Args:
        query: Search text (e.g. "laptop video editing").
        category: Optional category filter (e.g. "electronics").
        price_range: Optional dict with "min" and/or "max" (numeric).

    Returns:
        List of matching products (id, name, merchant_id, category, price, currency).
    """
    results = []
    max_price = price_range.get("max") if price_range and isinstance(price_range, dict) else None
    q_lower = query.lower()

    for p in PRODUCTS:
        if category and p["category"] != category:
            continue
        if max_price is not None and p["price"] > max_price:
            continue
        if q_lower in p["name"].lower() or q_lower in p["description"].lower():
            results.append(
                {
                    "id": p["id"],
                    "name": p["name"],
                    "merchant_id": p["merchant_id"],
                    "category": p["category"],
                    "price": p["price"],
                    "currency": p["currency"],
                }
            )

    if not results:
        results = [
            {
                "id": p["id"],
                "name": p["name"],
                "merchant_id": p["merchant_id"],
                "category": p["category"],
                "price": p["price"],
                "currency": p["currency"],
            }
            for p in PRODUCTS
        ][:5]

    return results


def get_product_details(product_id: str) -> dict[str, Any] | None:
    """
    Gets detailed product information.

    Args:
        product_id: Product identifier.

    Returns:
        Full product info plus merchant name, or None if not found.
    """
    for p in PRODUCTS:
        if p["id"] == product_id:
            merchant = MERCHANTS.get(p["merchant_id"], {})
            return {
                **p,
                "merchant_name": merchant.get("name", p["merchant_id"]),
            }
    return None


def get_merchant_info(merchant_id: str) -> dict[str, Any] | None:
    """
    Gets merchant details and policies.

    Args:
        merchant_id: Merchant identifier.

    Returns:
        Merchant info and payment options, or None if not found.
    """
    return MERCHANTS.get(merchant_id)


def check_payment_options(
    product_id: str,
    user_id: Optional[str] = None,
) -> dict[str, Any] | None:
    """
    Shows available BNPL options for a product.

    Args:
        product_id: Product identifier.
        user_id: Optional user ID for eligibility.

    Returns:
        Payment plans and eligibility, or None if product not found.
    """
    details = get_product_details(product_id)
    if not details:
        return None
    merchant = MERCHANTS.get(details["merchant_id"])
    if not merchant:
        return None
    price = details["price"]
    return {
        "product_id": product_id,
        "price": price,
        "currency": details["currency"],
        "merchant_name": details.get("merchant_name", details["merchant_id"]),
        "plans": [
            {"name": "Pay in 3", "installments": 3, "amount_per": round(price / 3, 2), "fee": "interest-free"},
            {"name": "Pay in 6", "installments": 6, "amount_per": round(price / 6 * 1.015, 2), "fee": "1.5%"},
        ],
        "eligible": True,
    }
