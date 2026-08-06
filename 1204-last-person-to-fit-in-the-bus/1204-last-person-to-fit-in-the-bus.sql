select 
person_name
from 
(select person_id,
person_name ,
weight,
turn,
row_number() over(order by turn asc) as sequence ,
sum(weight)over(order by turn asc) as running_weight
 from Queue 
 ) as c 
 where running_weight<=1000
 group by person_id having max(turn)=
(select max(turn) from (select person_id,
person_name ,
weight,
turn,
row_number() over(order by turn asc) as sequence ,
sum(weight)over(order by turn asc) as running_weight
 from Queue ) as d where running_weight<=1000)
 ;