# SQLZOO: [link](https://sqlzoo.net)


### **SELECT basics**
1. Modify it to show the population of Germany
```sql
SELECT population FROM world
WHERE name = 'Germany';
```
2. Show the ```name``` and the ```population``` for 'Sweden', 'Norway' and 'Denmark'
```sql
SELECT name, population FROM world
WHERE name IN ('Sweden', 'Norway', 'Denmark');
```
3. Which countries are not too small and not too big? ```BETWEEN``` allows range checking (range specified is inclusive of boundary values). The example below shows countries with an area of 250,000-300,000 sq. km. Modify it to show the country and the area for countries with an area between 200,000 and 250,000.
```sql
SELECT name, area FROM world
WHERE area BETWEEN 200000 AND 250000;
```


### **SELECT FROM world**
1. show the ```name```, ```continent``` and ```population``` of all countries.
```sql
SELECT name, continent, population FROM world
```
2. Show the name for the countries that have a population of at least 200 million. 200 million is 200000000, there are eight zeros.
```sql
SELECT name FROM world
WHERE population >= 200000000;
```
3. Give the ```name``` and the per capita GDP for those countries with a population of at least 200 million.
```sql
SELECT name, gdp/population
FROM world
WHERE population >= 200000000;
```
4. Show the ```name``` and ```population``` in millions for the countries of the continent 'South America'. Divide the population by 1000000 to get population in millions.
```sql
SELECT name, population/1000000
FROM world
WHERE continent = "South America";
```
5. Show the ```name``` and ```population``` for France, Germany, Italy
```sql
SELECT name, population
FROM world
WHERE name IN ('France', 'Germany', 'Italy');
```
6. Show the countries which have a name that includes the word 'United'
```sql
SELECT name
FROM world
WHERE name like "%United%";
```
7. Show the countries that are big by area or big by population. Show name, population and area.
```sql
SELECT name, population, area
FROM world
WHERE area > 3000000 OR population > 250000000
```


### **SELECT FROM nobel**
```
nobel(yr, subject, winner)
```
1. Change the query shown so that it displays Nobel prizes for 1950.
```sql
SELECT yr, subject, winner
FROM nobel
WHERE yr = 1950;
```
2. Show who won the 1962 prize for Literature.
```sql
SELECT winner
FROM nobel
WHERE yr = 1962
   AND subject = 'Literature';
```
3. Show the year and subject that won 'Albert Einstein' his prize.
```sql
SELECT yr, subject
FROM nobel
WHERE winner = 'ALbert Einstein';
```
4. Give the name of the 'Peace' winners since the year 2000, including 2000.
```sql
SELECT winner
FROM nobel
WHERE yr >= 2000 AND subject = 'Peace';
```
5. Show all details (yr, subject, winner) of the Literature prize winners for 1980 to 1989 inclusive.
```sql
SELECT * FROM nobel
WHERE subject = 'Literature' AND yr BETWEEN 1980 AND 1989;
```
6. Show all details of the presidential winners:
- Theodore Roosevelt
- Woodrow Wilson
- Jimmy Carter
- Barack Obama
```sql
SELECT * FROM nobel
WHERE  winner IN ('Theodore Roosevelt',
                  'Woodrow Wilson',
                  'Jimmy Carter', 
                  'Barack Obama');
```
7. Show the winners with first name John
```sql
SELECT winner
FROM nobel
WHERE winner LIKE "John %";
```
8. Show the year, subject, and name of Physics winners for 1980 together with the Chemistry winners for 1984.
```sql
SELECT * FROM nobel
WHERE (subject='Physics' AND yr=1980) OR (subject='Chemistry' AND yr=1984);
```
9. Show the year, subject, and name of winners for 1980 excluding Chemistry and Medicine
```sql
SELECT *
FROM nobel
WHERE yr=1980 AND subject NOT IN ('Chemistry', 'Medicine');
```
10. Show year, subject, and name of people who won a 'Medicine' prize in an early year (before 1910, not including 1910) together with winners of a 'Literature' prize in a later year (after 2004, including 2004)
```sql
SELECT * FROM nobel
WHERE (subject='Medicine' AND yr<1910) OR (subject = 'Literature' AND yr >=2004);
```
11. Find all details of the prize won by PETER GRÜNBERG. The u in his name has an [umlaut](https://en.wikipedia.org/wiki/%C3%9C#Keyboarding)
```sql
SELECT * FROM nobel
WHERE winner="PETER GRÜNBERG";
```
12. Find all details of the prize won by EUGENE O'NEILL (Escaping single quotes)
```sql
SELECT * FROM nobel
WHERE winner = "EUGENE O'NEILL";
```
13. List the winners, year and subject where the winner starts with Sir. Show the the most recent first, then by name order.
```sql
SELECT winner, yr, subject
FROM nobel
WHERE winner like 'Sir%'
order by yr desc, winner;
```
14. The expression subject IN ('Chemistry','Physics') can be used as a value - it will be 0 or 1. Show the 1984 winners and subject ordered by subject and winner name; but list Chemistry and Physics last.
```sql
SELECT winner, subject
FROM nobel
WHERE yr=1984
ORDER BY
 CASE WHEN subject IN ('Physics','Chemistry') THEN 1 ELSE 0 END,
 subject, winner;
```


### **SELECT in SELECT**
```
world(name, continent, area, population, gdp)
```
1. List each country name where the population is larger than that of 'Russia'
```sql
SELECT name FROM world
WHERE population >
     (SELECT population FROM world
      WHERE name='Russia');
```
2. Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.
```sql
SELECT name
FROM world
WHERE continent='Europe' 
	AND gdp/population > 
        	(SELECT gdp/population 
        	FROM world 
        	WHERE name='United Kingdom');
```
3. List the ```name``` and ```continent``` of countries in the continents containing either Argentina or Australia. Order by ```name``` of the country.
```sql
SELECT name, continent 
FROM world
WHERE continent in (SELECT continent 
	FROM world 
	WHERE name='Argentina' OR name='Australia')
ORDER BY name;
```
4. Which country has a population that is more than Canada but less than Poland? Show the ```name``` and the ```population```.
```sql
SELECT name, population 
FROM world
WHERE population > (SELECT population FROM world WHERE name='Canada')
	AND population < (SELECT population FROM world WHERE name='Poland');
```
5. Germany (population 80 million) has the largest population of the countries in Europe. Austria (population 8.5 million) has 11% of the population of Germany.**Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.**
```sql
SELECT name, concat(
	round(
		population/
		(SELECT population FROM world WHERE name='Germany')*100
		,0)
	,'%')
FROM world
WHERE continent='Europe';
```
6. Which countries have a GDP greater than every country in Europe? (Some countries may have NULL gdp values)
```sql
SELECT name
FROM world
WHERE gdp > ALL(SELECT gdp 
	FROM world 
	WHERE gdp>0 AND continent='Europe');
```
7. Find the largest country (by area) in each continent, show the continent, the name and the area.**The example is known as a correlated or synchronized sub-query.**
```sql
SELECT continent, name, area FROM world x
WHERE area >= ALL(SELECT area FROM world y
	WHERE y.continent=x.continent
	AND area>0);
```
8. List each continent and the name of the country that comes first alphabetically. **First country of each continent (alphabetically)**
```sql
SELECT continent, name
FROM world x
WHERE x.name <= ALL(SELECT name 
	FROM world y 
	WHERE x.continent=y.continent);
```
9. Find the continents where all countries have a ```population <= 25000000```. Then find the names of the countries associated with these continents. Show name, continent and population.
```sql
SELECT name, continent, population
FROM world
WHERE  continent IN (SELECT DISTINCT continent 
	FROM world 
	GROUP BY continent
	HAVING MAX(population) <= 25000000);
```
10. **(Hard)** Some countries have populations more than three times that of any of their neighbours (in the same continent). Give the countries and continents.
```sql
SELECT x.name, x.continent
FROM world x
WHERE x.population/3 >  ALL(SELECT z.population 
	FROM world z 
	WHERE z.continent=x.continent XOR z.name = x.name);
```


### **SUM and COUNT**
```
world(name, continent, area, population, gdp)
```
1. Show the total population of the world.
```sql
SELECT SUM(population)
FROM world;
```
2. List all the continents - just once each.
```sql
SELECT DISTINCT continent
FROM world;
```
3. Give the total GDP of Africa
```sql
SELECT SUM(gdp)
FROM world
WHERE continent="Africa";
```
4. How many countries have an area of at least 1000000
```sql
SELECT COUNT(DISTINCT name)
FROM world
WHERE area >= 1000000;
```
5. What is the total population of ('Estonia', 'Latvia', 'Lithuania')
```sql
SELECT SUM(population)
FROM world
WHERE name IN ('Estonia', 'Latvia', 'Lithuania');
```
6. For each continent show the continent and number of countries.
```sql
SELECT continent, COUNT(DISTINCT name)
FROM world
GROUP BY continent;
```
7. For each continent show the continent and number of countries with populations of at least 10 million.
```sql
SELECT x.continent, COUNT(x.name)
FROM (SELECT DISTINCT name, continent
	FROM world
	WHERE population >= 10000000) x
GROUP BY continent;
```
8. List the continents that have a total population of at least 100 million.
```sql
SELECT continent
FROM world
GROUP BY continent 
HAVING SUM(population) >= 100000000;
```


### **JOIN**
```
game(id, mdate, stadium, team1, team2)
goal(matchid, teamid, player, gtime)
eteam(id, teamname, coach)
```
1. Show the matchid and player name for all goals scored by Germany. To identify German players, check for: ```teamid = 'GER'```.
```sql
SELECT matchid, player FROM goal 
WHERE teamid = 'GER';
```
2. Show id, stadium, team1, team2 for just game 1012
```sql
SELECT id,stadium,team1,team2
FROM game
WHERE id=1012;
```
3. Show the player, teamid, stadium and mdate for every German goal.
```sql
SELECT player, teamid, stadium, mdate
FROM game JOIN goal ON (id=matchid)
WHERE teamid = "GER";
```
4. Show the team1, team2 and player for every goal scored by a player called ```Mario player LIKE 'Mario%'```
```sql
SELECT team1, team2, player
FROM game JOIN goal ON (id=matchid)
WHERE player LIKE 'Mario%';
```
5. Show ```player```, ```teamid```, ```coach```, ```gtime``` for all goals scored in the first 10 minutes ```gtime<=10```
```sql
SELECT player, teamid, coach, gtime
FROM goal JOIN eteam ON (teamid=id)
WHERE gtime<=10;
```
6. List the the dates of the matches and the name of the team in which 'Fernando Santos' was the team1 coach.
```sql
SELECT mdate, teamname
FROM game JOIN eteam ON (team1 = eteam.id)
WHERE coach='Fernando Santos';
```
7. List the player for every goal scored in a game where the stadium was 'National Stadium, Warsaw'
```sql
SELECT player
FROM goal JOIN game ON (matchid=id)
WHERE stadium="National Stadium, Warsaw";
```
8. Show the name of all players who scored a goal against Germany. You can use ```teamid!='GER'``` to prevent listing German players. You can use ```DISTINCT``` to stop players being listed twice.
```sql
SELECT DISTINCT player
FROM game JOIN goal ON matchid = id 
WHERE (team1='GER' OR team2='GER') AND teamid!='GER';
```
9. Show teamname and the total number of goals scored.
```sql
SELECT teamname, COUNT(*)
FROM goal JOIN eteam ON goal.teamid=eteam.id
GROUP BY teamname;
```
10. Show the stadium and the number of goals scored in each stadium.
```sql
SELECT stadium, COUNT(*)
FROM game JOIN goal ON (matchid=id)
GROUP BY stadium;
```
11. For every match involving 'POL', show the matchid, date and the number of goals scored.
```sql
SELECT matchid,mdate, COUNT(matchid)
FROM game JOIN goal ON matchid = id 
WHERE (team1 = 'POL' OR team2 = 'POL')
GROUP BY matchid;
```
12. For every match where 'GER' scored, show matchid, match date and the number of goals scored by 'GER'
```sql
SELECT matchid, mdate, count(matchid)
FROM game JOIN goal ON (matchid = id)
WHERE teamid = "GER"
GROUP BY matchid; 
```
13. **(Hard)**List every match with the goals scored by each team as shown. This will use "CASE WHEN" which has not been explained in any previous exercises.
```sql
SELECT mdate,
team1,
SUM(CASE WHEN teamid=team1 THEN 1 ELSE 0 END) score1,
team2,
SUM(CASE WHEN teamid=team2 THEN 1 ELSE 0 END) score2
FROM game LEFT JOIN goal ON matchid = id
GROUP BY game.id
ORDER BY game.mdate, goal.matchid, game.team1, game.team2;
```


### **More JOIN**
```
movie(id, title, yr, director, budget, gross)
actor(id, name)
casting(movieid, actorid, ord)
```
1. List the films where the ```yr``` is 1962 (Show ```id```, ```title```)
```sql
SELECT id, title
FROM movie
WHERE yr=1962;
```
2. Give year of 'Citizen Kane'
```sql
SELECT yr
FROM movie
WHERE title='Citizen Kane';
```
3. List all of the Star Trek movies, include the ```id```, ```title``` and ```yr``` (all of these movies include the words Star Trek in the title). Order results by year.
```sql
SELECT id, title, yr
FROM movie
WHERE title LIKE "%Star Trek%"
ORDER BY yr;
```
4. What id number does the actor 'Glenn Close' have?
```sql
SELECT id 
FROM actor
WHERE name="Glenn Close";
```
5. What is the id of the film 'Casablanca'
```sql
SELECT id
FROM movie
WHERE title="Casablanca";
```
6. Obtain the cast list for 'Casablanca'. Use ```movieid=11768```, (or whatever value you got from the previous question)
```sql
SELECT name
FROM movie 
JOIN casting ON movie.id=casting.movieid
JOIN actor ON actor.id=casting.actorid
WHERE movieid=11768;
```
7. Obtain the cast list for the film 'Alien'
```sql
SELECT name
FROM movie 
JOIN casting ON movie.id=casting.movieid
JOIN actor ON actor.id=casting.actorid
WHERE movie.title='Alien';
```
8. List the films in which 'Harrison Ford' has appeared
```sql
SELECT title
FROM movie 
JOIN casting ON movie.id=casting.movieid
JOIN actor ON actor.id=casting.actorid
WHERE actor.name='Harrison Ford';
```
9. List the films where 'Harrison Ford' has appeared - but not in the starring role. (Note: the ord field of casting gives the position of the actor. If ```ord=1``` then this actor is in the starring role)
```sql
SELECT title
FROM movie 
JOIN casting ON movie.id=casting.movieid
JOIN actor ON actor.id=casting.actorid
WHERE actor.name='Harrison Ford' AND casting.ord!=1;
```
10. List the films together with the leading star for all 1962 films.
```sql
SELECT title, actor.name
FROM movie 
	JOIN casting ON movie.id=casting.movieid
	JOIN actor ON actor.id=casting.actorid
WHERE casting.ord=1 AND movie.yr=1962;
```
11. Which were the busiest years for 'Rock Hudson', show the year and the number of movies he made each year for any year in which he made more than 2 movies.
```sql
SELECT yr, COUNT(title) 
FROM movie 
	JOIN casting ON movie.id=movieid
	JOIN actor   ON actorid=actor.id
WHERE name='Rock Hudson'
GROUP BY yr
HAVING COUNT(title) > 2;
```
12. List the film title and the leading actor for all of the films 'Julie Andrews' played in.
```sql
SELECT title, name 
FROM movie 
	JOIN casting ON movie.id=movieid 
	JOIN actor ON actorid=actor.id
WHERE ord=1 
	AND movieid IN (SELECT movieid FROM casting WHERE actorid IN 
			(SELECT id FROM actor WHERE name='Julie Andrews'));
```
13. Obtain a list, in alphabetical order, of actors who've had at least 15 starring roles.
```sql
SELECT actor.name 
FROM movie 
	JOIN casting ON movie.id=movieid 
	JOIN actor ON actorid=actor.id
WHERE ord=1
GROUP BY actor.name
HAVING COUNT(actor.name)>=15
ORDER BY actor.name;
```
14. List the films released in the year 1978 ordered by the number of actors in the cast, then by title.
```sql
SELECT title, COUNT(actorid) FROM movie JOIN casting ON movie.id=movieid JOIN actor ON actorid=actor.id
WHERE yr=1978
GROUP BY title
ORDER BY COUNT(actorid) DESC, title
```
15. List all the people who have worked with 'Art Garfunkel'.
```sql
SELECT actor.name 
FROM movie 
	JOIN casting ON movie.id=movieid 
	JOIN actor ON actorid=actor.id
WHERE movieid IN (SELECT movieid FROM casting JOIN actor ON actorid=actor.id WHERE actor.name='Art Garfunkel') AND actor.name <> 'Art Garfunkel';
```


### **Using NULL**
```
teacher(id, dept, name, phone, mobile)
dept(id, name)
```
1. List the teachers who have NULL for their department.
```sql
SELECT name
FROM teacher
WHERE dept IS NULL;
```
2. Note the INNER JOIN misses the teachers with no department and the departments with no teacher.
```sql
SELECT teacher.name, dept.name
FROM teacher INNER JOIN dept
	ON (teacher.dept=dept.id);
```
3. Use a different JOIN so that all teachers are listed.
```sql
SELECT teacher.name, dept.name
FROM teacher LEFT JOIN dept
	ON (teacher.dept=dept.id);
```
4. Use a different JOIN so that all departments are listed.
```sql
SELECT teacher.name, dept.name
FROM teacher RIGHT JOIN dept
	ON (teacher.dept=dept.id);
```
5. Use ```COALESCE``` to print the mobile number. Use the number '07986 444 2266' if there is no number given. **Show teacher name and mobile number or '07986 444 2266'**
```sql
SELECT name, COALESCE(mobile, '07986 444 2266')
FROM teacher;
```
6. Use the ```COALESCE``` function and a ```LEFT JOIN``` to print the teacher name and department name. Use the string 'None' where there is no department.
```sql
SELECT teacher.name, COALESCE(dept.name,'None')
FROM teacher LEFT JOIN dept ON teacher.dept=dept.id;
```
7. Use ```COUNT``` to show the number of teachers and the number of mobile phones.
```sql
SELECT COUNT(name), COUNT(mobile)
FROM teachher;
```
8. Use ```COUNT``` and ```GROUP BY dept.name``` to show each department and the number of staff. Use a ```RIGHT JOIN``` to ensure that the Engineering department is listed.
```sql
SELECT dept.name, COUNT(teacher.name)
FROM teacher RIGHT JOIN dept ON teacher.dept=dept.id
GROUP BY dept.name;
```
9. Use ```CASE``` to show the name of each teacher followed by 'Sci' if the teacher is in dept 1 or 2 and 'Art' otherwise.
```sql
SELECT name, CASE WHEN dept=1 or dept=2 THEN 'Sci' ELSE 'Art' END
FROM teacher;
```
10. Use ```CASE``` to show the name of each teacher followed by 'Sci' if the teacher is in dept 1 or 2, show 'Art' if the teacher's dept is 3 and 'None' otherwise.
```sql
SELECT name, 
	CASE WHEN dept=1 or dept=2 THEN 'Sci' 
		WHEN dept=3 THEN 'Art' 
		ELSE 'None' END
FROM teacher;
```


### **Self JOIN**
```
stops(**id**, name)
route(**num**, **company**, **pos**, stop)
```
1. How many stops are in the database.
```sql
SELECT COUNT(*)
FROM stops;
```
2. Find the ```id``` value for the stop 'Craiglockhart'
```sql
SELECT id
FROM stops
WHERE name="Craiglockhart";
```
3. Give the ```id``` and the ```name``` for the ```stops``` on the '4' 'LRT' service.
```sql
SELECT DISTINCT stops.id, stops.name
FROM stops RIGHT JOIN route ON stops.id=route.stop
WHERE num='4' AND company='LRT';
```
4. The query shown gives the number of routes that visit either London Road (149) or Craiglockhart (53). Run the query and notice the two services that link these stops have a count of 2. Add a ```HAVING``` clause to restrict the output to these two routes.
```sql
SELECT company, num, COUNT(*)
FROM route WHERE stop=149 OR stop=53
GROUP BY company, num
HAVING COUNT(*)=2;
```
5. Execute the self join shown and observe that b.stop gives all the places you can get to from Craiglockhart, without changing routes. Change the query so that it shows the services from Craiglockhart to London Road.
```sql
SELECT a.company, a.num, a.stop, b.stop
FROM route a 
  JOIN route b ON (a.company=b.company AND a.num=b.num)
WHERE a.stop=53 AND b.stop=149;
```
6. The query shown is similar to the previous one, however by joining two copies of the stops table we can refer to stops by name rather than by number. Change the query so that the services between 'Craiglockhart' and 'London Road' are shown. If you are tired of these places try 'Fairmilehead' against 'Tollcross'
```sql
SELECT a.company, a.num, stopa.name, stopb.name
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
  JOIN stops stopa ON (a.stop=stopa.id)
  JOIN stops stopb ON (b.stop=stopb.id)
WHERE stopa.name='Craiglockhart' AND stopb.name='London Road';
```
7. Give a list of all the services which connect stops 115 and 137 ('Haymarket' and 'Leith')
```sql
SELECT DISTINCT a.company, a.num
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
WHERE a.stop=115 AND b.stop=137
```
8. Give a list of the services which connect the stops 'Craiglockhart' and 'Tollcross'
```sql
SELECT DISTINCT a.company, a.num
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
  JOIN stops stopa ON (a.stop=stopa.id)
  JOIN stops stopb ON (b.stop=stopb.id)
WHERE stopa.name='Craiglockhart' AND stopb.name='Tollcross';
```
9. Give a distinct list of the stops which may be reached from 'Craiglockhart' by taking one bus, including 'Craiglockhart' itself, offered by the LRT company. Include the company and bus no. of the relevant services.
```sql
SELECT DISTINCT stopb.name, a.company, a.num
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
  JOIN stops stopa ON (a.stop=stopa.id)
  JOIN stops stopb ON (b.stop=stopb.id)
WHERE stopa.name = 'Craiglockhart' AND a.company='LRT';
```
10. Find the routes involving two buses that can go from Craiglockhart to Lochend. Show the bus No. and company for the first bus, the name of the stop for the transfer, and the bus no. and company for the second bus.
```sql
SELECT DISTINCT bus1.num, bus1.company, bus1.name, bus2.num, bus2.company
FROM
 (SELECT a.num, a.company, sb.name
  FROM route a JOIN route b ON (a.company=b.company AND a.num=b.num)
  JOIN stops sa ON (sa.id = a.stop)
  JOIN stops sb ON (sb.id = b.stop)
 WHERE sa.name='Craiglockhart' AND sb.name NOT IN ('Craiglockhart','Lochend')) bus1
JOIN
 (SELECT a.num, a.company, sa.name
  FROM route a JOIN route b ON (a.company=b.company AND a.num=b.num)
  JOIN stops sa ON (sa.id = a.stop)
  JOIN stops sb ON (sb.id = b.stop)
 WHERE sb.name='Lochend' AND sa.name NOT IN ('Craiglockhart','Lochend')) bus2
ON (bus1.name=bus2.name) 
```
**Incorrect, but the answer seems right**

**Why self join?**


### Some useful tips
**FUNCTIONS**
1. ```ROUND(num,-3)``` means round to the nearest 1000
2. ```LEFT(name,1)``` means the first letter of a word
3. ```CONCAT('A','B')``` the output is 'AB'
4. We can use the word ```ALL``` to allow ```>=``` or ```>``` or ```<``` or ```<=``` to act over a list. For example, you can find the largest country in the world, by population with this query:
```sql
SELECT name
FROM world
WHERE population >= ALL(SELECT population
                        FROM world
                        WHERE population>0)
```
5. Different ```JOIN```
- ```INNER JOIN``` = ```JOIN```: only return the matchable records
- ```LEFT JOIN```: return records in the left table
- ```RIGHT JOIN```: return records in the right table
- ```FULL JOIN```: return all records in both tables
6. ```COALESCE``` takes any number of arguments and returns the first value that is not null.
```
COALESCE(x,y,z) = x if x is not NULL
COALESCE(x,y,z) = y if x is NULL and y is not NULL
COALESCE(x,y,z) = z if x and y are NULL but z is not NULL
COALESCE(x,y,z) = NULL if x and y and z are all NULL
```

**NOTATION**
1. ```<>``` means ```!=```
2. ```'% %'``` means space
3. ```ORDER BY 2``` means order by the second field in the selection
```sql
SELECT name, COUNT(movieid)
FROM casting JOIN actor ON actorid=actor.id
WHERE name LIKE 'John %'
GROUP BY name ORDER BY 2 DESC
```

### SOME OTHER USEFUL TOOLS

**DELETE, DROP, UPDATE, ALTER, INSERT**

**CREATE VIEW, TABLE**

**WINDOW FUNCTION**

