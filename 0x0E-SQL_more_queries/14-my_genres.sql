--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT name
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg
ON tsg.show_id = ts.id
LEFT JOIN tv_genres AS tg
ON tg.id = tsg.genre_id
WHERE title = 'Dexter'
ORDER BY name ASC
