select 
Round(
(count(*)/(select count(distinct customer_id) from Delivery)) * 100,2) as immediate_percentage 
 from (select 
delivery_id ,customer_id,order_date
,customer_pref_delivery_date as pd ,
row_number() over(partition by customer_id order by order_date asc) as OD
from Delivery) as c 
where OD=1
and order_date=pd
;