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
app.geometry("500x620")
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
    task_id=""
    title_var.set("")
    desc_var.set("")
    status_var.set("")
    priority_var.set("")
    startdate_var.set("")
    duedate_var.set("")
    
#create a function for insert data  
def insert_data():
    pass

#create a function for show data  
def show_data():
    pass
        
#create a function for update data  
def update_data():
    pass
    
#create a function for select_item data  
def select_item():
    pass
      
#create a function for select_item data  
def delete_data():
    pass
    
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
    command=insert_data, 
    width=60,
).grid(row=6, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

tb.Button(
    frame,
    text="Reset Task",
    bootstyle="danger",
    command=insert_data, 
    width=60,
).grid(row=7, column=0, columnspan=2, padx=10, pady=20, sticky="ew")
# show desktop app 
app.mainloop()