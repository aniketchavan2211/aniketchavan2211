## Get Your News 

 We can't keep up with all the news. But filtering by date or topic
 could help us find those articles we're really interested in.

### Database

 `news`
 | articles | tag | days_ago | 
 | --- | --- | --- |
 | Solar Storms | #science | 2 |
 | All About NFTs | #tech | 0 |
 | Mars Touchdown | #science | 4 |
 | Beautiful Soup | #food | 1 |

### Query 

 ```sql
 SELECT *
 FROM news
 WHERE tag IN ('#science', '#food')
 AND days_ago <= 2
 ORDER BY days_ago;
 ```

### Query Result

 | article | tag | days_ago |
 | --- | --- | --- |
 | Beautiful Storm | #food | 1 |
 | Solar Storm | #science | 2 |
