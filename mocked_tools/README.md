# Mocked Tools

Mock implementations of the product discovery and customer support tools for the seQura AI Agent challenge. Use these so you can focus on agent orchestration and prompt design.

## Usage

From the project root (parent of `mocked_tools/`):

```python
from mocked_tools import (
    search_products,
    get_product_details,
    get_merchant_info,
    check_payment_options,
    get_order_details,
    get_payment_schedule,
    update_payment_method,
    request_payment_delay,
    escalate_to_human,
)

# Product discovery
products = search_products("laptop", category="electronics", price_range={"max": 1500})
details = get_product_details("mba-m3-mediamarkt")
options = check_payment_options("mba-m3-mediamarkt")

# Customer support
order = get_order_details(order_id="SQ-12345")
schedule = get_payment_schedule("SQ-12345")
delay = request_payment_delay("SQ-12345", days=7, reason="user_request")
```

## Interface

| Tool | Input | Output |
|------|--------|--------|
| `search_products` | `query`, `category?`, `price_range?` | List of products |
| `get_product_details` | `product_id` | Product + merchant |
| `get_merchant_info` | `merchant_id` | Merchant + payment options |
| `check_payment_options` | `product_id`, `user_id?` | Payment plans + eligibility |
| `get_order_details` | `order_id` or `user_id` | Order data |
| `get_payment_schedule` | `order_id` | Pending payments |
| `update_payment_method` | `order_id`, `payment_method` | Confirmation |
| `request_payment_delay` | `order_id`, `days`, `reason` | Approval status |
| `escalate_to_human` | `order_id`, `issue_summary` | Ticket ID |

Sample data includes products like "MacBook Air M3" and order "SQ-12345" (Nike Air Max, Pay in 3). You can extend `mocked_tools/data.py` or replace these modules; keep the same tool names and signatures for consistency.
