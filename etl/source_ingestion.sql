-- Ingest SAP and operational data into unified staging

SELECT
    record_id AS id,
    posting_date AS event_date,
    department,
    amount,
    currency,
    status,
    'SAP' AS source_system
FROM source_sap_finance

UNION ALL

SELECT
    op_id AS id,
    op_date AS event_date,
    process AS department,
    value AS amount,
    'ZAR' AS currency,
    status,
    'OPS' AS source_system
FROM source_operations;
