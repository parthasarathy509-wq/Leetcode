select contest_id,Round((count(*)/(select count(distinct user_id) from Users))*100,2) as percentage 
from Users u inner join Register r on u.user_id=r.user_id 
     
     group by r.contest_id 

     order by percentage Desc ,contest_id asc; 


