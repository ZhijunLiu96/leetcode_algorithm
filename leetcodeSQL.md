
# ORDER BY DIFFICULTY, ACCEPTANCE
## SQL Easy

1350. Students With Invalid Departments
```sql
SELECT id, name
FROM Students
WHERE department_id NOT IN (SELECT d.id FROM Departments as d)
```

1527. Patients With a Condition
```sql
SELECT *
FROM Patients
WHERE conditions LIKE '%_DIAB1%' OR conditions LIKE 'DIAB1%'
```

1303. Find the Team Size
```sql
SELECT a.employee_id, 
		(SELECT COUNT(*) FROM Employee AS b WHERE b.team_id = a.team_id )AS team_size
FROM Employee AS a
```

1378. Replace Employee ID With The Unique Identifier
```sql
SELECT unique_id, name
FROM Employees LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id
```

1484. Group Sold Products By The Date
```sql
SELECT sell_date, 
        COUNT(DISTINCT product) AS num_sold, 
        GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date ASC
```

1068. Product Sales Analysis I
```sql
SELECT product_name, year, price
FROM Sales LEFT JOIN Product ON Sales.product_id = Product.product_id;
```

1069. Product Sales Analysis II
```sql
SELECT product_id, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY product_id;
```

1407. Top Travellers
```sql
SELECT u.name, SUM(IFNULL(r.distance,0)) AS travelled_distance
FROM Users AS u LEFT JOIN Rides AS r ON u.id=r.user_id
GROUP BY u.id
ORDER BY travelled_distance DESC, u.name ASC
```

1251. Average Selling Price
```sql
SELECT r.product_id, round(SUM(r.prices) / SUM(r.units),2) AS average_price
FROM (
    SELECT  u.product_id,
            u.units,
            u.units*(SELECT p.price FROM Prices AS p 
                     WHERE u.purchase_date >= p.start_date 
                        AND u.purchase_date <= p.end_date
                        AND u.product_id = p.product_id) AS prices
    FROM UnitsSold AS u ) AS r
GROUP BY r.product_id
```

511. Game Play Analysis I
```sql
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
```

1179. Reformat Department Table
```sql
select id, 
	MAX(IF(month = 'jan', revenue, null)) as Jan_Revenue,
	sum(case when month = 'feb' then revenue else null end) as Feb_Revenue,
	sum(case when month = 'mar' then revenue else null end) as Mar_Revenue,
	sum(case when month = 'apr' then revenue else null end) as Apr_Revenue,
	sum(case when month = 'may' then revenue else null end) as May_Revenue,
	sum(case when month = 'jun' then revenue else null end) as Jun_Revenue,
	sum(case when month = 'jul' then revenue else null end) as Jul_Revenue,
	sum(case when month = 'aug' then revenue else null end) as Aug_Revenue,
	sum(case when month = 'sep' then revenue else null end) as Sep_Revenue,
	sum(case when month = 'oct' then revenue else null end) as Oct_Revenue,
	sum(case when month = 'nov' then revenue else null end) as Nov_Revenue,
	sum(case when month = 'dec' then revenue else null end) as Dec_Revenue
from department
group by id
order by id
```

1173. Immediate Food Delivery I
```sql
SELECT ROUND(100*(SELECT COUNT(*) AS immediate 
				FROM Delivery as d1 
				WHERE d1.order_date = d1.customer_pref_delivery_date)
				/COUNT(*)
			,2) AS immediate_percentage
FROM Delivery
```

613. Shortest Distance in a Line
```sql
SELECT 
    (CASE WHEN
        (SELECT COUNT(DISTINCT c.x) FROM point c)
         = (SELECT COUNT(d.x) FROM point d)
    THEN
        (SELECT MIN(a.x-b.x)
        FROM point a, point b
        WHERE a.x>b.x ) 
    ELSE 0 
    END) shortest
```

595. Big Countries
```sql
SELECT name, population, area
FROM World
WHERE area > 3000000 OR Population > 25000000;
```

1511. Customer Order Frequency
```sql
SELECT oo.customer_id, c.name
FROM (
    SELECT 
        o.customer_id,
        SUM(CASE WHEN o.order_date like '%-07-%' THEN o.quantity*p.price ELSE 0 END ) t1,
        SUM(CASE WHEN o.order_date like '%-06-%' THEN o.quantity*p.price ELSE 0 END ) t2
    FROM Orders AS o LEFT JOIN Product AS p ON p.product_id=o.product_id
    GROUP BY customer_id) AS oo,
    Customers AS c
WHERE oo.t1>=100 
    AND oo.t2 >= 100
    AND oo.customer_id = c.customer_id
```

1435. Create a Session Bar Chart
```sql
SELECT '[0-5>' AS bin, SUM(CASE WHEN duration >= 0 AND duration < 300 THEN 1 ELSE 0 END) AS total FROM Sessions UNION 
SELECT '[5-10>' AS bin, SUM(CASE WHEN duration >= 300 AND duration < 600 THEN 1 ELSE 0 END) AS total FROM Sessions  UNION 
SELECT '[10-15>' AS bin, SUM(CASE WHEN duration >= 600 AND duration < 900 THEN 1 ELSE 0 END) AS total FROM Sessions UNION 
SELECT '15 or more' AS bin, SUM(CASE WHEN duration >= 900 THEN 1 ELSE 0 END) AS total FROM Sessions 
```

1327. List the Products Ordered in a Period
```sql
SELECT Products.product_name, sum(Orders.unit) AS unit
FROM Orders LEFT JOIN Products ON Products.product_id = Orders.product_id
WHERE Orders.order_date >= '2020-02-01' AND Orders.order_date < '2020-03-01'
GROUP BY Products.product_name
HAVING unit >= 100 
```

1148. Article Views I
```sql
SELECT DISTINCT V.author_id AS id
FROM (SELECT DISTINCT * FROM Views) AS V
WHERE V.author_id = V.viewer_id
ORDER BY id ASC;
```

627. Swap Salary
```sql
UPDATE salary
SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END;
```

586. Customer Placing the Largest Number of Orders
```sql
select customer_number from orders
group by customer_number
order by count(*) desc limit 1;
```

1517. Find Users With Valid E-Mails
```sql
SELECT *
FROM Users
WHERE mail REGEXP '^[a-z|A-Z][A-Z|a-z|0-9|\.\_\-]*\@leetcode\.com$'
```

1280. Students and Examinations
```sql
SELECT s.student_id, s.student_name, ss.subject_name, IFNULL(b.counts,0) attended_exams
FROM (Students s JOIN Subjects ss
    LEFT JOIN (SELECT student_id, subject_name, COUNT(*) counts 
              FROM Examinations
              GROUP BY student_id, subject_name) b
    ON s.student_id = b.student_id AND ss.subject_name= b.subject_name)
ORDER BY student_id ASC, subject_name ASC
```

584. Find Customer Referee
```sql
SELECT name
FROM customer
WHERE referee_id <> 2 OR referee_id IS NULL
```

1082. Sales Analysis I
```sql
SELECT seller_id
FROM  Sales
GROUP BY seller_id
HAVING SUM(price) >= ALL (SELECT SUM(price)
                  FROM Sales
                  GROUP BY seller_id)
```

1050. Actors and Directors Who Cooperated At Least Three Times
```sql
SELECT DISTINCT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3 
```

1543. Fix Product Name Format
```sql
SELECT LOWER(REPLACE(product_name,' ',''))  PRODUCT_NAME,        
        SUBSTRING(sale_date,1,7) SALE_DATE, 
        COUNT(*) TOTAL
FROM Sales
GROUP BY LOWER(REPLACE(product_name,' ','')), SUBSTRING(sale_date,1,7)
ORDER BY 1 ASC, 2 ASC
```

1211. Queries Quality and Percentage
```sql
SELECT  query_name, 
        ROUND(AVG(rating/position),2) quality, 
        ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) poor_query_percentage
FROM Queries
GROUP BY query_name
```

577. Employee Bonus
```sql
SELECT e.name, b.bonus
FROM Employee AS e LEFT JOIN Bonus AS b ON e.empId=b.empId
WHERE b.bonus< 1000 or b.bonus IS NULL
```

620. Not Boring Movies
```sql
SELECT *
FROM cinema
WHERE id%2 = 1 AND description NOT LIKE 'boring'
ORDER BY rating DESC;
```

1241. Number of Comments per Post
```sql
SELECT s.sub_id AS post_id,
	  (SELECT COUNT(DISTINCT s1.sub_id) 
	   FROM Submissions s1 
	   WHERE s1.parent_id = s.sub_id) AS number_of_comments
FROM Submissions s
WHERE s.parent_id IS null
GROUP BY s.sub_id;
```

610. Triangle Judgement
```sql
select *, 
IF(x > 0 AND y > 0 AND z >0 AND x + y > z AND x + z > y AND y + z > x, 'Yes', 'No') AS triangle 
FROM triangle;
```

1075. Project Employees I
```sql
SELECT p.project_id, ROUND(AVG(e.experience_years),2) average_years
FROM Project p LEFT JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id
```

1113. Reported Posts
```sql
SELECT extra AS report_reason, count(DISTINCT post_id) AS report_count
FROM Actions
WHERE action_date = '2019-07-04' AND action='report'
GROUP BY extra;
```

603. Consecutive Available Seats
```sql
select distinct a.seat_id from
    cinema a join cinema b on a.seat_id = b.seat_id + 1 
             or a.seat_id = b.seat_id-1
where a.free = 1 and b.free = 1
order by a.seat_id;
```

1294. Weather Type in Each Country
```sql
SELECT a.country_name,
	CASE WHEN AVG(b.weather_state)<=15 THEN "Cold"
		 WHEN AVG(b.weather_state)>=25 THEN "Hot"
		 ELSE "Warm" END as weather_type 
FROM Countries as a JOIN Weather as b ON a.country_id=b.country_id
WHERE b.day BETWEEN "2019-11-01" AND "2019-11-30"
GROUP BY a.country_id;
```

607. Sales Person
```sql
SELECT s.name
FROM salesperson s
WHERE s.sales_id NOT IN ( SELECT o.sales_id
                        FROM orders o
                        WHERE o.com_id = (SELECT c.com_id
                                        FROM company c
                                        WHERE c.name='RED')  
                        )
```

182. Duplicate Emails
```sql
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*) >1
```

175. Combine Two Tables
```sql
SELECT FirstName, LastName, City, State
FROM Person left join Address
ON Person.PersonId = Address.PersonId;
```

1322. Ads Performance
```sql
SELECT  ad_id,
        IFNULL(ROUND(SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END)/
             SUM(CASE WHEN action = 'Ignored' THEN 0 ELSE 1 END)*100,2),0) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY 2 DESC, 1 ASC
```

181. Employees Earning More Than Their Managers
```sql
SELECT E1.Name AS Employee
FROM Employee E1 LEFT JOIN Employee E2 ON E1.ManagerId = E2.Id
WHERE E1.Salary > E2.Salary
```

512. Game Play Analysis II
```sql
SELECT player_id, device_id
FROM Activity
WHERE (player_id, event_date) IN
      (SELECT player_id, MIN(event_date)
       FROM Activity
       GROUP BY player_id)
```

1084. Sales Analysis III
```sql
SELECT p.product_id, p.product_name
FROM Product p
WHERE p.product_id  IN
                    (SELECT s.product_id
                    FROM Sales s
                    GROUP BY s.product_id
                    HAVING SUM(CASE WHEN s.sale_date >= '2019-01-01' AND s.sale_date <= '2019-03-31'
                                     THEN 0
                                     ELSE 1
                                END)=0)
```

1141. User Activity for the Past 30 Days I
```sql
SELECT activity_date AS day,
    COUNT(DISTINCT user_id) active_users
FROM Activity
WHERE activity_date<='2019-07-27' AND activity_date >='2019-06-28'
GROUP BY activity_date
```

1076. Project Employees II
```sql
SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(*) >= ALL(SELECT COUNT(*)
FROM Project
GROUP BY project_id)
```

183. Customers Who Never Order
```sql
SELECT Name Customers
FROM Customers
WHERE id not IN (SELECT CustomerId FROM Orders);
```

1495. Friendly Movies Streamed Last Month
```sql
SELECT DISTINCT title
FROM Content c JOIN TVProgram t ON c.content_id=t.content_id
WHERE t.program_date LIKE "2020-06%"
    AND c.Kids_content='Y'
    AND c.content_type='Movies'
```

1083. Sales Analysis II
```sql
SELECT DISTINCT s.buyer_id
FROM Sales s
WHERE s.buyer_id IN (SELECT ss.buyer_id FROM Sales ss WHERE ss.product_id=(SELECT p.product_id FROM Product p WHERE p.product_name='S8'))
  AND buyer_id NOT IN (SELECT ss.buyer_id FROM Sales ss WHERE ss.product_id=(SELECT p.product_id FROM Product p WHERE p.product_name='iPhone'))
```

619. Biggest Single Number
```sql
SELECT MAX(t.num) num
FROM(
    SELECT num
    FROM my_numbers
    GROUP BY num
    HAVING COUNT(*)=1) t
```

196. Delete Duplicate Emails
```sql
delete from 
Person
where  
Id not in (select Id 
           from 
            (select min(Id) as Id 
             from Person 
             group by Email
            ) p
          );
```

597. Friend Requests I: Overall Acceptance Rate
```sql
SELECT ROUND(
    IFNULL(
        (SELECT COUNT(*) FROM (SELECT DISTINCT requester_id, accepter_id FROM request_accepted) AS A)
        /
        (SELECT COUNT(*) FROM (SELECT DISTINCT sender_id, send_to_id FROM friend_request) AS B)
        ,0)
    ,2) AS accept_rate
```

197. Rising Temperature
```sql
SELECT w1.Id as Id
FROM Weather as w1, Weather as w2
Where w1.Temperature > w2.Temperature AND w1.RecordDate = dateadd(day,1,w2.recorddate);
```

596. Classes More Than 5 Students
```sql
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;
```

1142. User Activity for the Past 30 Days II
```sql
SELECT IFNULL(ROUND(COUNT(DISTINCT session_id)/COUNT(DISTINCT user_id),2),0.00) AS average_sessions_per_user 
FROM Activity 
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27';
```

176. Second Highest Salary
```sql
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary;
```


## SQL Medium


1393. Capital Gain/Loss
```SQL
SELECT stock_name,
    SUM(CASE WHEN operation='Buy' THEN price*(-1) ELSE price END) capital_gain_loss
FROM Stocks
GROUP BY stock_name
```

1445. Apples & Oranges
```sql
SELECT sale_date,
    SUM(CASE WHEN fruit="apples" THEN sold_num ELSE sold_num*(-1) END) diff
FROM Sales
GROUP BY sale_date
```

1270. All People Report to the Given Manager
```sql
SELECT DISTINCT a.employee_id
FROM Employees a JOIN Employees b ON a.manager_id=b.employee_id
                 JOIN Employees c ON b.manager_id=c.employee_id
WHERE a.employee_id <> 1 AND (a.manager_id=1 OR b.manager_id=1 OR c.manager_id=1)
```

1308. Running Total for Different Genders
```sql
SELECT a.gender, a.day, SUM(b.score_points) total
FROM Scores a JOIN Scores b ON (a.gender=b.gender AND b.day<=a.day)
GROUP BY a.gender, a.day
ORDER BY a.gender ASC, a.day ASC
```

1285. Find the Start and End Number of Continuous Ranges
```sql
SELECT min(log_id) as start_id, max(log_id) as end_id
FROM
(SELECT log_id, ROW_NUMBER() OVER(ORDER BY log_id) as num
FROM Logs) a
GROUP BY log_id - num
```

1398. Customers Who Bought Products A and B but Not C
```sql
SELECT c.customer_id, c.customer_name 
FROM Customers c
WHERE c.customer_id in (SELECT o.customer_id FROM Orders o WHERE o.product_name='A')
  AND c.customer_id in (SELECT o.customer_id FROM Orders o WHERE o.product_name='B')
  AND c.customer_id NOT in (SELECT o.customer_id FROM Orders o WHERE o.product_name='C')
```

1421. NPV Queries
```sql
SELECT q.id, q.year, IFNULL(n.npv,0) npv
FROM Queries q LEFT JOIN NPV n ON (q.id=n.id AND q.year=n.year)
```

1468. Calculate Salaries
```sql
SELECT s.company_id, s.employee_id, s.employee_name, 
    CASE WHEN b.msal < 1000 THEN ROUND(s.salary,0)
         WHEN b.msal >= 1000 AND b.msal <= 10000 THEN ROUND(s.salary*(1-0.24),0)
         ELSE ROUND(s.salary*(1-0.49),0)
    END salary
FROM Salaries s LEFT JOIN (SELECT company_id, MAX(salary) msal FROM Salaries GROUP BY company_id ) b ON s.company_id = b.company_id
```

534. Game Play Analysis III
```sql
SELECT player_id, event_date, SUM(games_played) OVER(PARTITION BY player_id ORDER BY event_date) games_played_so_far
FROM Activity
```

1364. Number of Trusted Contacts of a Customer
```sql
WITH cont AS (
    SELECT user_id, COUNT(*) contacts_cnt
    FROM Contacts
    GROUP BY user_id
),
    trust AS (
    SELECT user_id, 
           SUM( CASE WHEN contact_name IN (SELECT customer_name FROM Customers) THEN 1 ELSE 0 END) trusted_contacts_cnt
    FROM Contacts
    GROUP BY user_id
)

SELECT i.invoice_id, c3.customer_name, i.price, IFNULL(c1.contacts_cnt,0) contacts_cnt , IFNULL(c2.trusted_contacts_cnt,0) trusted_contacts_cnt
FROM Invoices i LEFT JOIN cont c1 ON i.user_id = c1.user_id
                LEFT JOIN trust c2 ON i.user_id = c2.user_id,
     Customers c3
WHERE i.user_id = c3.customer_id
ORDER BY 1 ASC
```

1077. Project Employees III
```sql
WITH maxi AS (
    SELECT p.project_id, MAX(e.experience_years) m
    FROM Project p LEFT JOIN Employee e ON p.employee_id = e.employee_id
    GROUP BY p.project_id
)

SELECT p.project_id, p.employee_id
FROM maxi, Project p LEFT JOIN Employee e ON p.employee_id = e.employee_id
WHERE p.project_id = maxi.project_id AND e.experience_years = maxi.m
```

1532. The Most Recent Three Orders
```sql
WITH temp AS
    (SELECT *,
     DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY customer_id, order_date DESC) AS order_num
    FROM orders)

SELECT c.name customer_name, t.customer_id, t.order_id, t.order_date
FROM temp t, customers c
WHERE c.customer_id = t.customer_id
AND  order_num <=3
ORDER BY 1, 2, 4 DESC
```

1440. Evaluate Boolean Expression
```sql
SELECT left_operand, operator, right_operand,
    (CASE WHEN (e.operator='>' AND v1.value > v2.value) 
            OR (e.operator='=' AND v1.value = v2.value)
            OR (e.operator='<' AND v1.value < v2.value)
        THEN 'true'
        ELSE 'false'
        END) value
FROM Expressions e, Variables v1, Variables v2
WHERE e.left_operand = v1.name AND e.right_operand = v2.name
```

1204. Last Person to Fit in the Elevator
```sql
WITH fulltable AS(
    SELECT *, SUM(weight) OVER (order by turn ASC) AS total
    FROM Queue
)
SELECT person_name
FROM fulltable
WHERE total<=1000
ORDER BY turn DESC
LIMIT 1
```

1112. Highest Grade For Each Student
```sql
SELECT t.student_id, t.course_id, t.grade
FROM 
	(SELECT student_id, course_id, grade, 
	row_number() over (partition by student_id order by grade desc, course_id asc) as r 
	FROM Enrollments) t
WHERE t.r=1
ORDER BY t.student_id asc
```

1355. Activity Participants
```sql
WITH freq AS (
    SELECT activity, COUNT(*) freq
    FROM Friends
    GROUP BY activity
)

SELECT name AS activity
FROM Activities a LEFT JOIN freq f ON a.name= f.activity
WHERE f.freq > (SELECT MIN(freq) FROM freq) AND f.freq<(SELECT MAX(freq) FROM freq)
```

1126. Active Businesses
```sql
WITH mean AS (
    SELECT event_type, AVG(occurences) mean
    FROM Events
    GROUP BY event_type
)

SELECT e.business_id
FROM Events e, mean m
WHERE e.occurences > m.mean AND e.event_type = m.event_type
GROUP BY e.business_id
HAVING COUNT(*)>1
```

1193. Monthly Transactions I
```sql
WITH approve AS (
    SELECT SUBSTRING(trans_date, 1, 7) month,
            country,
            SUM(amount) approved_total_amount,
            COUNT(*) approved_count
    FROM Transactions
    WHERE state = 'approved'
    GROUP BY month, country
),
    total AS (
    SELECT SUBSTRING(trans_date, 1, 7) month,
            country,
            SUM(amount) trans_total_amount,
            COUNT(*) trans_count
    FROM Transactions
    GROUP BY month, country
)

SELECT t.month, t.country, t.trans_count, IFNULL(a.approved_count,0) approved_count, t.trans_total_amount, IFNULL(a.approved_total_amount,0) approved_total_amount
FROM approve a RIGHT JOIN total t
ON (a.month = t.month AND a.country = t.country)
```

1321. Restaurant Growth
```sql
WITH daily AS (
    SELECT visited_on, SUM(amount) amount
    FROM Customer
    GROUP BY visited_on
), 
    moving AS (
    SELECT visited_on, SUM(amount) OVER(ORDER BY visited_on rows BETWEEN 6 PRECEDING AND CURRENT ROW) amount
    FROM daily
),
    mini AS (
    SELECT MIN(visited_on)
    FROM moving
    )

SELECT visited_on, amount, ROUND(amount/7,2) average_amount
FROM moving
WHERE visited_on >= ADDDATE((SELECT * FROM mini), INTERVAL 6 DAY)
```

1045. Customers Who Bought All Products
```sql
SELECT c.customer_id
FROM (SELECT DISTINCT * FROM Customer) c
GROUP BY c.customer_id
HAVING COUNT(*) = (SELECT COUNT(*) FROM Product)
```

1264. Page Recommendations
```sql
WITH friend AS(
    SELECT user1_id, user2_id
    FROM Friendship
    WHERE user1_id=1 OR user2_id=1
)

SELECT DISTINCT page_id recommended_page
FROM Likes
WHERE (user_id IN (SELECT user1_id FROM friend) OR user_id IN (SELECT user2_id FROM friend))
 AND page_id NOT IN (SELECT page_id FROM Likes WHERE user_id=1)
```

608. Tree Node
```sql
SELECT a.id ID, 
    IF(ISNULL(a.p_id), 
       'Root', 
       IF(a.id IN (SELECT DISTINCT p_id FROM tree) ,'Inner', 'Leaf') ) Type
FROM tree a
```

1164. Product Price at a Given Date
```sql
WITH maxi AS(
    SELECT a.product_id, a.new_price
    FROM Products a
    WHERE a.change_date = (SELECT MAX(change_date) FROM Products WHERE change_date <= '2019-08-16' AND product_id = a.product_id)
), 
    prod AS (
        SELECT DISTINCT product_id
        FROM Products 
    )

SELECT a.product_id, IFNULL(b.new_price,10) price
FROM prod a LEFT JOIN maxi b ON a.product_id = b.product_id
ORDER BY price DESC
```

570. Managers with at Least 5 Direct Reports
```sql
WITH manager AS (
    SELECT ManagerId 
    FROM Employee
    GROUP BY ManagerId
    HAVING COUNT(*) >= 5
)

SELECT Name
FROM Employee
WHERE Id IN (SELECT * FROM manager)
```

1501. Countries You Can Safely Invest In
```sql
SELECT Country_name country 
FROM  ((SELECT c.name Country_Name, cl1.duration
        FROM Country c
        JOIN Person p ON c.country_code = LEFT(p.phone_number,3)
        JOIN Calls cl1 ON cl1.caller_id = p.id)
    UNION ALL
        (SELECT c.name Country_Name, cl1.duration
        FROM Country c
        JOIN Person p ON c.country_code = LEFT(p.phone_number,3)
        JOIN Calls cl1 ON cl1.callee_id = p.id)
        ) t1
GROUP BY Country_name
HAVING AVG(duration) > (SELECT AVG(duration) FROM calls)
```

626. Exchange Seats
```sql
SELECT a.id, 
    CASE WHEN a.id%2=0 THEN (SELECT student FROM seat WHERE id = a.id-1)
        ELSE IFNULL((SELECT student FROM seat WHERE id = a.id+1), a.student)
    END student
FROM seat a
```

1158. Market Analysis I
```sql
WITH ord AS (
    SELECT buyer_id, COUNT(*) cnt
    FROM Orders
    WHERE order_date< '2020-01-01' AND order_date >='2019-01-01'
    GROUP BY buyer_id    
)

SELECT u.user_id buyer_id, u.join_date, IFNULL(o.cnt,0) orders_in_2019
FROM Users u LEFT JOIN ord o ON o.buyer_id = u.user_id
```

1459. Rectangles Area
```sql
SELECT a.id p1, b.id p2, ABS(a.x_value-b.x_value)*ABS(a.y_value-b.y_value) area
FROM Points a, Points b
WHERE a.id < b.id AND a.x_value <> b.x_value AND a.y_value <> b.y_value
ORDER BY area DESC, p1 ASC, p2 ASC
```

612. Shortest Distance in a Plane
```sql
SELECT ROUND(MIN(SQRT(POWER(a.x-b.x,2)+POWER(a.y-b.y,2))),2) shortest
FROM point_2d a, point_2d b
WHERE a.x <> b.x OR a.y <> b.y
```

1174. Immediate Food Delivery II
```sql
WITH firstOrder AS (
    SELECT * FROM Delivery d1
    WHERE  order_date <= ALL(SELECT d2.order_date FROM Delivery d2 WHERE d2.customer_id = d1.customer_id)
)

SELECT ROUND((SELECT COUNT(*) FROM firstOrder WHERE order_date= customer_pref_delivery_date)/
(SELECT COUNT(*) FROM firstOrder)*100,2) immediate_percentage
```

1549. The Most Recent Orders for Each Product
```sql
SELECT p.product_name, p.product_id, o.order_id, o.order_date
FROM Orders o, Products p
WHERE o.order_date = (SELECT MAX(order_date) FROM Orders WHERE product_id=p.product_id) 
    AND o.product_id = p.product_id
ORDER BY p.product_name ASC, p.product_id ASC, o.order_id ASC
```

1341. Movie Rating
```sql
    (SELECT u.name results
    FROM Movie_Rating m, Users u
    WHERE u.user_id=m.user_id
    GROUP BY m.user_id
    ORDER BY COUNT(*) DESC, u.name ASC
    LIMIT 1) 
UNION
    (SELECT m1.title reuslts
     FROM Movies m1, Movie_Rating m2
     WHERE SUBSTRING(m2.created_at,1,7)='2020-02'
        AND m1.movie_id=m2.movie_id
     GROUP BY m2.movie_id
     ORDER BY AVG(m2.rating) DESC, m1.title ASC
     LIMIT 1)
```

1212. Team Scores in Football Tournament
```sql

```

585. Investments in 2016
```sql
WITH val2015 AS(
    SELECT TIV_2015
    FROM insurance
    GROUP BY TIV_2015
    HAVING COUNT(*) >1
),
    loc AS(
    SELECT LAT, LON
    FROM insurance
    GROUP BY LAT, LON
    HAVING COUNT(*)=1
    )
    
SELECT SUM(TIV_2016) TIV_2016
FROM insurance 
WHERE TIV_2015 IN (SELECT * FROM val2015)
    AND (LAT,LON) IN (SELECT * FROM loc)
```

602. Friend Requests II: Who Has the Most Friends
```sql
SELECT t.id, COUNT(*) num
FROM
    ((SELECT requester_id id
    FROM request_accepted)
    UNION ALL
    (SELECT accepter_id id
    FROM request_accepted
    ) )t
GROUP BY t.id
ORDER BY num DESC
LIMIT 1
```

1070. Product Sales Analysis III
```sql
WITH miny AS(
    SELECT product_id, MIN(year) mini
    FROM Sales
    GROUP BY product_id
)

SELECT a.product_id, a.year first_year, a.quantity, a.price
FROM Sales a , miny b
WHERE a.product_id = b.product_id
    AND a.year = b.mini
```

580. Count Student Number in Departments
```sql
SELECT d.dept_name, COUNT(s.student_id) AS student_number
FROM department d LEFT JOIN student s ON d.dept_id = s.dept_id
GROUP BY d.dept_name
ORDER BY 2 DESC, 1 ASC
```

1149. Article Views II
```sql
SELECT DISTINCT viewer_id id
FROM Views
GROUP BY view_date, viewer_id
HAVING COUNT(DISTINCT article_id)>1
ORDER BY viewer_id ASC
```

574. Winning Candidate
```sql
SELECT Name
FROM Candidate
WHERE id = (SELECT CandidateId FROM Vote GROUP BY CandidateId ORDER BY COUNT(*) DESC LIMIT 1)
```

178. Rank Scores
```sql
SELECT Score,
DENSE_RANK() OVER(ORDER BY Score DESC) AS Rank
From Scores;
```

550. Game Play Analysis IV
```sql
WITH firstday AS (
    SELECT player_id, MIN(event_date) event_date
    FROM Activity
    GROUP BY player_id), 
     loggin AS(
    SELECT  a.player_id
    FROM firstday a, Activity b
    WHERE a.player_id = b.player_id 
        AND a.event_date = DATE_ADD(b.event_date, INTERVAL -1 DAY)
    GROUP BY a.player_id)
SELECT ROUND((SELECT COUNT( player_id) FROM loggin)/ (SELECT COUNT(DISTINCT player_id) FROM Activity),2) fraction
```

1107. New Users Daily Count
```sql
WITH firstdate AS (
    SELECT user_id, MIN(activity_date) login_date
    FROM Traffic
    WHERE activity='login'
    GROUP BY user_id
)
SELECT login_date, COUNT(*) user_count
FROM firstdate
WHERE login_date BETWEEN DATE_ADD('2019-06-30', INTERVAL -90 DAY) AND '2019-06-30'
GROUP BY login_date
ORDER BY login_date ASC
```

1205. Monthly Transactions II
```sql

```






