-- Write your PostgreSQL query statement below
select unique_id , e.name from EmployeeUNI right join Employees e using(id);