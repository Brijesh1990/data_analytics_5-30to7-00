import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from models.user import User
from database.connection import DatabaseManager
from utils.logger import logger

class LoginView(tb.Frame):
    """
    Login Screen supporting Admin & Cashier role authentication.
    """

    def __init__(self, parent, on_login_success):
        super().__init__(parent)
        self.on_login_success = on_login_success
        self.pack(fill=BOTH, expand=True)

        self._create_widgets()

    def _create_widgets(self):
        # Center container
        center_frame = tb.Frame(self)
        center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Card Frame
        card = tb.Labelframe(
            center_frame,
            text=" RAJDHANI RESTAURANT POS LOGIN ",
            bootstyle=PRIMARY,
            padding=30
        )
        card.pack(fill=BOTH, expand=True, ipadx=20, ipady=10)

        # Logo / Title Icon
        title_lbl = tb.Label(
            card,
            text="👑 RAJDHANI RESTAURANT",
            font=("Segoe UI", 18, "bold"),
            bootstyle=PRIMARY
        )
        title_lbl.pack(pady=(0, 5))

        subtitle_lbl = tb.Label(
            card,
            text="Billing & Restaurant Management System",
            font=("Segoe UI", 10),
            bootstyle=SECONDARY
        )
        subtitle_lbl.pack(pady=(0, 20))

        # Username Input
        tb.Label(card, text="Username:", font=("Segoe UI", 10, "bold")).pack(anchor=W, pady=(5, 2))
        self.username_entry = tb.Entry(card, font=("Segoe UI", 11), width=30)
        self.username_entry.pack(pady=(0, 15))
        self.username_entry.focus()

        # Password Input
        tb.Label(card, text="Password:", font=("Segoe UI", 10, "bold")).pack(anchor=W, pady=(5, 2))
        self.password_entry = tb.Entry(card, font=("Segoe UI", 11), width=30, show="•")
        self.password_entry.pack(pady=(0, 20))

        # Quick Login Role Hint
        hint_lbl = tb.Label(
            card,
            text="Default Logins: admin / admin123 | cashier / cashier123",
            font=("Segoe UI", 8, "italic"),
            bootstyle=INFO
        )
        hint_lbl.pack(pady=(0, 15))

        # Login Button
        login_btn = tb.Button(
            card,
            text="🔑 LOGIN TO POS",
            bootstyle=PRIMARY,
            width=28,
            command=self.handle_login
        )
        login_btn.pack(pady=5)

        # Database Status Indicator
        self.db_status_lbl = tb.Label(
            card,
            text="Checking database connection...",
            font=("Segoe UI", 8),
            bootstyle=SECONDARY
        )
        self.db_status_lbl.pack(pady=(15, 0))

        # Bind Enter Key
        self.username_entry.bind("<Return>", lambda e: self.password_entry.focus())
        self.password_entry.bind("<Return>", lambda e: self.handle_login())

        # Check DB status asynchronously
        self.after(500, self.check_db_status)

    def check_db_status(self):
        is_ok, msg = DatabaseManager.test_connection()
        if is_ok:
            self.db_status_lbl.config(text="🟢 Database Connected (MySQL)", bootstyle=SUCCESS)
        else:
            self.db_status_lbl.config(text=f"🔴 DB Offline: {msg[:35]}...", bootstyle=DANGER)

    def handle_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Validation Error", "Please enter both username and password.", parent=self)
            return

        user = User.authenticate(username, password)
        if user:
            self.on_login_success(user)
        else:
            messagebox.showerror("Access Denied", "Invalid username or password.", parent=self)
            self.password_entry.delete(0, END)
