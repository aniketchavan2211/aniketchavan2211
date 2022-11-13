## Personal Planner

Keeping track of tasks can be a hassle. That's where filtering by priority
or days, left until the deadline might come in handy.

### Table
**planner**
| task | priority | days_left |
| ---- | -------- | --------- |
| draft article | medium | 2 |
| water cactus | low | 0 |
| calculate taxes | high | 3 |

### Query

**script.sql**

```sql
SELECT task
FROM planner
WHERE priority = 'high'
OR days_left <= 1;
```

### Result

| task |
| ---- |
| water cactus |
| calculate taxes |
