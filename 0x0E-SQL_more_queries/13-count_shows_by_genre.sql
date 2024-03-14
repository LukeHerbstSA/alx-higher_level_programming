-- lists number of occurences of each show with a particular genre
SELECT tv_genres.name AS genre, 
(SELECT COUNT(*) FROM tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id) AS number_of_shows 
FROM tv_genres ORDER BY number_of_shows DESC;
