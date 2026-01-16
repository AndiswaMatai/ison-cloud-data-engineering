# ETL Layer

This folder contains the ingestion and transformation logic for the data platform.

## Flow
1. Python scripts ingest SAP and operational data into BigQuery staging tables.
2. SQL transformations normalize schemas and business statuses.
3. Unified fact tables are produced for analytics and dashboards.

## Technology Choice
- Python: ingestion, orchestration, error handling
- SQL: scalable transformations inside BigQuery

