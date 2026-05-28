import sqlite3
# create a database 
conn=sqlite3.connect("sms.db")
# print("Database successfully connected")
# create a table inside of sqlite 
cur=conn.cursor()
cur.execute("""
            create  table if not exists students(
                id integer primary key, 
                name text,
                course text, 
                address text
            )
            """)
print("Table created successffully in sms database")
# save query
conn.commit()
conn.close()