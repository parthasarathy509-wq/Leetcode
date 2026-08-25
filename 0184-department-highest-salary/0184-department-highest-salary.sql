select 
Department,Employee,Salary
from
(select  d.name Department , e.name Employee ,salary Salary ,
dense_rank() over(partition by d.id order by salary desc)  as ranking
 from Employee e inner join Department d on e.departmentId=d.id
 )as c 
 where ranking=1
 ;
