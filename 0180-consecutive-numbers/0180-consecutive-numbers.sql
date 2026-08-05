SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        ROW_NUMBER() OVER (ORDER BY id) 
        - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS delta
    FROM Logs
) AS derived_table
GROUP BY num, delta
HAVING COUNT(*) >= 3;
