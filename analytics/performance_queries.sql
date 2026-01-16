-- Operational performance metrics

-- Check query performance
SELECT
    query,
    total_bytes_processed/POWER(1024,3) AS GB_processed,
    total_slot_ms/1000 AS seconds
FROM
    `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
WHERE
    state='DONE'
ORDER BY
    creation_time DESC
LIMIT 10;

