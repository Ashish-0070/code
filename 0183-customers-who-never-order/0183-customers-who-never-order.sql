# Write your MySQL query statement below
SELECT  Customers.name as Customers
FROM Customers
LEFT JOIN Orders
ON Customers.id = Orders.customerId where Orders.id is null;