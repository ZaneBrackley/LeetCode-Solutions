# Write your MySQL query statement below
select name, bonus
from Employee
left join Bonus
using (empID)
where (Bonus < 1000)
or Bonus is null