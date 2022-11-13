SELECT *
FROM workout
WHERE target NOT IN ('abs', 'arms')
AND intensity <> 'low';
