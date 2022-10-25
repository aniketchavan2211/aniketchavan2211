SELECT *
FROM athlete
INNER JOIN award
ON athlete.name = award.name;
