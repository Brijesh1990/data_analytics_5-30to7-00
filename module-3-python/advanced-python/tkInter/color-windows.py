import tkinter as tk
# create a main windows 
root=tk.Tk()
# create a windows titles 
root.title("simple a windows desktop app")
# create a windows size 
root.geometry("350x300")
# create a label widget
label=tk.Label(root,text="Hello i am Brijesh", fg="blue", font=("Arial",19))
# set a positions with border and content and provides padding top to bottom 
label.pack(pady=25)

# print a window
root.mainloop()

