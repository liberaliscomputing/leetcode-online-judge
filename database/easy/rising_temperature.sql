/**
#Description
Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

+---------+------------+------------------+
| Id(INT) | Date(DATE) | Temperature(INT) |
+---------+------------+------------------+
|       1 | 2015-01-01 |               10 |
|       2 | 2015-01-02 |               25 |
|       3 | 2015-01-03 |               20 |
|       4 | 2015-01-04 |               30 |
+---------+------------+------------------+

For example, return the following Ids for the above Weather table:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+
 */

# Write your MySQL query statement below
SELECT W2.Id
FROM Weather AS W1
INNER JOIN Weather AS W2
ON W1.`Date` + INTERVAL 1 DAY = W2.`Date` 
WHERE W1.Temperature < W2.Temperature;

/**
# Use inner join without where
SELECT W2.Id
FROM Weather AS W1
INNER JOIN Weather AS W2
ON W1.`Date` + INTERVAL 1 DAY = W2.`Date` 
    AND W1.Temperature < W2.Temperature;
 */

/**
# Don't use inner join
SELECT W2.Id
FROM Weather AS W1, Weather AS W2
WHERE W1.`Date` + INTERVAL 1 DAY = W2.`Date` 
    AND W1.Temperature < W2.Temperature;
 */
