-- Cost efficiency analysis by department

SELECT
    department,
    SUM(amount) AS total_spend,
    COUNT(*) AS record_count,
    AVG(amount) AS avg_spend
FROM unified_fact
GROUP BY department;
