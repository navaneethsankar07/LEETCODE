select 
    query_name,
    ROUND(
        sum(rating*1.0/position) / count(query_name),
        2
    ) as quality,
    round(
        100.0*count(rating) filter (where rating < 3)
        / count(rating),
        2
    ) as poor_query_percentage

from queries
group by query_name;