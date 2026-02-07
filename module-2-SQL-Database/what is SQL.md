# what is SQL ?
  1. sql stands for structured query language
  2. sql is used to create a database and table structured
  3. sql is used as case-insenstive language 
     examples :  INSERT | insert | Insert  
  4. sql is pop based language 
  5. sql create a table structures i.e also called structured data formate 
  6. sql used some commands or query to create a structures (database and table) 

## what is database ? 

   database is stored an information in form of tables 
   
   **list of some database name**

    example : mysql , sqllite , mongodb , oracle , sqlserver, postgre 

## what is tables ?
   **table**
   
   table is stored data in form of column and rows 
   **users**
 | id | name    | email        | password | age | salary |
|----|---------|--------------|----------|-----|--------|
| 1  | brijesh | b@gmail.com  | b123456  | 34  | 89500  |


## what is column and rows in tables ? 

column :column in table also called fieldname 

| id | name    | email        | password | age | salary |
|----|---------|--------------|----------|-----|--------|

   rows : rows in formate of data stored 

   **users**
| id | name     | email              | password | age | salary |
|----|----------|--------------------|----------|-----|--------|
| 1  | brijesh  | b@gmail.com        | b123456  | 34  | 89500  |
| 2  | aman     | aman@gmail.com     | a123456  | 28  | 55000  |
| 3  | priya    | priya@gmail.com    | p123456  | 31  | 72000  |
| 4  | rohit    | rohit@gmail.com    | r123456  | 26  | 48000  |
| 5  | neha     | neha@gmail.com     | n123456  | 29  | 61000  |
| 6  | sumit    | sumit@gmail.com    | s123456  | 35  | 88000  |
| 7  | kavita   | kavita@gmail.com   | k123456  | 32  | 75000  |
| 8  | arjun    | arjun@gmail.com    | ar123456 | 27  | 52000  |
| 9  | pooja    | pooja@gmail.com    | po123456 | 30  | 68000  |
| 10 | rahul    | rahul@gmail.com    | ra123456 | 36  | 92000  |

## types of command in SQL ? 

1. DDL  (data definition language)
2. DML  (data manipulation language)
3. DQL  (data query language)
4. TCL  (transactional control language)             


1. **DDL** 
   stands for data  definition language 
   its create a database and table structures 

   **command or query  in DDL**

   1. create 
   2. alter 
   3. rename 
   4. change 
   5. truncate 
   6. drop 


   **How to create a database**

   **syntax**

   ``` 
   create database database name;

   ```

   **examples**

   ```
   create database data_analytics_app;
   or
   create database data_analytics_flipkart;
   ```

**How to create a table**

**chart of tables create**

| column name    | data types (size)     
|----------------|------------------------------------------------|
| id             | int(default size 11)  primary key auto_increment
| name,email,password| char,varchar(0-255)
| address,message,comment | text
| photo,file,pdf          | varchar(0-255), blob
| dob,date                | date,varchar(0-255)
| datetime                | datetime , varchar(0-255)
| phone                   | int,bigInt(default size 20)
| price                   | int, float, money 
| status (pending | confirmed) | as defined , varchar(0-255) 
| attendance (absent | present) | varchar(0-255), int
| long data               | enum (enumerated)


   **syntax of create table**

   ```
   create table tablename 
   (
    column name datatype(size) auto_increment primary key,
    .
    .
    .
    .
    column name datatype(size)
   )
   ```
   **examples**
   ```
   create table users
(
 user_id int AUTO_INCREMENT primary key,
 name varchar(55),
 password varchar(255),
 age int,
 salary float,
 department varchar(200),
 country varchar(155)   
);
```

## alter : 
   alter is used to add column | modify column | update column | delete column

   **add new column**
   ```
  alter table users add state varchar(255);
   
   ```
   **add new column after particular column**
   ```
  alter table users add photo blob after age;
   
   ```
  **update any column name**
  ```
  alter table users change photo upload_image blob;
  ```
  **delete any columnname**
  ```
  ALTER TABLE `users`
  DROP `age`; 

  or
 
  ALTER TABLE users
  DROP age; 
 
  ```

## change : 
   change the column name using alter 

   ```
  alter table users change photo upload_image blob;
   ```

## add : 
   add new   column name using alter 
   ```
   alter table users add state varchar(255);
   ```
     

## drop 
   drop is used to delete database and table structures 

   1. How to delete database 
     ```
     drop database data_analytics_flipkart;
     ```
     **after drop we never rollback any data**

   2. How to delete table 
     ```
     drop table users;
     ```
     **after drop we never rollback any data in table**


## truncate : 

   truncate is used to empty or removed all data at once time.

   **truncate**
   ```
   truncate table users
   
   ```
   **after truncate we never rollback data**

# rename 
  rename change the table name 

  ```
   rename table users to flip_users 
  ``` 



## what is DML ? 
   DMl stands for data manupulation language 
   DML is used to insert data | delete data | update data

   1. insert 
   2. delete 
   3. update 

   **insert**

   **single data or rows insert**

   ```
   INSERT into tbl_country(countryname) VALUES('india')
   ```
   
   **multiple data or rows insert**

   ```
   INSERT into tbl_country(countryname) VALUES('uk'),('usa'),('china'),('russia')
   ```

   ```
    INSERT into tbl_country VALUES('null','srilanka'),('null','nigeria'),('null','uae'),('null','pakistan')
   ```


   **Insert all columns from one table into another.**

   ```
   INSERT INTO archive_users SELECT * FROM users;

   ```


## delete 

   **delete**    
   1. delete will be used to delete all data from tables 

      ```
      delete from users;
      ```
   2. delete will be used to delete particular data or rows from tables 

      ```
      delete from users where user_id=1;
      or 
      delete from users where name='vishal';
      
      ```   


3. delete will be used to delete using in operator 

      ```
      delete from users where user_id in (3,5);
      
      ```   

      
4. delete will be used to delete using between 

      ```
      delete from users where user_id between 5 and 100;
      
      ```   

      **Note**
      after delete we will rollback our data using TCL


# update the rows or data 

  **update**

  ```
  update users set name='umang',age=35 where user_id=3;
  ```
 

# DQL 
  DQL stands for data query language
  DQL is used to fetch(select) data from tables 
  
  **select**

  1. select all data 

    ```
    select * from users;
    ```
    
  2. select particular  data from id 

    ```
    select * from users where user_id=2;
    ```

    
  3. select particular data from column name

    ```
    select user_id , name from users;
    or 
    
    select user_id , name from users where user_id=5;
    ```

  4. select data apply limit 

     ```
     select * from users where user_id limit 0,2;
     or
     select * from users where user_id limit 2,2;
     or
     select * from users where user_id limit 2,2;
     or
     
     select * from users where user_id limit 1,5;
     or 
     
     select * from users where user_id limit 2,5;
     or
     
     select * from users where user_id limit 4,3;

     ```
  5. select data apply in 

     ```
     select * from users where user_id in (2,4,5,7);
     ```
     
   6. select data apply between 

     ```
     select * from users where user_id between 4 and 7;
     or
     select * from users where user_id between 555 and 999;
     ```

    7. select data by ascending and descending order     

       **order by**
        order by is used to filter data from ascending and descending order   

       **ascending**
       ```
        select * from users order by name asc;
       ```

        ```
        select * from users order by user_id;
       ```
       **descending**
       ```
        select * from users order by name desc;
       ```

        ```
        select * from users order by user_id desc;
       ```

       **group by**
       
       A group by is always work on group of columns 

      ```
       select sum(salary),department from flip_users group by department;
      ```   


      **having**
      having is used to filter data after group by 

      ```
       select sum(salary),department from flip_users group by department having sum(salary)>50000;
      ```      

      **like**
      1. like is used to filter data using pattern matching
      2. like is used to search for specific column data using wildcards 

       **wildcards**
       1. % (percent) : represents zero or more characters
       2. _ (underscore) : represents a single character

       **examples**
      ```
       select * from users where name like 'b%';
       or
       select * from users where name like '%a%';
       or
       select * from users where name like '%a';
       or
       select * from users where name like '_a%';
      ```


## what is sql function
   sql function is used to perform some operations on data and return a single value 
   
   **types of sql function**
   1. aggregate function 
   2. scalar function

   **aggregate function**
   1. count() : count is used to count the number of rows in a table
   2. sum() : sum is used to calculate the total of a numeric column
   3. avg() : avg is used to calculate the average of a numeric column
   4. min() : min is used to find the minimum value in a numeric column
   5. max() : max is used to find the maximum value in a numeric column

   **examples of aggregate function**
   ```
   select count(*) from users;
   or
   select sum(salary) from users;
   or
   select sum(salary) as total_sum_salary from flip_users;
   or
   select avg(salary) as average_salary from flip_users;
   or
   select min(salary) from flip_users;
   or
   select max(salary) from flip_users;
   or
   select department , sum(salary) as total_salary from flip_users group by department; 
   or
   select department , avg(salary) as average_salary from flip_users group by department;
   or
   select department , min(salary) as minimum_salary from flip_users group by department;
   or
   select department , max(salary) as maximum_salary from flip_users group by department;
   or
   select department , count(*) as total_employee from flip_users group by department;
   or
   select department , count(*) as total_employee from flip_users group by department having count(*)>2;
   or
   select department , sum(salary) as total_salary from flip_users group by department having sum(salary)>50000;
   or
   select department , avg(salary) as average_salary from flip_users group by department having avg(salary)>60000;
   or
   select department , min(salary) as minimum_salary from flip_users group by department having min(salary)>50000;

   ```

   **find second highest salary**
    find second highest salary from table used subquery

   ```
   select max(salary) from flip_users where salary < (select max(salary) from flip_users);
   ```


   **scalar function**
   1. upper() : upper is used to convert a string to uppercase
   2. lower() : lower is used to convert a string to lowercase
   3. length() : length is used to find the length of a string
   4. now() : now is used to return the current date and time
   5. date() : date is used to return the current date
   6. time() : time is used to return the current time

   Note: first we will create a table and insert some data then we will apply sql function on that data to understand better

   Note: lastly we will learn about TCL (transactional control language) in next file


   **examples of scalar function**
   ```
   select upper(name) from users;
   or
   select lower(name) from users;
   or
   select length(name) from users;
   or
   select now() from users;
   or
   select date() from users;
   or
   select time() from users;
   or
   select name , upper(name) as uppercase_name from users;
   or
   select name , lower(name) as lowercase_name from users;
   or
   select name , length(name) as name_length from users;
   or
   select name , now() as current_datetime from users;
   or
   select name , date() as current_date from users;
   or
   select name , time() as current_time from users;
   
   ```


## sql key constraints
1. **primary key :** 

     1. primary key is used to uniquely identify each record in a table
     2. primary key is used to create a relationship between two tables
     3. primary key is used to ensure that all values in a column are different
     4. primary key always define on single column.
     5. primary key cannot have null value


     **examples of primary key**

       ```
         create table users
         (
         user_id int AUTO_INCREMENT primary key,
         name varchar(55),
         password varchar(255),
         age int,
         salary float,
         department varchar(200),
         country varchar(155)   
         );
         ```

**examples in fromat**

| user_id | name     | password | age | salary | department | country |
|---------|----------|----------|-----|--------|------------|---------|
| 1       | brijesh  | b123456  | 34  | 89500  | it         | india   |
| 2       | aman     | a123456  | 28  | 55000  | hr         | india   |
| 3       | priya    | p123456  | 31  | 72000  | sales      | india   |
| 4       | rohit    | r123456  | 26  | 48000  | it         | india   |
| 5       | neha     | n123456  | 29  | 61000  | hr         | india   |
| 6       | sumit    | s123456  | 35  | 88000  | sales      | india   |   


 2. **foreign key :**
  1. foreign key is used to establish a relationship between two tables
  2. foreign key is used to ensure referential integrity between two tables
  3. foreign key is used to ensure that the value in a column must match the value in another table's primary key column
  4. foreign key can have null value


  **examples of foreign key**

   **create table country**
 
   |country_id | country_name |
   |-----------|--------------|
   | 1         | india        |
   | 2         | uk           |
   | 3         | usa          |



   **create table users**

| user_id | name     | password | age | salary | department | country_id |
|---------|----------|----------|-----|--------|------------|------------|
| 1       | brijesh  | b123456  | 34  | 89500  | it         | 1          |
| 2       | aman     | a123456  | 28  | 55000  | hr         | 1          |
| 3       | priya    | p123456  | 31  | 72000  | sales      | 1          |
| 4       | rohit    | r123456  | 26  | 48000  | it         | 1          |
| 5       | neha     | n123456  | 29  | | 61000  | hr         | 1        |

**how to create foreign key**

```   
create table users
(
 user_id int AUTO_INCREMENT primary key,
 name varchar(55),
 password varchar(255),
 age int,
 salary float,
 department varchar(200),
 country_id int,
 foreign key (country_id) references country(country_id) 
);

```

3. **unique key :**
  1. unique key is used to ensure that all values in a column are different
  2. unique key is used to create a relationship between two tables
  3. unique key is used to ensure that a column cannot have duplicate values
  4. unique key can have null value one time only
  5. unique key can be defined on single column or multiple columns
 
   **examples of unique key**
   
   ```   
create table users
(
 user_id int AUTO_INCREMENT primary key,
 name varchar(55),
 password varchar(255) unique,
 age int,
 salary float,
 department varchar(200),
 country_id int,
 foreign key (country_id) references country(country_id) 
);

```
  alter table users add unique (email);
```
              
  4. not null : not null is used to ensure that a column cannot have a null value
  5. default : default is used to provide a default value for a column when no value is specified









## TCL (transactional control language)
1. TCL stands for transactional control language
2. TCL is used to manage transactions in a database
3. TCL is used to ensure the integrity of a database
4. TCL is used to rollback a transaction in case of an error
5. TCL is used to commit a transaction to make it permanent in the database


   1. **commit** : commit is used to save the changes made by a transaction to the database

     **syntax**
     ```
       commit;
   ```

   2. **rollback** : rollback is used to undo the changes made by a transaction in case of an error

     **syntax**
     ```
       rollback;
   ```

   **examples of commit and rollback**
   ```
   start transaction;
   delete from users where user_id=2;
   commit;

   delete from users where user_id=1;
   rollback;

   ```
 
   **Note:mysql is not support rollback in structures**


## Home work

  **students based database**

1. create a database named "school"
2. create a table named "students" with the following columns: id (primary key), name, age, grade, and country_id (foreign key referencing the country table).
3. insert at least 5 records into the students table.
4. create a table named "country" with the following columns: country_id (primary key) and country_name.
5. insert at least 3 records into the country table.
6. write a query to select all students along with their country names.
7. write a query to find the average age of students in each grade.
8. write a query to find the total number of students in each country.
9. write a query to find the student with the highest grade.
10. write a query to update the grade of a student with a specific id.
11. write a query to delete a student with a specific id.


  **add to cart based database**
1. create a database named "ecommerce"
2. create a table named "products" with the following columns: product_id (primary key), product_name, price, and stock.
3. insert at least 5 records into the products table.
4. create a table named "customers" with the following columns: customer_id (primary key), customer_name, email, and country_id (foreign key referencing the country table).
5. insert at least 3 records into the customers table.   
6. create a table named "orders" with the following columns: order_id (primary key), customer_id (foreign key referencing the customers table), product_id (foreign key referencing the products table), quantity, and order_date.
7. insert at least 5 records into the orders table.   
8. write a query to select all orders along with customer names and product names.
9. write a query to find the total revenue generated from all orders.
10. write a query to find the most popular product based on the quantity ordered.
11. write a query to update the stock of a product after an order is placed.
12. write a query to delete an order with a specific order_id.


 **faculty based database**
1. create a database named "university"
2. create a table named "faculty" with the following columns: faculty_id (primary key), faculty_name, department, and country_id (foreign key referencing the country table) and provides email as unique key in faculty tables.
3. insert at least 5 records into the faculty table.
4. create a table named "courses" with the following columns: course_id (primary key), course_name, and faculty_id (foreign key referencing the faculty table).
5. insert at least 3 records into the courses table.  
6. create a table named "students" with the following columns: student_id (primary key), student_name, age, and country_id (foreign key referencing the country table).
7. insert at least 5 records into the students table.
8. create a table named "enrollments" with the following columns: enrollment_id (primary key), student_id (foreign key referencing the students table), course_id (foreign key referencing the courses table), and enrollment_date.
9. insert at least 5 records into the enrollments table.
10. write a query to select all enrollments along with student names and course names.
11. write a query to find the total number of students enrolled in each course.
12. write a query to find the faculty member teaching the most courses.
13. write a query to update the department of a faculty member with a specific faculty_id.
14. write a query to delete a student with a specific student_id.

**Note: after creating database and tables you will insert some data in that tables then you will apply all the queries on that data to understand better**

