import sqlite3
# create a database 
conn=sqlite3.connect("sms.db")
# print("Database successfully connected")
# create a table inside of sqlite 
cur=conn.cursor()
cur.execute("""
            insert into students(name,course,address) values('brijesh','DA','150 feet ring road rajkot'),('het','DS','150 feet ring road rajkot'),('krish','DA','150 feet ring road ahemdabad'),('divyang','DA','150 feet ring road badodra')
            
            """)
print("Data inserted   successfully in tables")
# save query
conn.commit()
conn.close()