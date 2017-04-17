/**
Write a SQL query to find all numbers that appear at least three times consecutively.

+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+

For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.
 */

# Write your MySQL query statement below
SELECT DISTINCT L1.Num AS ConsecutiveNums
FROM `Logs` AS L1
INNER JOIN `Logs` AS L2
ON L1.Id + 1 = L2.Id
INNER JOIN `Logs` AS L3
ON L2.Id + 1 = L3.Id
WHERE L1.Num = L2.Num
    AND L2.Num = L3.Num;

/**
# Use inner join without where
SELECT DISTINCT L1.Num AS ConsecutiveNums
FROM `Logs` AS L1
INNER JOIN `Logs` AS L2
ON L1.Id + 1 = L2.Id 
    AND L1.Num = L2.Num
INNER JOIN `Logs` AS L3
ON L2.Id + 1 = L3.Id
    AND L2.Num = L3.Num;
 */

/**
# Don't use inner join
SELECT DISTINCT L1.Num AS ConsecutiveNums
FROM `Logs` AS L1, `Logs` AS L2, `Logs` AS L3
WHERE L1.Id + 1 = L2.Id
    AND L1.Num = L2.Num
    AND L2.Id + 1 = L3.Id
    AND L2.Num = L3.Num;
 */
