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
						  population/(SELECT population 
									  FROM world
									  WHERE name='Germany')*100
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
8. List each continent and the name of the country that comes first alphabetically. **
```sql
SELECT continent, name
FROM world x
WHERE x.name <= ALL(SELECT name 
					FROM world y 
					WHERE x.continent=y.continent);
```
9. 
```sql

```
10. 
```sql

```

### **SUM and COUNT**
1. 
```sql

```
2. 
```sql

```
3. 
```sql

```
4. 
```sql

```
5. 
```sql

```
6. 
```sql

```
7. 
```sql

```
8. 
```sql

```
9. 
```sql

```
10. 
```sql

```

### **JOIN**
1. 
```sql

```
2. 
```sql

```
3. 
```sql

```
4. 
```sql

```
5. 
```sql

```
6. 
```sql

```
7. 
```sql

```
8. 
```sql

```
9. 
```sql

```
10. 
```sql

```

### **More JOIN**
1. 
```sql

```
2. 
```sql

```
3. 
```sql

```
4. 
```sql

```
5. 
```sql

```
6. 
```sql

```
7. 
```sql

```
8. 
```sql

```
9. 
```sql

```
10. 
```sql

```


### **Using NULL**
1. 
```sql

```
2. 
```sql

```
3. 
```sql

```
4. 
```sql

```
5. 
```sql

```
6. 
```sql

```
7. 
```sql

```
8. 
```sql

```
9. 
```sql

```
10. 
```sql

```



### **Self JOIN**
1. 
```sql

```
2. 
```sql

```
3. 
```sql

```
4. 
```sql

```
5. 
```sql

```
6. 
```sql

```
7. 
```sql

```
8. 
```sql

```
9. 
```sql

```
10. 
```sql

```



### Some useful tips
**FUNCTIONS**
1. ```ROUND(num,-3)``` means round to the nearest 1000
2. ```LEFT(name,1)``` means the first letter of a word
3. ```CONCAT('A','B')``` the output is 'AB'

**NOTATION**
1. ```<>``` means ```!=```
2. ```'% %'``` means ```space```
3. We can use the word ```ALL``` to allow ```>=``` or ```>``` or ```<``` or ```<=``` to act over a list. For example, you can find the largest country in the world, by population with this query:
```sql
SELECT name
FROM world
WHERE population >= ALL(SELECT population
                        FROM world
                        WHERE population>0)
```

