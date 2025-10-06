# Write your MySQL query statement below
delete p from person p join person p2 using(email) where p.id >p2.id;