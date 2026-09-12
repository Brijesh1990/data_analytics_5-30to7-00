import requests
import mysql.connector 
# stablished connection with db
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="web_scraping_db"
)

# check connection 
cursor=connection.cursor();
# write a query to add or insert data 
query="""
insert into products(pname,price,qty) values(%s,%s,%s)
"""

data=(
    "laptop",
    45500,
    1
)

cursor.execute(
    query,
    data
)

connection.commit()
cursor.close()
