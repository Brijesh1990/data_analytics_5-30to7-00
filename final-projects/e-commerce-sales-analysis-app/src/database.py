import mysql.connector

def get_connection():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="e_commerce_dbapp"
        
    )
    return connection