import tkinter as tk
# pass a message in windows 
import tkinter.messagebox as messagebox
# create a function for user input 
def input_user():
    user_input=entry.get()
    # print("Your name is :",user_input)
    # pass or print in windows
    return messagebox.showinfo("User Input :",f"Hello , {user_input}")
# create a main windows 
root=tk.Tk()
# create a windows titles 
root.title("take input from users")
# create a windows size 
root.geometry("350x300")

# create a label 
label=tk.Label(root,text="Enter your Name :", font=("Arial", 17))
# create a padding in label 
label.pack(pady=14)
# create a input 
entry=tk.Entry(root,text="Enter your name :",font=("Arial",17))
entry.pack(pady=14)

# create an button widgets 
button=tk.Button(root, text="Submit", command=input_user)
button.pack(pady=14)


root.mainloop()