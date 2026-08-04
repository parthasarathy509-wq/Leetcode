
select d.name Department,c.name Employee,Salary
from
(select id,name,salary,departmentId ,
dense_rank() over(partition by departmentId order by salary desc) as Rank_
from Employee ) as c inner join Department d on c.departmentId=d.id
where Rank_=1
;