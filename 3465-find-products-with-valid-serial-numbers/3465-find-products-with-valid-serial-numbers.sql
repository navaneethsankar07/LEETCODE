-- Write your PostgreSQL query statement below
select * 
from Products
where description ~ '(^|\s)SN\d{4}-\d{4}([^A-Za-z0-9]|$)'
order by product_id;