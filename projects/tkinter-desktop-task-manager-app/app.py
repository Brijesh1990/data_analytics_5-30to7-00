# import tkinter gui 
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
# import ttkbootstrap module
import ttkbootstrap as tb
from ttkbootstrap.constants import *
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

# display desktop GUI 
# create a main windows 
root=tk.Tk()
# root=Tk()
root.title("Simple Task manager app GUI")
root.geometry("520x550")

# create a label widget
label=tk.Label(root,text="Task Manage App", font=("Arial",19))
# set a positions with border and content and provides padding top to bottom 
label.pack(pady=25)



# show desktop app 
root.mainloop()