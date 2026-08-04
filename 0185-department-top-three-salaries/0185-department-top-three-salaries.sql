select Department,Employee,Salary from
(

Select d.name Department,
Salary ,
d.id,
e.name Employee ,
dense_rank() over(partition by d.name order by Salary desc) as D_rank
from Employee e inner join Department 
d on e.departmentId=d.id  ) as c 
where D_rank =1 or D_rank =2 or D_rank =3
;