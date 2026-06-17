select 
    query_name,
    ROUND(
        sum(rating::numeric/position) / count(query_name),
        2
    ) quality,
    round(
        100. *count(rating) filter (where rating < 3)
        / count(rating),
        2
    )  poor_query_percentage

from queries
where query_name is not Null
group by query_name;