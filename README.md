# Ecommerce Analytics Platform

## Live Demo

🚀 Streamlit Application

https://ecommerce-analytics-platform-8j4dsvxex64fbefjtascx4.streamlit.app/

---

## Overview

This project demonstrates an end-to-end analytics engineering solution built for an e-commerce company experiencing challenges with manual data ingestion, poor data quality, and limited self-service analytics capabilities.

The solution includes:

- Automated data pipeline
- BigQuery data warehouse
- Data quality framework
- Validation and reconciliation framework
- Analytics-ready reporting layer
- AI-powered analytics chatbot
- Streamlit Cloud deployment

The platform enables non-technical users to ask business questions in plain English and receive data-driven answers directly from the warehouse.

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
                          │
                          ▼
                    OpenAI GPT
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
                    OpenAI GPT
                          │
                          ▼
              Natural Language Response
                          │
                          ▼
                    Streamlit UI
```

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python |
| Data Processing | Pandas |
| Data Warehouse | BigQuery |
| Transformations | SQL |
| Data Validation | SQL + Python |
| AI Layer | OpenAI GPT |
| Frontend | Streamlit |
| Deployment | Streamlit Cloud |
| Cloud Platform | GCP |

---

# Key Features

### Data Engineering

- Automated data ingestion workflow
- Layered warehouse architecture
- Data quality monitoring
- Validation and reconciliation framework
- Analytics-ready reporting layer

### AI Analytics Chatbot

- Natural language querying
- OpenAI-powered SQL generation
- BigQuery query execution
- Natural language response generation
- Streamlit-based user interface

### Deployment

- Cloud-hosted application
- Secure API key management
- BigQuery integration
- End-to-end working prototype

---

# Dataset Generation

A realistic e-commerce dataset was generated to simulate approximately three years of order history across multiple online stores.

Dataset characteristics:

- 10,050 records
- 5 online stores
- Multiple product categories
- Customer information
- Order transactions
- Revenue metrics

Intentional data quality issues were injected:

- Duplicate orders
- Missing order dates
- Missing store names
- Invalid email addresses
- Product naming inconsistencies
- Negative revenue records

These issues were later detected and handled by the data quality framework.

---

# Data Warehouse Design

## Raw Layer

Table:

```sql
raw_orders
```

Purpose:

- Stores source data exactly as received
- Immutable source of truth
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
- Applies business rules
- Cleanses source data

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

# Data Quality Framework

Automated data quality checks are executed before data is consumed by downstream analytics.

Checks include:

### Duplicate Orders

Detect duplicate transactions.

### Missing Order Dates

Identify records with missing dates.

### Negative Revenue

Detect invalid revenue values.

### Missing Store Names

Identify incomplete store information.

### Invalid Email Addresses

Validate email formatting.

### Product Name Variations

Detect inconsistent product naming.

---

# Validation Framework

The validation layer ensures integrity across the entire pipeline.

### Revenue Reconciliation

Validates revenue consistency across:

- Raw Layer
- Staging Layer
- Mart Layer

### Row Count Validation

Validates expected row count reductions after cleansing.

### Data Cleanup Validation

Confirms successful removal of:

- Duplicate records
- Missing dates
- Negative revenue

---

# AI Analytics Chatbot

The platform includes a fully functional AI-powered analytics chatbot.

Users can ask business questions in plain English without writing SQL.

## Architecture

```text
User Question
      │
      ▼
  Streamlit UI
      │
      ▼
   OpenAI GPT
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
   OpenAI GPT
      │
      ▼
Natural Language Response
      │
      ▼
  Streamlit UI
```

## Example Questions

- What was the total revenue last month?
- Which store generated the highest revenue?
- Show the top 5 products by revenue.
- Which category sold the most products?
- What is the average order value?

## Capabilities

- Natural language understanding
- Dynamic SQL generation
- BigQuery execution
- Business-friendly responses
- Self-service analytics

---

# Streamlit Cloud Deployment

The AI Analytics Chatbot is deployed on Streamlit Cloud.

Deployment features:

- Live cloud-hosted application
- OpenAI API integration
- BigQuery integration
- Secure credential management
- Interactive user experience

Live Application:

https://ecommerce-analytics-platform-8j4dsvxex64fbefjtascx4.streamlit.app/

---

# Project Structure

```text
ecommerce-analytics-platform/
│
├── chatbot/
│   ├── app.py
│   ├── bigquery_service.py
│   ├── config.py
│   ├── response_generator.py
│   ├── schema.py
│   ├── sql_generator.py
│   └── tests/
│
├── data/
│   ├── generated/
│   │   └── orders_dataset.csv
│   └── raw/
│
├── docs/
│   └── source_dataset_design.md
│
├── pipelines/
│   ├── load_raw.py
│   ├── run_staging.py
│   ├── run_mart.py
│   ├── run_data_quality.py
│   ├── run_validation.py
│   ├── run_pipeline.py
│   └── test_bigquery_connection.py
│
├── scripts/
│   ├── generate_orders_dataset.py
│   └── data_profile.py
│
├── sql/
│   ├── stg_orders.sql
│   ├── sales_summary.sql
│   ├── validation_queries.sql
│   └── data_quality/
│
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
```

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

# How To Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Generate Dataset

```bash
python scripts/generate_orders_dataset.py
```

## Run Full Pipeline

```bash
python pipelines/run_pipeline.py
```

## Launch Chatbot

```bash
streamlit run chatbot/app.py
```

---

# Production Considerations

Potential enhancements for production deployment:

- Apache Airflow / Cloud Composer
- Incremental loading
- Partitioned BigQuery tables
- Monitoring and alerting
- CI/CD pipelines
- Infrastructure as Code (Terraform)
- dbt transformations
- Great Expectations
- Data Catalog integration

---

# Conclusion

This project demonstrates a complete analytics engineering workflow, covering data generation, ingestion, transformation, data quality management, validation, warehouse modeling, AI-powered analytics, and cloud deployment.

The solution enables self-service analytics through natural language interactions while maintaining strong data quality and governance practices. The architecture follows modern data engineering principles and can be extended into a production-grade analytics platform with minimal architectural changes.