import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from models.settings import Settings
from models.user import User
from utils.logger import logger

class SettingsView(tb.Frame):
    """
    Admin System Settings interface to modify restaurant information, tax rate,
    receipt footer, theme, and operator passwords.
    """

    def __init__(self, parent, current_user, on_theme_change):
        super().__init__(parent, padding=15)
        self.current_user = current_user
        self.on_theme_change = on_theme_change
        self.pack(fill=BOTH, expand=True)

        self._create_widgets()
        self.load_settings()

    def _create_widgets(self):
        # Title Header
        header = tb.Frame(self)
        header.pack(fill=X, pady=(0, 15))

        tb.Label(
            header,
            text="⚙️ SYSTEM & RESTAURANT SETTINGS",
            font=("Segoe UI", 16, "bold"),
            bootstyle=PRIMARY
        ).pack(side=LEFT)

        # Container Frame
        main_box = tb.Frame(self)
        main_box.pack(fill=BOTH, expand=True)

        # Left Column: Restaurant Profile (60%)
        rest_box = tb.Labelframe(main_box, text=" RESTAURANT INFORMATION & INVOICE PROFILE ", bootstyle=PRIMARY, padding=15)
        rest_box.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

        # Fields
        tb.Label(rest_box, text="Restaurant Name:", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        self.name_entry = tb.Entry(rest_box)
        self.name_entry.pack(fill=X, pady=(0, 10))

        tb.Label(rest_box, text="Tagline:", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        self.tagline_entry = tb.Entry(rest_box)
        self.tagline_entry.pack(fill=X, pady=(0, 10))

        tb.Label(rest_box, text="Address:", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        self.address_entry = tb.Entry(rest_box)
        self.address_entry.pack(fill=X, pady=(0, 10))

        # Phone & Email
        r_pe = tb.Frame(rest_box)
        r_pe.pack(fill=X, pady=(0, 10))

        tb.Label(r_pe, text="Phone:", font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky=W, padx=(0, 10))
        self.phone_entry = tb.Entry(r_pe)
        self.phone_entry.grid(row=1, column=0, sticky=EW, padx=(0, 10))

        tb.Label(r_pe, text="Email:", font=("Segoe UI", 9, "bold")).grid(row=0, column=1, sticky=W)
        self.email_entry = tb.Entry(r_pe)
        self.email_entry.grid(row=1, column=1, sticky=EW)

        r_pe.columnconfigure(0, weight=1)
        r_pe.columnconfigure(1, weight=1)

        # GSTIN & Tax Rate
        r_gt = tb.Frame(rest_box)
        r_gt.pack(fill=X, pady=(0, 10))

        tb.Label(r_gt, text="GSTIN No:", font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky=W, padx=(0, 10))
        self.gstin_entry = tb.Entry(r_gt)
        self.gstin_entry.grid(row=1, column=0, sticky=EW, padx=(0, 10))

        tb.Label(r_gt, text="GST Rate (%):", font=("Segoe UI", 9, "bold")).grid(row=0, column=1, sticky=W)
        self.tax_entry = tb.Entry(r_gt)
        self.tax_entry.grid(row=1, column=1, sticky=EW)

        r_gt.columnconfigure(0, weight=1)
        r_gt.columnconfigure(1, weight=1)

        # Receipt Footer Message
        tb.Label(rest_box, text="Receipt Footer Message:", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        self.footer_entry = tb.Entry(rest_box)
        self.footer_entry.pack(fill=X, pady=(0, 15))

        save_rest_btn = tb.Button(rest_box, text="💾 Save Profile Settings", bootstyle=SUCCESS, command=self.save_restaurant_settings)
        save_rest_btn.pack(fill=X)

        # Right Column: UI Theme & Security (40%)
        right_col = tb.Frame(main_box)
        right_col.pack(side=RIGHT, fill=BOTH, expand=True)

        # Theme Frame
        theme_box = tb.Labelframe(right_col, text=" APPEARANCE & THEME ", bootstyle=INFO, padding=15)
        theme_box.pack(fill=X, pady=(0, 15))

        tb.Label(theme_box, text="UI Theme Palette:", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        self.theme_var = tb.StringVar()
        themes = ["cosmo", "flatly", "superhero", "darkly", "litera", "minty", "pulse", "cyborg", "sandstone"]
        theme_combo = tb.Combobox(theme_box, textvariable=self.theme_var, values=themes, state="readonly")
        theme_combo.pack(fill=X, pady=(0, 10))
        theme_combo.bind("<<ComboboxSelected>>", lambda e: self.change_theme())

        # Password Frame
        pwd_box = tb.Labelframe(right_col, text=" SECURITY & PASSWORD ", bootstyle=WARNING, padding=15)
        pwd_box.pack(fill=X)

        tb.Label(pwd_box, text="New Password:", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        self.pwd_entry = tb.Entry(pwd_box, show="•")
        self.pwd_entry.pack(fill=X, pady=(0, 10))

        tb.Label(pwd_box, text="Confirm Password:", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        self.confirm_pwd_entry = tb.Entry(pwd_box, show="•")
        self.confirm_pwd_entry.pack(fill=X, pady=(0, 15))

        save_pwd_btn = tb.Button(pwd_box, text="🔑 Update Password", bootstyle=WARNING, command=self.change_password)
        save_pwd_btn.pack(fill=X)

    def load_settings(self):
        settings = Settings.get_all()
        self.name_entry.insert(0, settings.get("restaurant_name", ""))
        self.tagline_entry.insert(0, settings.get("tagline", ""))
        self.address_entry.insert(0, settings.get("address", ""))
        self.phone_entry.insert(0, settings.get("phone", ""))
        self.email_entry.insert(0, settings.get("email", ""))
        self.gstin_entry.insert(0, settings.get("gstin", ""))
        self.tax_entry.insert(0, settings.get("tax_rate", "5.0"))
        self.footer_entry.insert(0, settings.get("receipt_footer", ""))
        self.theme_var.set(settings.get("theme", "cosmo"))

    def save_restaurant_settings(self):
        try:
            tax = float(self.tax_entry.get().strip() or 5.0)
        except ValueError:
            messagebox.showwarning("Validation Error", "GST Rate must be a valid number.", parent=self)
            return

        new_settings = {
            "restaurant_name": self.name_entry.get().strip(),
            "tagline": self.tagline_entry.get().strip(),
            "address": self.address_entry.get().strip(),
            "phone": self.phone_entry.get().strip(),
            "email": self.email_entry.get().strip(),
            "gstin": self.gstin_entry.get().strip(),
            "tax_rate": str(tax),
            "receipt_footer": self.footer_entry.get().strip()
        }

        Settings.save_all(new_settings)
        messagebox.showinfo("Success", "Settings updated successfully!", parent=self)

    def change_theme(self):
        new_theme = self.theme_var.get()
        Settings.save_setting("theme", new_theme)
        self.on_theme_change(new_theme)

    def change_password(self):
        pwd = self.pwd_entry.get().strip()
        confirm = self.confirm_pwd_entry.get().strip()

        if not pwd or not confirm:
            messagebox.showwarning("Validation Error", "Please enter new password and confirmation.", parent=self)
            return

        if pwd != confirm:
            messagebox.showerror("Error", "Passwords do not match.", parent=self)
            return

        if len(pwd) < 4:
            messagebox.showwarning("Weak Password", "Password should be at least 4 characters long.", parent=self)
            return

        User.change_password(self.current_user.id, pwd)
        messagebox.showinfo("Success", "Password changed successfully!", parent=self)
        self.pwd_entry.delete(0, END)
        self.confirm_pwd_entry.delete(0, END)
