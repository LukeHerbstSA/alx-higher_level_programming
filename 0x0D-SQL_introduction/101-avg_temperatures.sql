-- displays avg temp on cities ordered by descending temp
SELECT city, AVG(value) AS avg_temp 
FROM temperatures 
GROUP BY city 
ORDER BY avg_temp DESC;
