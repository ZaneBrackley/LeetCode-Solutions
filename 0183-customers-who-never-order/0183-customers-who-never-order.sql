# Write your MySQL query statement below
select c.name AS Customers from Customers c
LEFT JOIN Orders o on c.id = o.customerId
where o.customerId IS NULL;