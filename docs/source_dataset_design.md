# Source Dataset Design

## Dataset Overview

The dataset represents transactional order data from five e-commerce stores selling home and outdoor products across the United States.

Historical Coverage:
- January 2022 – December 2024
- Approximately 10,000 orders

Daily Incremental File:
- One CSV file received daily containing newly created orders

---

## Column Definitions

| Column | Data Type | Description |
|----------|----------|----------|
| order_id | STRING | Unique order identifier |
| order_date | DATE | Date order was created |
| customer_id | STRING | Unique customer identifier |
| customer_name | STRING | Customer full name |
| customer_email | STRING | Customer email address |
| product_id | STRING | Product identifier |
| product_name | STRING | Product name |
| category | STRING | Product category |
| quantity | INTEGER | Quantity purchased |
| unit_price | FLOAT | Price per item |
| revenue | FLOAT | Quantity × Unit Price |
| store_name | STRING | Store where order originated |
| shipping_city | STRING | Shipping city |
| shipping_state | STRING | Shipping state |
| shipping_country | STRING | Shipping country |
| shipping_cost | FLOAT | Shipping charge |
| payment_method | STRING | Payment type |
| order_status | STRING | Completed, Returned, Cancelled |

---

## Stores

- OutdoorHub
- PatioWorld
- HomeEssentials
- GardenPro
- CampMaster

---

## Product Categories

- Patio Furniture
- Garden Tools
- Camping Gear
- Outdoor Decor
- Kitchen
- Home Decor
- Storage
- Lighting

---

## Payment Methods

- Credit Card
- PayPal
- Apple Pay
- Google Pay

---

## Order Status

- Completed
- Returned
- Cancelled

---

## Planned Data Quality Issues

### Duplicate Orders
Purpose:
- Validate uniqueness checks

### Missing Order Dates
Purpose:
- Validate mandatory field checks

### Negative Revenue
Purpose:
- Validate business rule checks

### Invalid Emails
Purpose:
- Validate format checks

### Missing Store Names
Purpose:
- Validate reference integrity checks

### Product Name Variations
Examples:
- Camping Chair
- camping chair
- Camp Chair

Purpose:
- Validate standardization logic

---

## Business Assumptions

1. One row represents one purchased product.
2. Revenue = Quantity × Unit Price.
3. Customers can place multiple orders.
4. Orders can be returned.
5. All stores share a centralized analytics platform.