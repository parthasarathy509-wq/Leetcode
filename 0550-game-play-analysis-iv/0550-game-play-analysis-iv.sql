select 
Round(count(player_id)/(select count(distinct player_id) from Activity),2) as fraction
from
(select 
player_id,event_date,
min(event_date) over(partition by player_id)as first_login,
lead(event_date ,1 ) over(partition by player_id order by event_date asc) as next_login
 from 
Activity)as c 
where datediff(next_login,first_login)=1;