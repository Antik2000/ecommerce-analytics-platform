# Ecommerce Analytics Platform

## Overview

The objective of this project was to design and implement an end-to-end analytics solution for an e-commerce company facing challenges with manual data ingestion, poor data quality, and limited self-service analytics capabilities.

The solution includes:

- Automated data ingestion pipeline
- Data warehouse design using BigQuery
- Data quality validation framework
- Data validation and reconciliation checks
- Business-ready analytics mart
- Production-style orchestration
- Foundation for an AI-powered analytics chatbot

---

# Business Problem

An e-commerce company selling home and outdoor products across multiple online stores is facing several challenges:

- Daily CSV files are loaded manually into the warehouse.
- No automated data pipeline exists.
- Duplicate orders are appearing in reports.
- Missing dates impact business reporting.
- Product names are inconsistent across records.
- Stakeholders do not trust dashboard numbers.
- Non-technical users depend on the BI team for every business question.

The goal is to build a scalable analytics solution that automates data ingestion, improves data quality, and enables self-service analytics.

---

# Solution Architecture

```text
Generated Orders CSV
          │
          ▼
    Raw Layer
 (raw_orders)
          │
          ▼
  Staging Layer
 (stg_orders)
          │
          ▼
    Mart Layer
(sales_summary)
          │
          ├─────────────► Data Quality Checks
          │
          └─────────────► Validation Checks
                          │
                          ▼
                 Analytics Ready Data
```

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python |
| Data Processing | Pandas |
| Data Warehouse | BigQuery |
| Transformations | SQL |
| Orchestration | Python |
| Data Validation | SQL + Python |
| AI Layer (Planned) | LLM + BigQuery |
| Cloud Platform | GCP |

---

# Dataset Generation

A realistic e-commerce dataset was generated to simulate approximately three years of order history across multiple online stores.

Dataset characteristics:

- 10,050 total records
- 5 online stores
- Multiple product categories
- Customer information
- Order information
- Revenue calculations

Intentional data quality issues were injected into the dataset:

- Duplicate orders
- Missing order dates
- Missing store names
- Invalid email addresses
- Product naming inconsistencies
- Negative revenue records

These issues were later detected and handled by the data quality framework.

---

# Data Warehouse Design

The warehouse follows a layered architecture.

## Raw Layer

Table:

```sql
raw_orders
```

Purpose:

- Stores source data exactly as received
- Serves as immutable source of truth
- Supports auditing and troubleshooting

---

## Staging Layer

Table:

```sql
stg_orders
```

Purpose:

- Removes duplicate orders
- Removes invalid records
- Standardizes product names
- Applies business validation rules

---

## Mart Layer

Table:

```sql
sales_summary
```

Purpose:

- Business-ready reporting layer
- Aggregated metrics
- Faster analytical queries
- Dashboard consumption

Metrics include:

- Total Orders
- Total Revenue
- Average Order Value

---

# Project Structure

```text
ecommerce_analytics/
│
├── data/
│   └── orders.csv
│
├── sql/
│   ├── stg_orders.sql
│   ├── sales_summary.sql
│   │
│   └── data_quality/
│       ├── duplicate_orders.sql
│       ├── missing_order_dates.sql
│       ├── negative_revenue.sql
│       ├── missing_store_names.sql
│       ├── check_email_format.sql
│       └── check_product_name_variations.sql
│
├── generate_orders_dataset.py
├── data_profile.py
├── load_raw.py
├── run_staging.py
├── run_mart.py
├── run_data_quality.py
├── run_validation.py
├── run_pipeline.py
│
└── README.md
```

---

# Pipeline Workflow

The pipeline executes in the following order:

```text
1. Generate Dataset
2. Load Raw Data
3. Run Staging Transformations
4. Build Analytics Mart
5. Execute Data Quality Checks
6. Execute Validation Checks
```

Pipeline orchestration is handled by:

```python
run_pipeline.py
```

This script coordinates execution and handles failures using try/except logic.

---

# Data Quality Framework

The solution includes automated data quality checks executed before data is consumed by downstream analytics.

## Duplicate Orders

Purpose:

Detect duplicate transactions.

Query:

```sql
duplicate_orders.sql
```

---

## Missing Order Dates

Purpose:

Identify records with missing dates.

Query:

```sql
missing_order_dates.sql
```

---

## Negative Revenue

Purpose:

Identify invalid revenue records.

Query:

```sql
negative_revenue.sql
```

---

## Missing Store Names

Purpose:

Identify incomplete store information.

Query:

```sql
missing_store_names.sql
```

---

## Invalid Email Addresses

Purpose:

Identify malformed customer emails.

Query:

```sql
check_email_format.sql
```

---

## Product Name Variations

Purpose:

Detect inconsistent product naming.

Query:

```sql
check_product_name_variations.sql
```

---

# Validation Framework

The validation layer ensures data integrity throughout the pipeline.

## Revenue Reconciliation

Validates that revenue remains consistent across transformations.

Validation compares:

- Raw Layer
- Staging Layer
- Mart Layer

---

## Row Count Validation

Validates expected row count reductions due to cleaning operations.

Validation compares:

- Raw Layer
- Staging Layer
- Mart Layer

---

## Data Cleanup Validation

Confirms successful removal of:

- Duplicate records
- Missing dates
- Negative revenue

---

# Results

## Row Counts

| Layer | Row Count |
|---------|------------|
| Raw | 10,050 |
| Staging | 9,851 |
| Mart | 965 |

---

## Revenue Validation

| Layer | Revenue |
|---------|------------|
| Raw Valid Revenue | 7,730,918.39 |
| Staging Revenue | 7,693,201.66 |
| Mart Revenue | 7,693,201.66 |

Revenue reconciliation passed successfully.

---

## Data Quality Results

| Check | Result |
|---------|------------|
| Duplicate Orders Found | 50 |
| Negative Revenue Remaining | 0 |
| Missing Dates Remaining | 0 |

---

# Orchestration

The pipeline can be executed end-to-end using:

```bash
python run_pipeline.py
```

Execution sequence:

```text
load_raw.py
      ↓
run_staging.py
      ↓
run_mart.py
      ↓
run_data_quality.py
      ↓
run_validation.py
```

---

# AI Chatbot Architecture (Planned)

The next phase of the solution enables natural language querying of warehouse data.

Example questions:

- How did we perform last month?
- Which store generated the highest revenue?
- Which products are selling the most?

Proposed architecture:

```text
User Question
       │
       ▼
      LLM
       │
       ▼
 SQL Generation
       │
       ▼
   BigQuery
       │
       ▼
 Query Results
       │
       ▼
 Natural Language Response
```

This enables self-service analytics for non-technical users.

---

# Production Considerations

For a production deployment, the following enhancements would be implemented:

## Workflow Orchestration

Current:

```text
run_pipeline.py
```

Production:

```text
Apache Airflow
or
Cloud Composer (GCP)
```

---

## Monitoring

- Pipeline execution monitoring
- Data quality alerts
- Failure notifications

---

## CI/CD

- GitHub Actions
- Automated testing
- Automated deployment

---

## Infrastructure as Code

- Terraform
- Environment provisioning
- Resource management

---

## Incremental Loading

Instead of full refreshes:

- Daily incremental ingestion
- Partitioned tables
- Reduced processing cost

---

# How to Run

## Generate Dataset

```bash
python generate_orders_dataset.py
```

## Load Raw Data

```bash
python load_raw.py
```

## Build Staging Layer

```bash
python run_staging.py
```

## Build Mart Layer

```bash
python run_mart.py
```

## Run Data Quality Checks

```bash
python run_data_quality.py
```

## Run Validation Checks

```bash
python run_validation.py
```

## Run Entire Pipeline

```bash
python run_pipeline.py
```

---

# Future Enhancements

- Apache Airflow / Cloud Composer
- dbt-based transformations
- Great Expectations
- Data Catalog
- Automated alerting
- Infrastructure as Code
- Incremental processing
- AI chatbot deployment
- Dashboard integration
- Real-time ingestion

---

# Conclusion

This project demonstrates a complete analytics engineering workflow, including data generation, ingestion, transformation, quality validation, business reporting, and preparation for AI-powered analytics.

The solution follows industry-standard data engineering practices and can be extended into a production-grade analytics platform with minimal architectural changes.