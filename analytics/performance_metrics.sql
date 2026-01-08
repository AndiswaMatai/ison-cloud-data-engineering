-- Operational performance metrics

SELECT
    department,
    normalized_status,
    COUNT(*) AS metric_count
FROM unified_fact
GROUP BY department, normalized_status;
