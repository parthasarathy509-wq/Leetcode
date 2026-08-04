Select 
Case 
     when count(salary)=1 then salary 
     else null 
end as SecondHighestSalary

    from (
        Select distinct salary from Employee 
        order by salary desc 
        Limit 1 OFFSET 1
    ) as c 
    ;