# import all dependendancy 
import mysql.connector 
import pandas as pd 
import numpy as np 
import matplotlib as plt 
import seaborn as snb
# name="welcome to coaching management app"
# print(name)
# database connection mysql.connector 
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="student_management_app"
)

# check connection is stablished or not 
cursor=db.cursor()
print("student managements connection stablished successfully")
