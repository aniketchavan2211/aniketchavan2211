## Food Delivery Service

Ordering takeout gets easier when filtering by cuisine and ordering the
restaurants by rating.

### Table

**offer**
| restaurant | cuisine | rating |
| ---------- | ------- | ------ |
| Yumi | Japanese | 3 |
| La Zucca | Italian | 4.5 |
| Sombrero | Mexican | 3.5 |
| Masa | Japanese | 4.9 |

### Query

**script.sql**

```sql
SELECT restaurant AS japanese
FROM offer
WHERE cuisine = 'japanese'
ORDER BY rating DESC;
```
**IF ANY Issue see the script.sql in repo**

### Result

| japanese |
| -------- |
| Masa |
| Yumi |
