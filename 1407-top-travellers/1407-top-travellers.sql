select
    u.name as name, COALESCE(SUM(distance), 0)  travelled_distance
from users u
left join rides r
on u.id = r.user_id
group by u.name, u.id
order by 2 desc, 1;

