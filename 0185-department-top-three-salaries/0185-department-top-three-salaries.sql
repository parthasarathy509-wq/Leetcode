select 
Department,Employee,Salary
from
(select e.id,e.name as Employee,salary as Salary,departmentId,d.name as Department,
dense_rank() over(partition by departmentId order by salary desc) as ranking
from 
Department d inner join Employee e on d.id=e.departmentId ) as c 
where ranking IN(1,2,3)
;