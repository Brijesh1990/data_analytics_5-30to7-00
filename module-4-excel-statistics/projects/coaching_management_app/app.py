# import all dependendancy 
import mysql.connector 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as snb
from datetime import datetime
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

# perform crud in this coaching managements systems  .....
# add task create a function 
def add_data():
    
    studentname=input("Enter student Name * :")
    course=input("Enter your course details * :")
    revenue=int(input("Enter your revenue * :"))
    expense=int(input("Enter your expense * :"))
    profit_loss=int(input("Enter profit/loss * :"))
    added_date=datetime.now()
    sql="""
     insert into tbl_coaching_data(studentname,course,revenue,expense,profit_loss,added_date) VALUES (%s,%s,%s,%s,%s,%s)
    """
    data=(studentname,course,revenue,expense,profit_loss,added_date)
    print(data)
    cursor.execute(sql, data)
    db.commit()
    print("Coaching details added successfully")
    
# display coaching data 
def display_data():
    cursor.execute("select * from tbl_coaching_data")
    result=cursor.fetchall()
    print("\n=====display all coaching revenue data =======")
    for i in result:
        print(i)
    
# update data
def update_data():
    taxid=int(input("Enter  id for Update :"))
    studentname=input("Enter student Name * :")
    course=input("Enter your course details * :")
    revenue=int(input("Enter your revenue * :"))
    expense=int(input("Enter your expense * :"))
    profit_loss=int(input("Enter profit/loss * :"))
    added_date=datetime.now()
     
    sql="""
    update tbl_coaching_data set studentname=%s, course=%s,revenue=%s,expense=%s,profit_loss=%s,added_date=%s where taxid=%s
    """
    data=(studentname,course,revenue,expense,profit_loss,added_date,taxid)
    cursor.execute(sql,data)
    db.commit()
    print('Your data successfully updated')
    
# delete data
def delete_data():
    taxid=int(input("Enter data id for delete :"))
    sql="delete from tbl_coaching_data where taxid=%s"
    data=(taxid,)
    cursor.execute(sql,data)
    db.commit()
    print('Data successfully deleted')
    
# create a function for data frames 
def load_df():
    query="select * from tbl_coaching_data"
    df=pd.read_sql(query,db)
    print("\n=====dataframes=======")
    print(df)
    return df 

# create a function for pie chart display data in chart
def showpiechart():
    df = load_df()

    if df.empty:
        print("No data found.")
        return

    plt.figure(figsize=(7,7))

    plt.pie(
        df["profit_loss"],
        labels=df["studentname"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Student Profit/Loss Distribution")
    plt.tight_layout()
    plt.show()
    
# create a function for pie chart display data in chart
def showbarchart():
    df = load_df()

    if df.empty:
        print("No data found.")
        return

    plt.figure(figsize=(10,5))

    plt.bar(
        df["studentname"],
        df["profit_loss"]
    )

    plt.title("Student Profit/Loss")
    plt.xlabel("Student Name")
    plt.ylabel("Profit/Loss")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


while True:
    print(""" 
    ====coaching management systems ====
    1. add coaching data
    2. display all coaching data
    3. update coaching data
    4. delete coaching data
    5. show data in chart
    6. show  data in bar chart
    7. exit
    
     """)
    
    choice=input("Enter your choice :")
    
    if choice=="1":
        add_data()
    elif choice=="2":
       display_data()
    elif choice=="3":
        update_data()   
    elif choice=="4":
        delete_data()
    elif choice=="5":
        showpiechart()    
    elif choice=="6":
        showbarchart()    
    else:
        print("You selected wrong choice")
        break


