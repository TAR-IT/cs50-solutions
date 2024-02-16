SELECT DISTINCT p.name
FROM people p
JOIN stars s ON p.id = s.person_id
JOIN movies m ON s.movie_id = m.id
WHERE m.id IN (
    SELECT movie_id
    FROM stars
    WHERE person_id = (
        SELECT id
        FROM people
        WHERE name = 'Kevin Bacon' AND birth = 1958
    )
) AND p.name != 'Kevin Bacon';
