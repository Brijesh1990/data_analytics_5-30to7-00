import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import openpyxl
# used sqllite3
import sqlite3
conn=sqlite3.connect("students_management_app")
print("connection successfully",conn)

# create a tables inside of sqlite3
cur=conn.cursor()
cur.execute(
    """ 
    create table if not exists users(
        uid integer primary key autoincrement,
        name text,
        email text,
        phone integer,
        address text,
        picode integer,
        country text,
        state text,
        city text
    )
    """
)

# create students tables 
cur.execute(
    """ 
    create table if not exists students(
        sid integer primary key autoincrement,
        name text,
        email text,
        phone integer,
        address text,
        picode integer,
        collegename text,
        department text,
        country text,
        state text,
        city text
    )
    """
)

# create feedback tables 
cur.execute(
    """ 
    create table if not exists feedback(
        fid integer primary key autoincrement,
        name text,
        email text,
        phone integer,
        comment text
         )
    """
)

# create employee tables 
cur.execute(
    """ 
    create table if not exists employee(
        empid integer primary key autoincrement,
        name text,
        email text,
        phone integer,
        address text,
        salary integer,
        department text,
        picode integer,
        country text,
        state text,
        city text
    )
    """
)

# create employee tables 
cur.execute(
    """ 
    create table if not exists country(
        cid integer primary key autoincrement,
        cname text,
        created_at text
    )
    """
)

# create employee tables 
cur.execute(
    """ 
    create table if not exists state(
        sid integer primary key autoincrement,
        sname text,
        created_at text
    )
    """
)

# create employee tables 
cur.execute(
    """ 
    create table if not exists city(
        ctid integer primary key autoincrement,
        ctname text,
        created_at text
    )
    """
)


# create category tables 
cur.execute(
    """ 
    create table if not exists category(
        catid integer primary key autoincrement,
        catname text
    )
    """
)


# create category tables 
cur.execute(
    """ 
    create table if not exists subcategory(
        subcatid integer primary key autoincrement,
        subcatname text
    )
    """
)


# create products tables 
cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        pid INTEGER PRIMARY KEY AUTOINCREMENT,
        pname TEXT,
        pimage TEXT,
        qty INTEGER,
        price INTEGER,
        catid INTEGER,
        subcatid INTEGER,
        descriptions TEXT,
        added_date TEXT,
        FOREIGN KEY (catid) REFERENCES category(catid),
        FOREIGN KEY (subcatid) REFERENCES subcategory(subcatid)
    )
""")


# stored data or insert in  tables country 
insertCountry=[
                    (1,'india','27-10-2026'),
                    (2,'usa','27-10-2026'),
                    (3,'china','27-10-2026'),
                ]
cur.executemany("""
                insert or replace into country values(?,?,?)
                """,insertCountry)


# stored data or insert in  tables state 
insertState=[
                    (1,'gujrat','27-10-2026'),
                    (2,'california','27-10-2026'),
                    (3,'sanghai','27-10-2026'),
                ]
cur.executemany("""
                insert or replace into state values(?,?,?)
                """,insertState)


# stored data or insert in  tables city 
insertCity=[
                    (1,'rajkot','27-10-2026'),
                    (2,'navada','27-10-2026'),
                    (3,'sanghai city','27-10-2026'),
                ]
cur.executemany("""
                insert or replace into city values(?,?,?)
                """,insertCity)


# stored data or insert in  tables category 
insertCategory=[
                    (1,'electronics'),
                    (2,'furnitures'),
                    
                ]
cur.executemany("""
                insert or replace into category values(?,?)
                """,insertCategory)



# stored data or insert in  tables subcategory 
insertSubcategory=[
                    (1,'mobiles'),
                    (2,'sofa'),
                    
                ]
cur.executemany("""
                insert or replace into subcategory values(?,?)
                """,insertSubcategory)




# stored data or insert in  tables products
insertProd=[
                    (1,'samsung galaxy','samsung.jpg',1,15500,1,1,'good for basics need','27/10/2026'),
                    (2,'3 seater sofa','sofa.jpg',1,35500,2,2,'good for basics need','27/10/2026'),
                    
                ]
cur.executemany("""
                insert or replace into products values(?,?,?,?,?,?,?,?,?)
                """,insertProd)

# print("data succesfully inserted")

# fetch data 
# select="select * from products"
# df=pd.read_sql_query(select,conn)
# print(df)

# fetch data through join 
select="select  products.*,catname,subcatname from products join category on products.catid=category.catid join subcategory on products.subcatid=subcategory.subcatid"
df=pd.read_sql_query(select,conn)
print(df)

# generate data in excels 
generateExcels=df.to_excel("products_list.xlsx", engine='openpyxl', index=False, sheet_name='products_list')
print('excels generated successfully',generateExcels)


# visualizations in chart all products data 
plt.title('show data')
plt.pie(
    df['price'],
    labels=df['pname'], 
    autopct='%1.1f%%'
)

plt.show()

# save query 
conn.commit()
print("table successfully created",conn)
conn.close()
