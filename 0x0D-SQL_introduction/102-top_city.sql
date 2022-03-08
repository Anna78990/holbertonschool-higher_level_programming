-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures AS t1
GROUP BY city
INNER JOIN (SELECT t1.city AS city, RANK() OVER(ORDER BY t1.avg_temp DESC) AS r FROM t1) AS B
ON t1.city = B.city
