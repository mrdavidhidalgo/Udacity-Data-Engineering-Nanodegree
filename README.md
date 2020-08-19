## Sparkify star schema

The project scheme aims to be an implementation of Sparkify, a Json file architecture, to have a star model database.

### Purpose

The architecture that Sparkify implements is based on writing JSON files with information  
about songs and information about the users who listen to them, about which it can be useful at a transactional level,    
it allows you to generate information and store generating very little lock against disk with high speed.     
on the other hand it is also very difficult to generate reports with the current data schema.

This project aims to create an **OLAP** database for reporting purposes.   
Making aggregated queries and taking consolidated information easier by SQL. 


### Database Schema 

The proposed scheme is a star type scheme, with 4 dimension tables,  
This approach allows you to take full advantage of the flexibility of a SQL database.


#### Fact Table
songplays - table associated with song plays.    
fields -> songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

####  Dimension Tables

**users** - users in the app
fields -> (user_id, first_name, last_name, gender, level)

**songs** - songs in music database
fields -> (song_id, title, artist_id, year, duration)

**artists** - artists in music database
fields -> (artist_id, name, location, latitude, longitude)

**time** - timestamps of records in songplays broken down into specific units
fields -> (start_time, hour, day, week, month, year, weekday)


### Example queries

 
#### Top 10 - More active users

```sql
SELECT u.first_name||' '||u.last_name, count(1)   
FROM users u 
join songplays using (user_id)   
group by 1
order by 2 desc 
LIMIT 10;
```

<table style="width:50%; align:left">
  <tr>
    <th>user_name</th>
    <th>count</th>
  </tr>
  <tr>
    <td>Chloe Cuevas</td>
    <td>689</td> 
  </tr>
  <tr>
    <td>Tegan Levine</td>
    <td>665</td> 
  </tr>
  <tr>
    <td>Kate Harrell</td>
    <td>557</td> 
  </tr>
  <tr>
    <td>Lily Koch</td>
    <td>463</td> 
  </tr>
  <tr>
    <td>Aleena Kirby</td>
    <td>397</td> 
  </tr>
  <tr>
    <td>Jacqueline Lynch</td>
    <td>346</td> 
  </tr>
  <tr>
    <td>Layla Griffin</td>
    <td>321</td> 
  </tr>
  <tr>
    <td>Jacob Klein</td>
    <td>289</td> 
  </tr>
  <tr>
    <td>Mohammad Rodriguez</td>
    <td>270</td> 
  </tr>
  <tr>
    <td>Matthew Jones </td>
    <td>248</td> 
  </tr>
    
</table>


### How to run the Python scripts

To run python scripts

1. python3 create_tables.py  

This script drop and create the fact and dimension tables

2. python3 etl.py

This script extract, transform and load the data from json files to  
SQL database