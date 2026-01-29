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


   **syntax**

       