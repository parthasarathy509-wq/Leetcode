select id from 
(
select 
id,recordDate ,temperature ,
lag(temperature,1) over(order by recordDate) as prev_temp,
lag(recordDate,1) over() as prev_date
from Weather) as c 
where prev_temp<temperature
and datediff(recordDate,prev_date)=1;