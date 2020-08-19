# DROP TABLES

songplay_table_drop = "drop table if exists songplay;"
user_table_drop = "drop table if exists users;"
song_table_drop = "drop table if exists songs;"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time;"

# CREATE TABLES

songplay_table_create = ("""
    create table if not exists songplays 
    (songplay_id serial primary key,
    start_time bigint NOT NULL, 
    user_id text NOT NULL, 
    level text, 
    song_id text, 
    artist_id text, 
    session_id text NOT NULL, 
    location text,
    user_agent text);
""")

user_table_create = ("""
    create table if not exists users(
    user_id text primary key,
    first_name text,
    last_name text,
    gender varchar,
    level varchar);
""")

song_table_create = ("""
    create table if not exists songs(
    song_id text primary key,
    title text not null,
    artist_id text,
    year int,
    duration numeric);
""") 

artist_table_create = ("""
    create table if not exists artists(
    artist_id text primary key,
    name varchar not null,
    location varchar,
    latitude numeric,
    longitude numeric);
""") 

time_table_create = ("""
    create table if not exists time(
    start_time bigint primary key,
    hour int not null,
    day int not null,
    week int not null,
    month int not null, 
    year int not null,
    weekday int not null);
""")


# INSERT RECORDS

songplay_table_insert = ("""
    insert into songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    values(%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    insert into users(user_id, first_name, last_name, gender, level) 
    values(%s, %s, %s, %s, %s)
    on conflict(user_id) 
    do update 
        set level = excluded.level
""")

song_table_insert = ("""
    insert into songs(song_id, title, artist_id, year, duration) values(%s, %s, %s, %s, %s)
    on conflict(song_id) do nothing;
""")

artist_table_insert = ("""
    insert into artists(artist_id, name, location, latitude, longitude) values(%s, %s, %s, %s, %s)
    on conflict(artist_id) do nothing;
""")


time_table_insert = ("""
    insert into time(start_time, hour, day, week, month, year, weekday) 
    values(%s, %s, %s, %s, %s, %s, %s)
    on conflict(start_time) do nothing;
""")

# FIND SONGS

song_select = ("""
    select s.song_id, a.artist_id
    from songs s inner join artists a on (s.artist_id = a.artist_id)
    where  lower(s.title) like lower(%s)
    and lower(a.name) like lower(%s)
    and s.duration = %s 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]