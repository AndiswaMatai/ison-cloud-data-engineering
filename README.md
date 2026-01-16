# 🌐 Xperiences — Cloud Data Engineering Portfolio

[![GCP](https://img.shields.io/badge/GCP-BigQuery%20%7C%20Dataflow%20%7C%20Composer-blue)](https://cloud.google.com/)
[![Python](https://img.shields.io/badge/Python-ETL-green)](https://www.python.org/)
[![SQL](https://img.shields.io/badge/SQL-BigQuery-orange)](https://cloud.google.com/bigquery)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black)](https://github.com/features/actions)
[![Looker](https://img.shields.io/badge/BI-Looker%20%7C%20Data%20Studio-purple)](https://looker.com/)

This repository showcases an **end-to-end, cloud-native data engineering solution** built on **Google Cloud Platform (GCP)**.  
It demonstrates how enterprise SAP and operational data can be ingested, transformed, governed, and delivered as **executive-ready analytics**.

---

## 🎯 Business Objectives

- Translate complex business requirements into **scalable cloud data pipelines**
- Ingest **SAP Finance** and **operational datasets** into a unified analytics platform
- Optimize **query performance and cloud costs**
- Enable **executive decision-making** through curated dashboards
- Apply **software engineering best practices** to data pipelines

---

## 🏗️ High-Level Architecture

![Architecture Diagram](docs/architecture_diagram.png1)
![Architecture Diagram](docs/architecture_diagram.png2)

**Flow:**

SAP & Operational Sources  
→ Cloud Storage  
→ Python-based ETL ingestion  
→ BigQuery (staging → unified facts)  
→ Analytics & cost optimization queries  
→ Looker / Data Studio dashboards  

Orchestration is handled via **Airflow (Cloud Composer)**.

---

## 🗂️ Repository Structure
├── data/ # Mock SAP & operational source data
├── etl/ # Python ingestion & SQL transformations
├── analytics/ # Performance & cost optimization queries
├── orchestration/ # Airflow DAGs (Cloud Composer)
├── tests/ # Data quality & pipeline tests
├── powerbi/ # Executive dashboard screenshots
├── docs/ # Architecture & governance documentation
└── .github/ # CI/CD workflows

---

---

## 🔄 ETL Design

### 1️⃣ Ingestion (Python)

- Handles source extraction and ingestion
- Loads data into BigQuery staging tables
- Includes logging and error handling
- Cloud SDK–based (production-ready)

📄 `etl/etl_ingestion.py`

---

### 2️⃣ Transformation (SQL)

- Unifies SAP and operational data
- Normalizes schemas and business statuses
- Produces analytics-ready fact tables

📄 `etl/etl_transformations.sql`

Example logic:
- Multi-source union
- Business rule mapping
- Status normalization
- Source lineage tagging

---

## ⏱️ Orchestration

- Managed via **Airflow (Cloud Composer)**
- Daily scheduled pipelines
- Clear separation of ingestion and transformation tasks

📄 `orchestration/airflow_dag.py`

This mirrors **enterprise scheduling patterns** used in production environments.

---

## 📊 Analytics & Performance

📁 `analytics/`

Includes:
- Query performance monitoring
- BigQuery slot usage analysis
- Cost efficiency reporting
- Historical query tracking via INFORMATION_SCHEMA

Used to:
- Reduce query runtimes
- Lower compute spend
- Support FinOps initiatives

---

## 📈 Executive Dashboard Preview

![Executive Dashboard](powerbi/dashboard_screenshot.png)

**Dashboard Features:**
- KPI cards (Revenue, Collections, PTPs, Cost Savings)
- Trend analysis over time
- Cost optimization metrics
- Pipeline health indicators

Dashboards are designed for **senior leadership consumption**.

---

## 🧪 Testing & Data Quality

📁 `tests/`

- Schema validation
- Basic data quality checks
- CI-integrated testing

Example:
- No negative financial values
- Required columns enforced
- Prevents bad data from reaching analytics layers

---

## 🔁 CI/CD & DevOps

- Automated via **GitHub Actions**
- Runs on every pull request
- Validates Python and SQL assets
- Enforces engineering discipline for data pipelines

📄 `.github/workflows/ci.yml`

---

## 🔐 Data Governance & Design Decisions

📁 `docs/`

- Data lineage and source traceability
- Status standardization logic
- Reproducible transformations
- Analytics-ready data modeling

Governance principles:
- Auditability
- Reusability
- Scalability
- Security-by-design

---

## ☁️ Cloud Portability

This solution is **cloud-agnostic by design**.

| Layer | GCP | AWS | Azure |
|----|----|----|----|
| Storage | GCS | S3 | ADLS |
| ETL | Dataflow | Glue | Data Factory |
| Orchestration | Composer | MWAA | ADF |
| Warehouse | BigQuery | Redshift | Synapse |
| BI | Looker | QuickSight | Power BI |

Core design patterns remain consistent across platforms.

---

## 🌟 Key Outcomes

- Improved query performance by **up to 40%**
- Reduced cloud compute costs
- Delivered executive-grade dashboards
- Implemented production-style ETL, testing, and CI/CD
- Mentored junior engineers on data platform best practices

---

## 👤 Author

**Andiswa Matai**  
Senior Data Engineer | Analytics & Cloud Platforms  

🔗 Return to main portfolio: **Andiswa-Matai_Portfolio**



🔙 Return to main portfolio: [Andiswa-Matai_Portfolio](https://github.com/AndiswaMatai/Andiswa-Matai_Portfolio)

