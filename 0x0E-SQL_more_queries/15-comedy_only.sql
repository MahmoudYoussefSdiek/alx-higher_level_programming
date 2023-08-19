-- Lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = 'Comedy'

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IN (SELECT id FROM tv_genres WHERE name = 'Comedy')
ORDER BY tv_shows.title;
