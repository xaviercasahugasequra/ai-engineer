# seQura AI Agent Challenge

Welcome to seQura's AI Agent code challenge!

This challenge is for candidates applying to the **Senior Backend Engineer – AI Agents** position. It reflects a simplified version of the types of problems we tackle daily at seQura.

Our goal is to evaluate your pragmatism, precision, clarity, ownership, production-readiness, and thoughtful use of tools. A successful candidate is someone who can balance technical skills with strong communication and a product-focused mindset.

---

## Context

At seQura, we're a leading Buy Now Pay Later (BNPL) company that enables shoppers to purchase products at e-commerce stores and pay over time. We partner with thousands of online merchants across various categories.

As part of our AI-powered customer experience initiative, we're developing intelligent agents that help shoppers discover products at our partner merchants and resolve support queries about their existing orders.

This challenge focuses on **building an AI agent system** that demonstrates production-ready orchestration, state management, and integration patterns.

---

## Problem Statement

Your task is to build an **AI-powered shopping assistant** for seQura that handles two main user intents:

1. **Product Discovery** – Help shoppers find e-commerce products at merchants that accept seQura
2. **Customer Support** – Assist shoppers with questions about their existing BNPL orders and payments

The agent must intelligently route between these intents, maintain conversation context, and orchestrate calls to various backend services (simulated as tools).

---

## Scenario Context

seQura enables shoppers to buy products at partner e-commerce stores and pay flexibly:

- **Pay in 3** – Split purchase into 3 interest-free payments
- **Pay in 6/12** – Extended installment plans
- **Pay Later** – Full payment deferred by 7 days

Shoppers interact with the assistant to either:
- **Discover products** – Find items they want to buy at seQura-enabled merchants
- **Get support** – Manage their existing orders (payment status, schedules, issues)

---

## Functional Requirements

### Intent 1: Product Discovery

The agent should help shoppers discover products at seQura partner merchants by:

- Understanding what the shopper is looking for (category, features, price range)
- Searching for products across seQura-enabled merchants
- Providing product details, comparisons, and recommendations
- Showing available payment options for products they're interested in

**Available Tools for Product Discovery:**

| Tool | Description | Input | Output |
|------|-------------|-------|--------|
| `search_products` | Searches for products across merchants | `query`, `category?`, `price_range?` | List of matching products |
| `get_product_details` | Gets detailed product information | `product_id` | Full product info + merchant |
| `get_merchant_info` | Gets merchant details and policies | `merchant_id` | Merchant info + payment options |
| `check_payment_options` | Shows available BNPL options | `product_id`, `user_id?` | Payment plans + eligibility |

### Intent 2: Customer Support

The agent should assist users with existing orders by:

- Retrieving order details and payment status
- Explaining upcoming payments and due dates
- Handling common issues (payment method updates, payment delays)
- Escalating complex issues when necessary

**Available Tools for Customer Support:**

| Tool | Description | Input | Output |
|------|-------------|-------|--------|
| `get_order_details` | Retrieves order information | `order_id` or `user_id` | Order data with status |
| `get_payment_schedule` | Shows remaining payments | `order_id` | List of pending payments |
| `update_payment_method` | Updates payment card | `order_id`, `payment_method` | Confirmation |
| `request_payment_delay` | Requests a payment delay | `order_id`, `days`, `reason` | Approval status |
| `escalate_to_human` | Creates support ticket | `order_id`, `issue_summary` | Ticket ID |

---

## Technical Requirements

### Core Requirements

1. **Agent Orchestration**
   - Implement a conversational agent that manages multi-turn dialogues
   - Handle intent classification and routing between product discovery and support
   - Maintain conversation state and context across turns
   - Implement proper tool/function calling patterns

2. **State Management**
   - Track conversation history and extracted entities
   - Handle context switching between intents gracefully
   - Persist relevant user information across the conversation

3. **Tool Integration**
   - Implement a clean abstraction for tool definitions and execution
   - Handle tool failures gracefully with appropriate fallbacks
   - Validate tool inputs and handle edge cases

4. **Production Readiness**
   - Write comprehensive tests (unit and integration)
   - Implement proper error handling and logging
   - Structure code for maintainability and extensibility
   - Document architectural decisions

### LLM Integration

You may choose one of these approaches:

**Option A: Real LLM Integration**
- Integrate with an LLM API (OpenAI, Anthropic, etc.)
- Implement proper prompt engineering for intent classification and tool calling
- Handle API errors, rate limits, and timeouts

**Option B: Simulated LLM**
- Create a mock LLM that demonstrates the orchestration patterns
- Implement rule-based intent classification
- Focus on the agent architecture and tool orchestration

*Either approach is valid. We're evaluating your backend engineering skills, not prompt engineering.*

---

## Design Questions (Required)

In addition to the implementation, you must document your answers to these design questions in your README. **You do not need to implement the product catalog** – we want to understand your thinking and approach.

### Product Catalog Design

1. **Data Modeling**
   - How would you structure the product catalog to support multiple merchants?
   - What attributes would you store for products, and how would you handle merchant-specific variations?
   - How would you model categories and product relationships?

2. **Search Implementation**
   - How would you implement the `search_products` functionality to handle natural language queries like "laptop for video editing under €1,500"?
   - What search technologies or approaches would you consider (e.g., full-text search, vector embeddings, hybrid)?
   - How would you handle relevance ranking and filtering?

3. **Data Ingestion**
   - How would you keep the catalog synchronized with merchant inventories?
   - What strategies would you use for handling catalog updates at scale (thousands of merchants, millions of products)?

*These questions help us understand your system design thinking. Be concise but thorough – a few paragraphs per question is sufficient.*

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

[Agent calls get_product_details(product_id: "mbp-m3-mediamarkt")]
[Agent calls check_payment_options(product_id: "mbp-m3-mediamarkt")]

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

1. **Source Code**
   - Well-structured, clean, and documented code
   - Clear separation of concerns (agent, tools, state, etc.)

2. **Tests**
   - Unit tests for core components
   - Integration tests for conversation flows
   - Focus on testing edge cases and error scenarios

3. **README**
   - Setup and running instructions
   - Architecture overview and key decisions
   - **Answers to the Design Questions** (Product Catalog section)
   - Known limitations and potential improvements

---

## Evaluation Criteria

| Criteria | Weight | What We Look For |
|----------|--------|------------------|
| **Agent Orchestration** | 25% | Intent handling, context management, tool calling patterns |
| **Code Quality** | 25% | Clean code, SOLID principles, proper abstractions |
| **Testing** | 20% | Test coverage, meaningful tests, edge cases |
| **Design Questions** | 15% | Thoughtful approach to catalog modeling, search, and data ingestion |
| **Production Readiness** | 15% | Error handling, logging, documentation, extensibility |

---

## How to Approach the Challenge

This section explains the mindset and practices we encourage you to adopt while solving the challenge. It's about how you approach the work, communicate your thought process, and align with our values.

1. **Be pragmatic:** Build the **Best Simple System for Now**—a solution that solves the problem effectively while remaining adaptable and easy to iterate on. Avoid overengineering.

2. **Communicate effectively:**
   - Share your thought process, including:
     - Decisions you made and why.
     - Decisions you didn't take and your reasoning.
   - Include your assumptions, trade-offs, and any areas left incomplete due to time constraints.

3. **Demonstrate ownership:**
   - Make decisions confidently and justify them.
   - Ask any question to us (the hiring team) if something is unclear, ideally, as you would to stakeholders in a real-world scenario.

4. **Design, test, develop, document:** Treat this solution as production-ready code. Commit your changes as if this were a real-world feature.
   - You may implement your solution in **any programming language**. While we are most familiar with Ruby, Python, JavaScript, Go, and Java, feel free to use the language you are most comfortable with.
   - Your **experience level will also be taken into consideration** during evaluation.
   - We value clarity, maintainability, and problem-solving over the specific technology used.

5. **AI usage and workflow (optional):**
   If you typically use AI tools (like Copilot, Cursor, etc. for coding, or ChatGPT, Claude, Gemini, etc. for idea refinement and assistance) as part of your workflow, we are happy to see you use them in this challenge as well.

   _Using AI won't give you extra points, and not using it won't count against you either._

   However, if you do choose to use AI, we'd love to understand how you integrated it into your process. Specifically:
   - Which tools you used.
   - The prompts or instructions you provided (sharing a link to the conversation, when available).
   - How you tailored the AI's outputs to your needs.
   - Your reasoning behind using (or not using) AI for specific parts of the challenge.

---

## What We're NOT Evaluating

- **Prompt engineering mastery** – We care about backend architecture, not perfect prompts
- **AI/ML knowledge** – This is a software engineering role, not a data science role
- **UI/Frontend** – A simple CLI or API interface is sufficient
- **Deployment/DevOps** – Focus on the application code

---

## Submission Instructions

When you're done, make sure that you:

1. Created a **README** file explaining:
   - How to set up and run your solution
   - An explanation of your technical choices, trade-offs, and assumptions
   - Answers to the **Design Questions** (Product Catalog section)
   - Areas you would improve given more time
   - _(Optional)_ How you used AI tools, if applicable

2. Included all your code and the `.git` folder in a zip file to show your commit history.

3. Send your submission to your hiring contact.

**Time Expectation:** We recommend spending no more than **6 hours** on this challenge.

*If you run out of time, document what you would have done differently or added in your README.*

---

## Questions?

Please read the challenge carefully before starting. If you have any doubts or need extra info, don't hesitate to ask us before starting.

If anything is unclear during the challenge, make reasonable assumptions and document them in your README. We value seeing how you approach ambiguity.

Good luck! We're excited to see your solution.
