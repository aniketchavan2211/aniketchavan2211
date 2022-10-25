SELECT task
FROM planner
WHERE priority = 'high'
OR days_left <= 1;
