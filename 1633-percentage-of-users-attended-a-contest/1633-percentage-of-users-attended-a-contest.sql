select contest_id,Round((count(*)/(select count(distinct user_id) from Users))*100,2) as percentage 
from Register 
     
     group by contest_id 

     order by percentage Desc ,contest_id asc; 


