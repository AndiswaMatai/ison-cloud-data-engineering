# Data Governance & Design Notes

## Data Lineage
- Source system tracked via `source_system`
- Unified schema across SAP and Operations

## Business Rules
- Status normalization ensures consistent reporting
- All financial metrics standardized to ZAR

## Design Principles
- Separation of ingestion, transformation, analytics
- Reproducible SQL transformations
- Analytics-ready fact tables
