-- Write your PostgreSQL query statement below
select * from Users where email ~* '^[A-Z0-9_%+-]+@[A-Z]+\.com$' order by user_id asc;