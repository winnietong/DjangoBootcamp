__author__ = 'winnie'


# psql -h localhost postgres
# create database blog;
# \connect blog   --> to connect to blog
#     or if you're in command line (terminal), just do psql -h localhost blog


# blog - authors, tags, posts
#
# CREATE TABLE author (
#   id       serial PRIMARY KEY,
#   name     varchar(120) NOT NULL,
#   twitter  varchar(40)
# );

#  Let's say we want to add Tags table

# CREATE TABLE tag(
#     id serial PRIMARY KEY,
#     name varchar(20) NOT NULL
# );
# INSERT INTO tag (name) VALUES ('food');
# INSERT INTO tag (name) VALUES ('literature');
# INSERT INTO tag (name) VALUES ('poetry');

#
# insert into country (code, name, continent, population, region, surfacearea, localname, governmentform, code2)
# values ('LIL', 'Lilliput', 'Europe', 150, 'North', 239, 'unknown', 'democracy', 'L2');
#
# update country set lifeexpectancy=100 where code='LIL';

# select (code, name, surfacearea) from country where continent='Oceania';
# select (name, population) from country where population>10000000;
# select (name, district, population) from city where countrycode='ITA';
# SELECT (language, countrycode) FROM countrylanguage WHERE percentage < 25;

# SELECT continent, AVG(population) AS avg_pop FROM country GROUP BY continent HAVING AVG(population) > 0;

# TABLE JOINS #
###############

# SELECT * FROM post INNER JOIN author ON (post.author_id = author.id);

# SELECT city.district, city.name, country.name, city.population,
# round((city.population::float /country.population*100)::numeric,1) as percentage
# FROM city, country
# WHERE city.id = country.capital and country.continent='Asia';



## HOMEWORK ##

# select tag.name from tag
# INNER JOIN post_tag on (post_tag.tag_id= tag.id)
# INNER JOIN post ON (post_tag.post_id = post.id)
# WHERE post.title = 'First!';

# select post.title from post
# INNER JOIN post_tag ON (post_tag.post_id = post.id)
# INNER JOIN tag ON (post_tag.tag_id = tag.id)
# WHERE tag.id = 1;

# select * from post
# INNER JOIN post_tag ON (post_tag.post_id = post.id)
# INNER JOIN tag ON (post_tag.tag_id = tag.id)
# WHERE tag.name = 'poetry';

# select tag.name from tag
# INNER JOIN post_tag ON (post_tag.tag_id = tag.id)
# INNER JOIN post ON (post_tag.post_id = post.id)
# INNER JOIN author ON (post.author_id = author.id)
# WHERE length(twitter) < 15;


# CREATE TABLE author (
#   id       serial PRIMARY KEY,
#   name     varchar(120) NOT NULL,
#   twitter  varchar(40)
# );