## Find Music Albums
 We'll browse through a table of music albums
 looking for titles by Patti Smith or Miles Davis.

### Database

 `albums`
 | title | artist |
 | ------ | ------ |
 | Kind of Blue | Miles Davis |
 | Rumours | Fleetwood Mac |
 | Blue | Joni Mitchel |
 | Horses | Patti Smith |
 
 
### Query 
 ```sql
 SELECT title 
 FROM albums
 WHERE artist IN ('Miles Davis ','Patti Smith')
 ORDER BY title;
 ```
 
### Query Result
 | title |
 | --- |
 | Horses | 
 | Kind Of Blue |
