-- Normalize statuses and create unified fact table

SELECT
    id,
    event_date,
    department,
    amount,
    currency,
    CASE
        WHEN status = 'POSTED' OR status = 'CLOSED' THEN 'CONFIRMED'
        WHEN status = 'PENDING' OR status = 'OPEN' THEN 'IN_PROGRESS'
        ELSE 'UNKNOWN'
    END AS normalized_status,
    source_system
FROM unified_staging;
