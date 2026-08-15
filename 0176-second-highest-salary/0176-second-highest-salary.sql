select 
max(salary) as SecondHighestSalary
from 
(select id,salary,
dense_rank() over(order by salary desc) as rank_
from Employee ) as c 
where rank_=2
;