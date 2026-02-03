# seQura AI Agent Challenge

Code challenge for the **Senior Backend Engineer – AI Agents** position. We evaluate pragmatism, clarity, ownership, and production-readiness. **Time budget:** ~6 hours.

---

## Context & Problem

seQura is a Buy Now Pay Later (BNPL) company: shoppers buy at partner e-commerce stores and pay flexibly (Pay in 3, Pay in 6/12, Pay Later). Your task is to build an **AI-powered shopping assistant** that:

1. **Product Discovery** – Helps shoppers find products at seQura-enabled merchants (search, details, payment options).
2. **Customer Support** – Helps with existing orders (status, payment schedule, delays, payment method updates, escalation).

The agent must route between these intents, keep conversation context, and call backend services via the tools below (mocked implementations provided).

---

## Tools & Functional Scope

### Product Discovery

| Tool                    | Description                            | Input                                | Output                          |
| ----------------------- | -------------------------------------- | ------------------------------------ | ------------------------------- |
| `search_products`       | Searches for products across merchants | `query`, `category?`, `price_range?` | List of matching products       |
| `get_product_details`   | Gets detailed product information      | `product_id`                         | Full product info + merchant    |
| `get_merchant_info`     | Gets merchant details and policies     | `merchant_id`                        | Merchant info + payment options |
| `check_payment_options` | Shows available BNPL options           | `product_id`, `user_id?`             | Payment plans + eligibility     |

### Customer Support

| Tool                    | Description                 | Input                        | Output                   |
| ----------------------- | --------------------------- | ---------------------------- | ------------------------ |
| `get_order_details`     | Retrieves order information | `order_id` or `user_id`      | Order data with status   |
| `get_payment_schedule`  | Shows remaining payments    | `order_id`                   | List of pending payments |
| `update_payment_method` | Updates payment card        | `order_id`, `payment_method` | Confirmation             |
| `request_payment_delay` | Requests a payment delay    | `order_id`, `days`, `reason` | Approval status          |
| `escalate_to_human`     | Creates support ticket      | `order_id`, `issue_summary`  | Ticket ID                |

Use the **mocked tools** in `mocked_tools/` (Python) so you can focus on the agent; see `mocked_tools/README.md` for usage. You may extend or replace them; keep tool names and signatures consistent.

---

## Technical Requirements

- **Agent:** Multi-turn conversational agent; intent classification and routing; conversation state; tool/function calling.
- **Tools:** Use the provided mocked tools; clean abstraction for definitions and execution; handle failures and validate inputs.
- **LLM:** Integrate a **real LLM API** (OpenAI, Anthropic, etc.). We care about how you design prompts for intent and tool use. Handle errors, rate limits, timeouts. **Use your own API key;** we don’t provide one (mention if it’s a blocker).
- **Deliverables:** Tests, error handling, logging, maintainable structure, and a **technical decision document** (ADR or README section) with your solution rationale and trade-offs.

---

## Design Questions (Required)

Document your answers in the README (see Deliverables). **No need to implement the catalog**—we want your reasoning only.

1. **Data modeling** – How would you structure the product catalog for multiple merchants? Attributes, merchant-specific variations, categories and relationships?
2. **Search** – How would you implement `search_products` for queries like "laptop for video editing under €1,500"? Technologies (full-text, vectors, hybrid), ranking, filtering?
3. **Data ingestion** – How would you keep the catalog in sync with merchant inventories? Strategies for updates at scale (many merchants, many products)?

---

## Sample Conversations

### Product Discovery Flow

```
User: I'm looking for a new laptop for video editing, budget around €1,500

Agent: I'd be happy to help you find a laptop for video editing! Let me search our partner merchants.

[Agent calls search_products(query: "laptop video editing", category: "electronics", price_range: {max: 1500})]

Agent: I found several options for you:

1. **MacBook Air M3** - €1,299 at MediaMarkt
2. **ASUS ProArt Studiobook** - €1,449 at PcComponentes
3. **Dell XPS 15** - €1,399 at El Corte Inglés

Would you like more details on any of these?

User: Tell me more about the MacBook

[Agent calls get_product_details(product_id: "mba-m3-mediamarkt")]
[Agent calls check_payment_options(product_id: "mba-m3-mediamarkt")]

Agent: **MacBook Air M3** at MediaMarkt
- 15" Liquid Retina display
- Apple M3 chip, 16GB RAM, 512GB SSD
- Price: €1,299

**Payment options with seQura:**
- Pay in 3: 3 × €433 (interest-free)
- Pay in 6: 6 × €220 (1.5% fee)

Would you like me to help you proceed with this purchase?
```

### Customer Support Flow

```
User: I need help with my order

Agent: I'd be happy to help with your order. Could you provide your order number, or would you like me to look up your recent orders?

User: Order SQ-12345

[Agent calls get_order_details(order_id: "SQ-12345")]

Agent: I found your order SQ-12345:
- Product: Nike Air Max 90 (Size 42)
- Merchant: Foot Locker
- Purchase date: Nov 20, 2024
- Total: €150 (Pay in 3)
- Status: 1 of 3 payments completed (€50 paid)

What would you like help with?

User: I need to delay my next payment, I had unexpected expenses

[Agent calls get_payment_schedule(order_id: "SQ-12345")]
[Agent calls request_payment_delay(order_id: "SQ-12345", days: 7, reason: "user_request")]

Agent: I understand. I've submitted a request to delay your next payment of €50 (originally due Dec 20) by 7 days.

Your new due date would be Dec 27. You'll receive a confirmation email shortly.

Is there anything else I can help you with?
```

---

## Deliverables

- **Code** – Python, clear structure (agent / tools / state), use the provided mocked tools.
- **Technical decision document** – Why you chose your solution, trade-offs, alternatives (ADR or README section).
- **Tests** – Unit and integration (including conversation flows and edge cases).
- **README** – Setup and run instructions; architecture and key decisions; **answers to the Design Questions**; limitations and improvements.

---

## Evaluation Criteria

| Criteria                 | Weight | What We Look For                                                    |
| ------------------------ | ------ | ------------------------------------------------------------------- |
| **Agent Orchestration**  | 25%    | Intent handling, context management, tool calling patterns          |
| **Design Questions**     | 25%    | Thoughtful approach to catalog modeling, search, and data ingestion |
| **Code Quality**         | 20%    | Clean code, SOLID principles, proper abstractions                   |
| **Production Readiness** | 15%    | Error handling, logging, documentation, extensibility               |
| **Testing**              | 15%    | Test coverage, meaningful tests, edge cases                          |

### How We Evaluate Chat Responses

We assess the agent’s replies along these dimensions:

- **Intent routing** – Correct classification (product discovery vs support) and appropriate tool use.
- **Relevance** – Answers address the user’s question and use tool results meaningfully.
- **Clarity** – Responses are concise, structured, and easy to follow (e.g. lists, payment breakdowns).
- **Completeness** – All needed info is surfaced (e.g. payment options when discussing a product; next due date when discussing delays).
- **Graceful degradation** – Sensible behaviour when tools fail, inputs are missing, or the request is ambiguous (e.g. asking for order ID when only `user_id` is given).

---

## How to Approach

- **Pragmatic** – Best simple system for now; avoid overengineering.
- **Communicate** – Share decisions (taken and not), assumptions, trade-offs, and what you’d do with more time.
- **Ownership** – Decide and justify; ask us if anything is unclear.
- **Python preferred;** use the provided mocked tools. We value clarity and problem-solving.
- **AI tools (optional)** – You may use Copilot, Cursor, ChatGPT, etc. It won’t affect scoring. If you do, briefly describe how you used them and tailored the output.

---

## What We're NOT Evaluating

- **AI/ML knowledge** – This is a software engineering role, not a data science role
- **UI/Frontend** – A simple CLI or API interface is sufficient
- **Deployment/DevOps** – Focus on the application code

---

## Submission

Zip your code **including the `.git` folder** and send to your hiring contact. If you run out of time, document next steps in the README. Questions? Ask us; if you assume something, document it.
