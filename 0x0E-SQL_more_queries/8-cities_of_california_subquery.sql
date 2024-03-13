-- lists all cities in database table
SELECT * FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC, state_id ASC, name;
