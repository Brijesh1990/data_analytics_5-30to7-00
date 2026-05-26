# create a database connection mysql 
# create a pandas for data set or data frames 
# create a matplotlib for data visualisation in chart
# install all ....
# pip install pandas matplotlib mysql-connector-python 

# create an app and import all dependancies
import pandas as pd 
import matplotlib.pyplot as plt 
import mysql.connector
# database connection 
db=mysql.connector.connect(
    
    host="localhost",
    user="root", 
    password="admin",
    database="task_manager_appdb"
)

cursor=db.cursor()
print("connection successfully stablished")

# add task create a function 

def add_task():
    title=input("Enter task Name* :")
    priority=input("Enter your task priority* :")
    status=input("Enter your task status* :")
    
    sql="""
     insert into tasks(title,priority,status) VALUES (%s,%s,%s)
    """
    data=(title,priority,status)
    
    print(data)
    cursor.execute(sql, data)
    db.commit()
    print("Task successfully added in tables")
    
# display task
def display_task():
    cursor.execute("select * from tasks")
    result=cursor.fetchall()
    print("\n==========display all task================")
    for i in result:
        print(i)
    
# update task
# def update_task():
    
    
# delete task
def delete_task():
    taskid=int(input("Enter task id for delete :"))
    sql="delete from tasks where id=%s"
    data=(taskid,)
    cursor.execute(sql,data)
    db.commit()
    print('Task successfully deleted')
    
    

while True:
    print(""" 
          
    ====task manager app====
    1. task add
    2. display task
    3. update task
    4. delete task
    5. show task in chart
    6. show in bar chart
    7. exit
    
     """)
    
    choice=input("Enter your choice :")
    
    if choice=="1":
        add_task()
    elif choice=="2":
        display_task()
    # elif choice=="3":
    #     update_task()
    
    elif choice=="4":
        delete_task()
            
        



