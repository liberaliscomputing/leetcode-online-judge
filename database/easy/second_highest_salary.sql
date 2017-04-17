/**
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

For example, given the above Employee table, the second highest salary is 200. If there is no second highest salary, then the query should return null.
 */

# Write your MySQL query statement below
SELECT MAX(Salary) AS SecondHighestSalary
FROM (
    SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1) AS E;

/**
# Use union
SELECT DISTINCT Salary AS SecondHighestSalary
FROM Employee
UNION
SELECT NULL
ORDER BY SecondHighestSalary DESC
LIMIT 1 OFFSET 1;
*/
