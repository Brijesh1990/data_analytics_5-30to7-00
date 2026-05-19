import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# database connection 
conn=sqlite3.connect("sms.db")
cur=conn.cursor()

# create a table
cur.execute("""
            create  table if not exists employee(
                id integer primary key, 
                name text,
                salary integer, 
                address text,
                company text
            )
            """)

# print("Table created successfully in sms database")

# insert data in table 
insert_data=[
    (1,"brijesh",45500,"150 feet ring road rajkot","Tops technology"),
    
    (2,"het",55500,"150 feet ring road rajkot","Infosys"),
    
    (3,"krish",65500,"150 feet ring road rajkot","HCL"),
    
    (4,"divyang",75500,"150 feet ring road rajkot","TCS"),
    
]

# execute query
cur.executemany("""
                
                insert or replace into employee values(?,?,?,?,?)
                
                """,insert_data)

conn.commit() 

# fetch all data using pandas 
query="select * from employee"
df=pd.read_sql(query, conn)
print(df)


# display in bar chart


# plt.figure(figsize=(7,5))
# plt.bar(df["name"], df["salary"])
# plt.title("employee salary in Bar charts")
# plt.xlabel("employeeName")
# plt.ylabel("employeeSalary")
# plt.grid(True)
# plt.show()


# display all or fetch all data in pie chart 

plt.figure(figsize=(5,5))
plt.pie(
    df["salary"], 
    labels=df["name"], 
    autopct="%1.1f%%"
)

plt.title("Employee salary display in percentage in pie chart")
plt.show()


# display employee name with salary in scatter plot chart 
# plt.figure(figsize=(8,5))
# plt.scatter(df["id"],df["name"],df["salary"])
# plt.title("Employee salary display in scatter plot  chart")
# plt.xlabel("employee Id")
# plt.ylabel("salary")
# plt.grid(True)
# plt.show()