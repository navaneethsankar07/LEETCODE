Select contest_id,
    Round(Count(user_id) * 100.0/(Select Count(*) from users), 2) as percentage
from Register
group by contest_id
order by percentage desc,contest_id asc;
