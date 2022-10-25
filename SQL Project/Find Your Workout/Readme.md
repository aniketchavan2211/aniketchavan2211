## Find Your Workout

Filter an app's 'workout' table by excluding certain targets and intensity
levels to find those workouts that fits you best.

### Table

**Workout**
| target | intensity |
| ------ | --------- |
| abs | medium |
| legs | high |
| back | low | 

### Query 

**script.sql**

```sql
SELECT *
FROM workout
WHERE target NOT IN ('abs', 'arms')
AND intensity <> 'low';
```

### Result

| target | intensity |
| ------ | --------- |
| legs | high |

