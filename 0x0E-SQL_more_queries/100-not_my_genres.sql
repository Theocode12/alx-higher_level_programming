--  a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

SELECT DISTINCT tv_genres.name
FROM tv_genres
    JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
    WHERE  tv_genres.id NOT IN (
                                    SELECT genre_id
                                    FROM tv_shows
                                        JOIN tv_show_genres
                                        ON tv_shows.id = tv_show_genres.show_id
                                        WHERE tv_shows.title = 'Dexter'
                                )
    ORDER BY tv_genres.name; 
