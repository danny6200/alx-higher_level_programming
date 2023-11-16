--  lists shows in hbtn_0d_tvshows having at least one genre linked.
-- A record should have: tv_shows.title, tv_show_genres.genre_id
-- Records must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id


SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
