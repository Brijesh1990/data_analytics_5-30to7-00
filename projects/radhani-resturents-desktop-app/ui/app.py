import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
import datetime
from config import APP_NAME, APP_VERSION, KEYBOARD_SHORTCUTS
from database.connection import DatabaseManager
from models.settings import Settings
from ui.login_view import LoginView
from ui.dashboard_view import DashboardView
from ui.pos_billing_view import POSBillingView
from ui.menu_mgmt_view import MenuManagementView
from ui.order_history_view import OrderHistoryView
from ui.reports_view import ReportsView
from ui.settings_view import SettingsView
from utils.logger import logger

class RajdhaniPOSApp(tb.Window):
    """
    Main Desktop Application Window managing view routing, header navbar,
    role-based authorization, bottom shortcut bar, application exit control, and status bar.
    """

    def __init__(self):
        # Fetch stored theme or default to cosmo
        saved_theme = Settings.get("theme", "cosmo")
        super().__init__(
            title=f"{APP_NAME} v{APP_VERSION}",
            themename=saved_theme,
            size=(1280, 800),
            minsize=(1024, 700)
        )

        self.current_user = None
        self.current_view_name = None
        self.current_view_frame = None

        self._setup_layout()
        self._bind_global_shortcuts()
        self.show_login()

    def _setup_layout(self):
        # Root container
        self.root_frame = tb.Frame(self)
        self.root_frame.pack(fill=BOTH, expand=True)

        # 1. Header Navbar Frame (hidden during login)
        self.navbar = tb.Frame(self.root_frame, padding=10, bootstyle=PRIMARY)

        # Brand Title
        self.brand_lbl = tb.Label(
            self.navbar,
            text="👑 RAJDHANI POS",
            font=("Segoe UI", 14, "bold"),
            bootstyle="inverse-primary"
        )
        self.brand_lbl.pack(side=LEFT, padx=(5, 20))

        # Nav Buttons Frame
        self.nav_btns_frame = tb.Frame(self.navbar, bootstyle=PRIMARY)
        self.nav_btns_frame.pack(side=LEFT)

        # User Badge & Action Controls on Right
        self.right_nav_frame = tb.Frame(self.navbar, bootstyle=PRIMARY)
        self.right_nav_frame.pack(side=RIGHT)

        self.shortcuts_btn = tb.Button(
            self.right_nav_frame,
            text="⌨️ Shortcuts",
            bootstyle="light-outline",
            command=self.show_shortcuts_modal
        )
        self.shortcuts_btn.pack(side=LEFT, padx=5)

        self.user_lbl = tb.Label(
            self.right_nav_frame,
            text="👤 Offline",
            font=("Segoe UI", 10, "bold"),
            bootstyle="inverse-primary"
        )
        self.user_lbl.pack(side=LEFT, padx=10)

        self.logout_btn = tb.Button(
            self.right_nav_frame,
            text="🚪 Logout",
            bootstyle="danger",
            command=self.logout
        )
        self.logout_btn.pack(side=LEFT, padx=5)

        # 2. FIXED BOTTOM CONTROLS & SHORTCUTS BAR
        # (Packed at side=BOTTOM BEFORE central container to guarantee fixed visibility)
        self.bottom_bar = tb.Frame(self.root_frame, padding=(10, 6), bootstyle=DARK)
        self.bottom_bar.pack(fill=X, side=BOTTOM)

        # Left side: Close App & Logout Buttons + Shortcut Badges
        self.bottom_left = tb.Frame(self.bottom_bar, bootstyle=DARK)
        self.bottom_left.pack(side=LEFT)

        self.quit_app_btn = tb.Button(
            self.bottom_left,
            text="❌ CLOSE APP (Alt+F4)",
            bootstyle=DANGER,
            command=self.quit_app
        )
        self.quit_app_btn.pack(side=LEFT, padx=(0, 10))

        self.bottom_logout_btn = tb.Button(
            self.bottom_left,
            text="🚪 Logout",
            bootstyle=WARNING,
            command=self.logout
        )
        self.bottom_logout_btn.pack(side=LEFT, padx=(0, 15))

        # Quick Shortcut Badges
        shortcut_hints = [
            ("F1", "Billing"),
            ("F2", "Clear"),
            ("F3", "Phone"),
            ("F5", "Pay"),
            ("Ctrl+H", "History"),
            ("Esc", "Close Modal")
        ]
        for key_str, label_str in shortcut_hints:
            sc_badge = tb.Label(
                self.bottom_left,
                text=f"[{key_str}] {label_str}",
                font=("Segoe UI", 8, "bold"),
                bootstyle="inverse-dark"
            )
            sc_badge.pack(side=LEFT, padx=5)

        # Right side: Status info & Clock
        self.bottom_right = tb.Frame(self.bottom_bar, bootstyle=DARK)
        self.bottom_right.pack(side=RIGHT)

        self.status_left = tb.Label(self.bottom_right, text="Ready", font=("Segoe UI", 8), bootstyle="inverse-dark")
        self.status_left.pack(side=LEFT, padx=10)

        self.status_clock = tb.Label(self.bottom_right, text="", font=("Segoe UI", 8, "bold"), bootstyle="inverse-dark")
        self.status_clock.pack(side=RIGHT)

        self._update_clock()

        # 3. CENTRAL VIEW CONTAINER AREA
        # (Packed LAST with expand=True to fill middle remaining space)
        self.container = tb.Frame(self.root_frame)
        self.container.pack(fill=BOTH, expand=True)

    def _update_clock(self):
        now_str = datetime.datetime.now().strftime("%Y-%m-%d  %I:%M:%S %p")
        self.status_clock.config(text=now_str)
        self.after(1000, self._update_clock)

    def show_login(self):
        """Displays Login View and hides navbar."""
        self.current_user = None
        self.navbar.pack_forget()
        self.bottom_logout_btn.pack_forget()
        self._clear_container()

        self.current_view_frame = LoginView(self.container, on_login_success=self.on_login_success)
        self.status_left.config(text="Status: Authentication required")

    def on_login_success(self, user):
        """Callback on successful authentication."""
        self.current_user = user
        logger.info(f"User {user.username} ({user.role}) logged in.")

        # Show Navbar & Build Nav Buttons
        self.navbar.pack(fill=X, side=TOP)
        self.bottom_logout_btn.pack(side=LEFT, padx=(0, 15))
        self.user_lbl.config(text=f"👤 {user.full_name} ({user.role.upper()})")
        self._build_nav_buttons()

        # Navigate to default view (POS Billing)
        self.navigate_to("billing")

    def _build_nav_buttons(self):
        for widget in self.nav_btns_frame.winfo_children():
            widget.destroy()

        modules = [
            ("dashboard", "🏠 Dashboard"),
            ("billing", "🛒 POS Billing (F1)"),
            ("history", "📜 Order History (Ctrl+H)")
        ]

        if self.current_user.role == "admin":
            modules.extend([
                ("menu", "🍲 Menu Management (Ctrl+M)"),
                ("reports", "📊 Sales Reports (Ctrl+R)"),
                ("settings", "⚙️ Settings")
            ])

        for mod_id, title in modules:
            btn = tb.Button(
                self.nav_btns_frame,
                text=title,
                bootstyle="inverse-primary",
                command=lambda m=mod_id: self.navigate_to(m)
            )
            btn.pack(side=LEFT, padx=3)

    def navigate_to(self, view_name):
        """Routes application frame to target view."""
        if view_name == "logout":
            self.logout()
            return

        self._clear_container()
        self.current_view_name = view_name

        if view_name == "dashboard":
            self.current_view_frame = DashboardView(
                self.container,
                self.current_user,
                nav_callback=self.navigate_to,
                logout_callback=self.logout
            )
            self.status_left.config(text="Overview Dashboard")
        elif view_name == "billing":
            self.current_view_frame = POSBillingView(self.container, self.current_user)
            self.status_left.config(text="POS Billing Interface | Shortcuts: F1 (Search), F2 (Clear), F3 (Phone), F5 (Pay)")
        elif view_name == "history":
            self.current_view_frame = OrderHistoryView(self.container, self.current_user)
            self.status_left.config(text="Order History & Invoice Reprint")
        elif view_name == "menu":
            self.current_view_frame = MenuManagementView(self.container, self.current_user)
            self.status_left.config(text="Menu Items & Categories Management")
        elif view_name == "reports":
            self.current_view_frame = ReportsView(self.container, self.current_user)
            self.status_left.config(text="Sales Analytics & CSV Reports")
        elif view_name == "settings":
            self.current_view_frame = SettingsView(self.container, self.current_user, on_theme_change=self.set_app_theme)
            self.status_left.config(text="Restaurant Settings & Preferences")

    def _clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def set_app_theme(self, theme_name):
        try:
            self.style.theme_use(theme_name)
            logger.info(f"Changed application theme to '{theme_name}'")
        except Exception as e:
            logger.error(f"Failed to change theme: {e}")

    def logout(self):
        if messagebox.askyesno("Confirm Logout", "Are you sure you want to log out of POS session?", parent=self):
            self.show_login()

    def quit_app(self):
        """Asks confirmation and closes application."""
        if messagebox.askyesno("Exit Application", "Are you sure you want to close Rajdhani POS System?", parent=self):
            logger.info("Closing Rajdhani POS System.")
            self.destroy()

    def show_shortcuts_modal(self):
        dialog = tb.Toplevel(self)
        dialog.title("Keyboard Shortcuts Manual")
        dialog.geometry("450x420")
        dialog.resizable(False, False)
        dialog.grab_set()

        tb.Label(dialog, text="⌨️ KEYBOARD SHORTCUTS REFERENCE", font=("Segoe UI", 12, "bold"), bootstyle=PRIMARY).pack(pady=15)

        table_frame = tb.Frame(dialog, padding=15)
        table_frame.pack(fill=BOTH, expand=True)

        for key, desc in KEYBOARD_SHORTCUTS.items():
            r = tb.Frame(table_frame)
            r.pack(fill=X, pady=3)
            tb.Label(r, text=f"[{key}]", font=("Courier New", 10, "bold"), bootstyle=SUCCESS, width=12).pack(side=LEFT)
            tb.Label(r, text=desc, font=("Segoe UI", 10)).pack(side=LEFT)

        tb.Button(dialog, text="OK (Esc)", bootstyle=SECONDARY, command=dialog.destroy).pack(pady=15)
        dialog.bind("<Escape>", lambda e: dialog.destroy())

    def _bind_global_shortcuts(self):
        self.bind_all("<F1>", lambda e: self._handle_shortcut("F1"))
        self.bind_all("<F2>", lambda e: self._handle_shortcut("F2"))
        self.bind_all("<F3>", lambda e: self._handle_shortcut("F3"))
        self.bind_all("<F4>", lambda e: self._handle_shortcut("F4"))
        self.bind_all("<F5>", lambda e: self._handle_shortcut("F5"))
        self.bind_all("<F8>", lambda e: self._handle_shortcut("F8"))
        self.bind_all("<Control-r>", lambda e: self.navigate_to("reports") if self.current_user and self.current_user.role == "admin" else None)
        self.bind_all("<Control-m>", lambda e: self.navigate_to("menu") if self.current_user and self.current_user.role == "admin" else None)
        self.bind_all("<Control-h>", lambda e: self.navigate_to("history") if self.current_user else None)
        self.bind_all("<Alt-F4>", lambda e: self.quit_app())
        self.bind_all("<Control-q>", lambda e: self.quit_app())

    def _handle_shortcut(self, key):
        if not self.current_user:
            return

        if key == "F1":
            if self.current_view_name != "billing":
                self.navigate_to("billing")
            if isinstance(self.current_view_frame, POSBillingView):
                self.current_view_frame.focus_search()
        elif key == "F2":
            if isinstance(self.current_view_frame, POSBillingView):
                self.current_view_frame.clear_cart()
        elif key == "F3":
            if isinstance(self.current_view_frame, POSBillingView):
                self.current_view_frame.focus_phone()
        elif key == "F4":
            if isinstance(self.current_view_frame, POSBillingView):
                self.current_view_frame.toggle_dining_type()
        elif key == "F5" or key == "F8":
            if isinstance(self.current_view_frame, POSBillingView):
                self.current_view_frame.process_checkout()
