# import tkinter gui 
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
# import ttkbootstrap module
import ttkbootstrap as tb
# from ttkbootstrap.constants import *
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb 
import openpyxl as pyxl

# create a mysql connection in tkinter GUI 
con=mysql.connector.connect(
    
    host="localhost",
    user="root",
    password="admin",
    database="tkinterapp_taskapp" 
)

# check connection 
cursor=con.cursor()
print("connections stablish successfully",cursor)


# create an windows for app
app=tb.Window(themename="flatly")
app.title("Task manager app")
app.geometry("550x820")
# create a responsive form for add task data


# create a variables to stored data in variables

task_id=tk.StringVar()
title_var=tk.StringVar()
desc_var=tk.StringVar()
priority_var=tk.StringVar()
status_var=tk.StringVar()
startdate_var=tk.StringVar()
duedate_var=tk.StringVar()

# create all function for crud app 

# for clear the values of input
def clear():
    global task_id
    task_id = ""
    title_var.set("")
    desc_var.set("")
    priority_var.set("")
    status_var.set("")
    startdate_var.set("")
    duedate_var.set("")
    
#create a function for insert data  
def insert_data():
    if title_var.get()=="":
        messagebox.showerror("Error","Title is Required")
        return

    sql="""INSERT INTO tasks
    (title,description,priority,status,start_date,due_date)
    VALUES(%s,%s,%s,%s,%s,%s)"""

    values=(
        title_var.get(),
        desc_var.get(),
        priority_var.get(),
        status_var.get(),
        startdate_var.get(),
        duedate_var.get()
    )
    cursor.execute(sql,values)
    con.commit()
    messagebox.showinfo("Success","Task Added Successfully")
    clear()
    show_data()
    
#create a function for show data  
def show_data():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM tasks")
    rows=cursor.fetchall()
    for row in rows:
        tree.insert("",END,values=row)
    
            
#create a function for select_item data  
def select_item(event):

    global task_id

    selected=tree.focus()

    values=tree.item(selected,"values")

    if values:

        task_id=values[0]

        title_var.set(values[1])
        desc_var.set(values[2])
        priority_var.set(values[3])
        status_var.set(values[4])
        startdate_var.set(values[5])
        duedate_var.set(values[6])
    

def update_data():

    global task_id

    if task_id=="":
        messagebox.showerror("Error","Please Select Task")
        return

    sql="""
    UPDATE tasks SET

    title=%s,
    description=%s,
    priority=%s,
    status=%s,
    start_date=%s,
    due_date=%s

    WHERE id=%s
    """

    values=(

        title_var.get(),
        desc_var.get(),
        priority_var.get(),
        status_var.get(),
        startdate_var.get(),
        duedate_var.get(),
        task_id

    )

    cursor.execute(sql,values)
    con.commit()

    messagebox.showinfo("Updated","Task Updated Successfully")

    clear()
    show_data()
    
      
#create a function for select_item data  
def delete_data():

    global task_id

    if task_id=="":
        messagebox.showerror("Error","Select Task")
        return

    answer=messagebox.askyesno("Delete","Delete Selected Task?")

    if answer:

        cursor.execute("DELETE FROM tasks WHERE id=%s",(task_id,))
        con.commit()

        messagebox.showinfo("Deleted","Task Deleted Successfully")

        clear()
        show_data()
        
                
# create a form 
# Heading
# Create form frame
frame = tb.Frame(app, padding=25)
frame.pack(fill="both", expand=True)

# Heading
tb.Label(
    frame,
    text="📝 Task Manager Application",
    font=("Helvetica", 20, "bold"),
    bootstyle="success"
).grid(row=0, column=0, columnspan=2, pady=(10, 30))

# Title
tb.Label(
    frame,
    text="Enter your Title"
).grid(row=1, column=0, padx=10, pady=(10, 10), sticky="w")

tb.Entry(
    frame,
    textvariable=title_var,
    width=45
).grid(row=1, column=1, padx=10, pady=(10, 10), sticky="ew")

# Description
tb.Label(
    frame,
    text="Enter your Description"
).grid(row=2, column=0, padx=10, pady=(10, 10), sticky="w")

tb.Entry(
    frame,
    textvariable=desc_var,
    width=45
).grid(row=2, column=1, padx=10, pady=(10, 10), sticky="ew")


# priority
tb.Label(
    frame,
    text="Select your priority"
).grid(row=3, column=0, padx=10, pady=(10, 10), sticky="w")

tb.Entry(
    frame,
    textvariable=priority_var,
    width=45
).grid(row=3, column=1, padx=10, pady=(10, 10), sticky="ew")

# 
tb.Label(
    frame,
    text="select your status"
).grid(row=4, column=0, padx=10, pady=(10, 10), sticky="w")

tb.Entry(
    frame,
    textvariable=status_var,
    width=45
).grid(row=4, column=1, padx=10, pady=(10, 10), sticky="ew")

# select start date
tb.Label(
    frame,
    text="Enter your start date"
).grid(row=5, column=0, padx=10, pady=(10, 10), sticky="w")

tb.Entry(
    frame,
    textvariable=startdate_var,
    width=45
).grid(row=5, column=1, padx=10, pady=(10, 10), sticky="ew")

# due date
tb.Label(
    frame,
    text="Enter your Due date"
).grid(row=6, column=0, padx=10, pady=(10, 10), sticky="w")

tb.Entry(
    frame,
    textvariable=duedate_var,
    width=45
).grid(row=6, column=1, padx=10, pady=(10, 10), sticky="ew")

# add task button
tb.Button(
    frame,
    text="➕ Add Task",
    bootstyle="success",
    command=insert_data
).grid(row=7,column=0,pady=10,sticky="ew")

tb.Button(
    frame,
    text="✏ Update",
    bootstyle="warning",
    command=update_data
).grid(row=7,column=1,pady=10,sticky="ew")

tb.Button(
    frame,
    text="🗑 Delete",
    bootstyle="danger",
    command=delete_data
).grid(row=8,column=0,pady=10,sticky="ew")

tb.Button(
    frame,
    text="🔄 Reset",
    bootstyle="secondary",
    command=clear
).grid(row=8,column=1,pady=10,sticky="ew")


# create to display data in tables 
table_frame=tb.Frame(app)
table_frame.pack(fill="both",expand=True,padx=10,pady=10)

scroll=Scrollbar(table_frame)
scroll.pack(side=RIGHT,fill=Y)

tree=ttk.Treeview(

    table_frame,

    columns=(
        "id",
        "title",
        "description",
        "priority",
        "status",
        "start_date",
        "due_date"
    ),

    show="headings",

    yscrollcommand=scroll.set

)

scroll.config(command=tree.yview)

tree.heading("id",text="ID")
tree.heading("title",text="Title")
tree.heading("description",text="Description")
tree.heading("priority",text="Priority")
tree.heading("status",text="Status")
tree.heading("start_date",text="Start Date")
tree.heading("due_date",text="Due Date")

tree.column("id",width=50)
tree.column("title",width=150)
tree.column("description",width=200)
tree.column("priority",width=100)
tree.column("status",width=100)
tree.column("start_date",width=100)
tree.column("due_date",width=100)
tree.pack(fill="both",expand=True)
tree.bind("<ButtonRelease-1>",select_item)


# show desktop app 
app.mainloop()