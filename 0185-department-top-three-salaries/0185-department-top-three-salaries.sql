SELECT 
    d.name AS Department,
    c.Employee,
    c.Salary
FROM (
    SELECT 
        departmentId,
        name AS Employee,
        Salary,
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY Salary DESC) AS D_rank
    FROM Employee
) as c 
INNER JOIN Department d ON c.departmentId = d.id
WHERE c.D_rank <= 3;
