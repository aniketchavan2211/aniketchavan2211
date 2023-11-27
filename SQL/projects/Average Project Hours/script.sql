SELECT project, AVG(hours)
FROM work_sheet
GROUP BY project
HAVING AVG(hours) > 30;
