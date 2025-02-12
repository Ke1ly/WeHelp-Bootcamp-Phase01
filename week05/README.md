## Task 02: Create database and table in MySQL server
#### CREATE DATABASE website and CREATE TABLE member
```sql
CREATE DATABASE website;
CREATE TABLE member(
id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
name VARCHAR(255) NOT NULL COMMENT 'Name',
username VARCHAR(255) NOT NULL COMMENT 'Username',
password VARCHAR(255) NOT NULL COMMENT 'Password',
follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time');
```

<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task02.png?raw=true" width=200px>

## Task 03: SQL CRUD
#### INSERT VALUES to the member table
```sql
INSERT INTO member(id, name, username, password, follower_count, time) 
VALUES (1, 'test', 'test', 'test' , 43, CURRENT_TIMESTAMP),
(2,'Diana', 'diananana', 'rjuoiuvjn', 899, CURRENT_TIMESTAMP),
(3, 'Lily', 'lily778', 'ueueue', 173, CURRENT_TIMESTAMP),
(4, 'Oscar', 'oscar___01', 'happyhappy', 405, CURRENT_TIMESTAMP),
(5, 'Bob', 'bobob', 'jjjjjj1234', 234, CURRENT_TIMESTAMP);
```

#### SELECT all rows from the member table
```sql
SELECT * FROM member;
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task03-1&2.png?raw=true" width=550px>

#### SELECT all rows from the member table, in descending order of time
```sql
SELECT * FROM member ORDER BY time DESC;
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task03-3.png?raw=true" width=600px>

#### SELECT total 3 rows, second to fourth, from the member table, in descending order of time
```sql
SELECT * FROM member ORDER BY time DESC
LIMIT 3 OFFSET 1;
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task03-4.png?raw=true" width=600px>

#### SELECT rows where username equals to test
```sql
SELECT * FROM member WHERE username = 'test';
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task03-5.png?raw=true" width=600px>

#### SELECT rows where name includes the es keyword
```sql
SELECT * FROM member WHERE name LIKE '%es%';
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task03-6.png?raw=true" width=600px>

#### SELECT rows where both username and password equal to test
```sql
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task03-7.png?raw=true" width=600px>


#### UPDATE data in name column to test2 where username equals to test
```sql
UPDATE member SET name = 'test2' WHERE username = 'test';
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task03-8.png?raw=true" width=600px>


## Task 04: SQL Aggregation Functions
#### SELECT how many rows from the member table
```sql
SELECT COUNT(*) FROM member;
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task04-1.png?raw=true" width=600px>

#### SELECT the sum of follower_count of all the rows from the member table
```sql
SELECT SUM(follower_count) FROM member;
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task04-2.png?raw=true" width=650px>

#### SELECT the average of follower_count of all the rows from the member table
```sql
SELECT AVG(follower_count) FROM member;
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task04-3.png?raw=true" width=650px>

#### SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table
```sql
SELECT AVG(follower_count) 
FROM (SELECT * FROM member ORDER BY follower_count DESC LIMIT 2) AS top2;
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task04-4.png?raw=true" width=650px>


## Task 05: SQL JOIN
#### CREATE TABLE message in the website database and INSERT VALUES
```sql
CREATE TABLE message (
id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
member_id BIGINT NOT NULL COMMENT 'Member ID for Message Sender',
content VARCHAR(255) NOT NULL COMMENT 'Content',
like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Like Count',
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',
FOREIGN KEY (member_id) REFERENCES member(id));
```

```sql
INSERT INTO message(member_id, content, like_count)
VALUES(1,'Life is a journey, not a destination. Sometimes the best moments happen when you least expect them. 🌙 #Reflect',55),
(1,'Taking a break and enjoying some me-time. How do you unwind?',66),
(2,'Making memories with friends today! Good times, good laughs',677),
(2,'Catching up on my favorite shows and loving every minute of it!',890),
(3,'Feeling grateful for the little things today',135),
(4,'Can’t get enough of this view! Nature truly is the best therapy',399),
(4,'Just found my new favorite song! Cant stop playing it',354),
(4,'Off to explore new places and create unforgettable memories',306),
(5,'Sipping on tea and watching the world go by. There’s something so peaceful about quiet afternoons',220),
(5,'Grabbing a cup of coffee and setting new goals for the week ahead',195);
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task05-1.png?raw=true" width=100%>


#### SELECT all messages, including sender names
```sql
SELECT * FROM message INNER JOIN member ON message.member_id=member.id;
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task05-2.png?raw=true" width=100%>


#### SELECT all messages, including sender names, where sender username equals to test
```sql
SELECT * FROM message INNER JOIN member ON message.member_id=member.id
WHERE username ='test';
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task05-3.png?raw=true" width=100%>


#### get the average like count of messages where sender username equals to test
```sql
SELECT AVG(like_count) FROM message INNER JOIN member ON message.member_id=member.id
WHERE username ='test';
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task05-4.png?raw=true" width=650px>


#### get the average like count of messages GROUP BY sender username
```sql
SELECT member.username, AVG(like_count) FROM message INNER JOIN member ON message.member_id=member.id
GROUP BY member.username;
```
<img src="https://github.com/Ke1ly/WeHelp-Bootcamp-Phase01/blob/main/week05/screenshots%20of%20the%20executing%20results/task05-5.png?raw=true" width=750px>

