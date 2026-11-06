select contest_id,
ROUND(COUNT(DISTINCT user_id) * 100.0/ (select COUNT(*) from Users ), 2) as percentage 
from Register
group by contest_id
order by percentage desc, contest_id asc;