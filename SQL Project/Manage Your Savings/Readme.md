## Manage Your Savings 

Let's look into gaining insights from a users monthly savings by using
queries to make a few calculations.

### Table 

**savings**
| month | amount |
| ----- | ------ |
| January | 200 |
| February | 5 |
| March | 312 |

### Query 


**script.sql**

```sql
SELECT AVG(amount)
AS monthly_average
FROM savings;

SELECT MIN(amount)
AS least_saved
FROM savings;

SELECT MAX(amount)
AS most_saved
FROM savings;
```

### Result

| monthly_average |
| --------------- |
| 172.33333333333 |

| least_saved |
| ----------- |
| 5 |

| most_saved |
| ---------- |
| 312 |
