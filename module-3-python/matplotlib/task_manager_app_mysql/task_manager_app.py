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

cursor=db.cursor();
# print("connection successfully stablished")



