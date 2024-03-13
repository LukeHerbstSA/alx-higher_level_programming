-- lists all cities in database table
SELECT * FROM cities WHERE state_id IN (SELECT * from states WHERE name = 'California');
