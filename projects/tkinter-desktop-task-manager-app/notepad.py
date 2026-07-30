import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class SimpleNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Notepad")
        self.root.geometry("900x600")

        self.filename = None

        self.create_menu()
        self.create_editor()
        self.create_statusbar()

        self.root.protocol("WM_DELETE_WINDOW", self.exit_app)

    # ---------------- MENU ----------------
    def create_menu(self):
        menubar = tk.Menu(self.root)

        # File
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # View
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Increase Font", command=self.increase_font)
        view_menu.add_command(label="Decrease Font", command=self.decrease_font)
        view_menu.add_command(label="Reset Font", command=self.reset_font)
        menubar.add_cascade(label="View", menu=view_menu)

        # Help
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    # ---------------- EDITOR ----------------
    def create_editor(self):
        frame = ttk.Frame(self.root, padding=5)
        frame.pack(fill=BOTH, expand=True)

        self.text = tk.Text(
            frame,
            wrap="word",
            undo=True,
            font=("Arial", 14),
            padx=10,
            pady=10
        )

        scrollbar = ttk.Scrollbar(
            frame,
            orient=VERTICAL,
            command=self.text.yview
        )

        self.text.configure(yscrollcommand=scrollbar.set)

        self.text.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.text.bind("<KeyRelease>", self.update_status)
        self.text.bind("<ButtonRelease>", self.update_status)

    # ---------------- STATUS BAR ----------------
    def create_statusbar(self):
        self.status = ttk.Label(
            self.root,
            text="Line: 1 | Column: 1",
            bootstyle="secondary",
            anchor=W,
            padding=5
        )
        self.status.pack(fill=X, side=BOTTOM)

    # ---------------- FILE FUNCTIONS ----------------
    def new_file(self):
        self.text.delete("1.0", END)
        self.filename = None
        self.root.title("Simple Notepad")
        self.update_status()

    def open_file(self):
        file = filedialog.askopenfilename(
            title="Open File",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Files", "*.py"),
                ("HTML Files", "*.html"),
                ("All Files", "*.*")
            ]
        )

        if not file:
            return

        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()

            self.text.delete("1.0", END)
            self.text.insert("1.0", content)

            self.filename = file
            self.root.title(f"{file} - Simple Notepad")
            self.update_status()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_file(self):
        if self.filename is None:
            return self.save_as()

        try:
            content = self.text.get("1.0", "end-1c")

            with open(self.filename, "w", encoding="utf-8") as f:
                f.write(content)

            messagebox.showinfo("Saved", "File saved successfully.")
            return True

        except Exception as e:
            messagebox.showerror("Error", str(e))
            return False

    def save_as(self):
        file = filedialog.asksaveasfilename(
            title="Save File",
            defaultextension=".txt",
            filetypes=[
                ("Text Files", "*.txt"),
                ("Python Files", "*.py"),
                ("HTML Files", "*.html"),
                ("All Files", "*.*")
            ]
        )

        if not file:
            return False

        self.filename = file

        if self.save_file():
            self.root.title(f"{file} - Simple Notepad")
            return True

        return False

    # ---------------- EDIT FUNCTIONS ----------------
    def undo(self):
        try:
            self.text.edit_undo()
        except tk.TclError:
            pass

    def redo(self):
        try:
            self.text.edit_redo()
        except tk.TclError:
            pass

    def cut(self):
        self.text.event_generate("<<Cut>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

    def select_all(self):
        self.text.tag_add("sel", "1.0", END)
        self.text.mark_set("insert", "1.0")
        self.text.see("insert")

    # ---------------- FONT FUNCTIONS ----------------
    def increase_font(self):
        current = self.text.cget("font")
        font_size = int(current.split()[-1])
        if font_size < 40:
            self.text.configure(font=("Arial", font_size + 2))

    def decrease_font(self):
        current = self.text.cget("font")
        font_size = int(current.split()[-1])
        if font_size > 8:
            self.text.configure(font=("Arial", font_size - 2))

    def reset_font(self):
        self.text.configure(font=("Arial", 14))

    # ---------------- STATUS ----------------
    def update_status(self, event=None):
        position = self.text.index("insert")
        line, column = position.split(".")
        self.status.config(
            text=f"Line: {line} | Column: {int(column) + 1}"
        )

    # ---------------- HELP ----------------
    def about(self):
        messagebox.showinfo(
            "About",
            "Simple Notepad\n\n"
            "Created using Python Tkinter and ttkbootstrap."
        )

    # ---------------- EXIT ----------------
    def exit_app(self):
        self.root.destroy()


if __name__ == "__main__":
    root = ttk.Window(
        themename="flatly",
        title="Simple Notepad",
        size=(900, 600)
    )

    app = SimpleNotepad(root)

    # Keyboard shortcuts
    root.bind("<Control-n>", lambda e: app.new_file())
    root.bind("<Control-o>", lambda e: app.open_file())
    root.bind("<Control-s>", lambda e: app.save_file())
    root.bind("<Control-z>", lambda e: app.undo())
    root.bind("<Control-y>", lambda e: app.redo())
    root.bind("<Control-a>", lambda e: app.select_all())

    root.mainloop()