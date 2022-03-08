-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp, RANK() OVER(ORDER BY avg_temp DESC) AS r
FROM temperatures GROUP BY city
