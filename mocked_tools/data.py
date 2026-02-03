"""Mock data for product discovery and customer support tools."""

PRODUCTS = [
    {
        "id": "mba-m3-mediamarkt",
        "name": "MacBook Air M3",
        "merchant_id": "mediamarkt",
        "category": "electronics",
        "price": 1299,
        "currency": "EUR",
        "description": "Laptop - 15\" Liquid Retina display, Apple M3 chip, 16GB RAM, 512GB SSD",
    },
    {
        "id": "asus-proart-pccomponentes",
        "name": "ASUS ProArt Studiobook",
        "merchant_id": "pccomponentes",
        "category": "electronics",
        "price": 1449,
        "currency": "EUR",
        "description": "Laptop for content creation and video editing, high color accuracy",
    },
    {
        "id": "dell-xps-elcorteingles",
        "name": "Dell XPS 15",
        "merchant_id": "elcorteingles",
        "category": "electronics",
        "price": 1399,
        "currency": "EUR",
        "description": "Laptop - 15.6\" OLED, Intel i7, 32GB RAM, 1TB SSD",
    },
]

MERCHANTS = {
    "mediamarkt": {
        "id": "mediamarkt",
        "name": "MediaMarkt",
        "payment_options": ["pay_in_3", "pay_in_6", "pay_later"],
    },
    "pccomponentes": {
        "id": "pccomponentes",
        "name": "PcComponentes",
        "payment_options": ["pay_in_3", "pay_in_6", "pay_in_12"],
    },
    "elcorteingles": {
        "id": "elcorteingles",
        "name": "El Corte Inglés",
        "payment_options": ["pay_in_3", "pay_in_6", "pay_later"],
    },
}

ORDERS = {
    "SQ-12345": {
        "order_id": "SQ-12345",
        "user_id": "user-001",
        "product": "Nike Air Max 90 (Size 42)",
        "merchant_id": "footlocker",
        "merchant_name": "Foot Locker",
        "purchase_date": "2024-11-20",
        "total": 150,
        "currency": "EUR",
        "plan": "pay_in_3",
        "installment_amount": 50,
        "payments_completed": 1,
        "status": "active",
    },
}

PAYMENT_SCHEDULES = {
    "SQ-12345": [
        {"due_date": "2024-12-20", "amount": 50, "status": "pending"},
        {"due_date": "2025-01-20", "amount": 50, "status": "pending"},
    ],
}
