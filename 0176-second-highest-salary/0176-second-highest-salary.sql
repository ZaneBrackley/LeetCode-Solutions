# Write your MySQL query statement below
SELECT (
    select distinct salary from Employee
    order by salary desc
    LIMIT 1 OFFSET 1
) as SecondHighestSalary