-- Write your PostgreSQL query statement below
select 
case 
    when count(distinct salary)>=2 then (select distinct salary from Employee order by salary desc limit 1 offset 1) else
null end as SecondHighestSalary
from employee;