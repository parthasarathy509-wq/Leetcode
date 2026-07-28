(Select name as results
from(select name,count(*) as cnt from Users u inner join MovieRating m on u.user_id=m.user_id group by u.user_id order by cnt desc,name asc limit 1
) as s 
)
union all 
(select title as results 
from (select m.title,avg(m1.rating) as avr from Movies m inner join MovieRating m1 on m.movie_id=m1.movie_id where created_at between '2020-02-01'and '2020-02-29'
group by m.title order by avr desc ,title asc limit 1  )
as c  );