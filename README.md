
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

