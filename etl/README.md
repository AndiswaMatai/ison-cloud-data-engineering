# ETL Layer

This folder contains the **Extract, Transform, and Load (ETL)** logic for the data platform.

## Components

### Python Ingestion
- File: `etl_ingestion.py`
- Loads CSV data into BigQuery staging tables
- Handles schema consistency and ingestion logic

### SQL Transformations
- File: `etl_transformations.sql`
- Unifies SAP and operational data
- Normalizes business statuses
- Produces analytics-ready fact tables

## Design Principles
- Python for ingestion and orchestration
- SQL for scalable transformations
- Clear separation of concerns
