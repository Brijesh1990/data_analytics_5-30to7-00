import tkinter as tk
# pass a message in windows 
import tkinter.messagebox as messagebox
# create a function for user input 
def input_user():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a+b
    return messagebox.showinfo("Additions of Numbers is  :",f"Additions of numbers is  , {c}")
# create a main windows 
root=tk.Tk()
# create a windows titles 
root.title("Additions of numbers")
# create a windows size 
root.geometry("350x300")

# create a label 
label1=tk.Label(root,text="Enter your N1 Numbers  :", font=("Arial", 17))
# create a padding in label 
label1.pack(pady=14)
# create a input 
entry1=tk.Entry(root,text="Enter your name :",font=("Arial",17))
entry1.pack(pady=14)


# create a label 
label2=tk.Label(root,text="Enter your N2 Numbers  :", font=("Arial", 17))
# create a padding in label 
label2.pack(pady=14)
# create a input 
entry2=tk.Entry(root,text="Enter your N2 Numbers :",font=("Arial",17))
entry2.pack(pady=14)

# create an button widgets 
button=tk.Button(root, text="Submit", command=input_user)
button.pack(pady=14)


root.mainloop()