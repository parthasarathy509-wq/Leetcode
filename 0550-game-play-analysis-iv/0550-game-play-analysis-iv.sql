select 
Round(count(distinct player_id)/(select count(distinct player_id)from activity),2) 
 as fraction from
 (select player_id,
 device_id,
 event_date,
 lead(event_date,1) over(partition by player_id order by event_Date asc) as next_login,
 min(event_date) over(partition by player_id ) as first_login from Activity
 ) as c 
 where datediff(next_login,event_date)=1
 and event_date =first_login ;