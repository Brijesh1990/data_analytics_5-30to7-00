import ttkbootstrap as tb
from ttkbootstrap.constants import *
import datetime
from models.report import SalesReport
from models.order import Order
from utils.helpers import format_currency, format_datetime
from utils.logger import logger

class DashboardView(tb.Frame):
    """
    Overview Dashboard displaying sales KPIs, performance summaries,
    recent orders stream, and operator session logout details.
    """

    def __init__(self, parent, current_user, nav_callback, logout_callback=None):
        super().__init__(parent, padding=15)
        self.current_user = current_user
        self.nav_callback = nav_callback
        self.logout_callback = logout_callback
        self.login_time = datetime.datetime.now().strftime("%I:%M %p")
        self.pack(fill=BOTH, expand=True)

        self._create_widgets()
        self.refresh_dashboard()

    def _create_widgets(self):
        # 1. BOTTOM SECTION: OPERATOR SESSION & LOGOUT PANEL
        # (Packed at side=BOTTOM FIRST to guarantee fixed visibility at bottom)
        session_frame = tb.Labelframe(
            self,
            text=" 👤 OPERATOR SESSION & LOGOUT DETAILS ",
            bootstyle=DANGER,
            padding=12
        )
        session_frame.pack(side=BOTTOM, fill=X, pady=(10, 0))

        # Left side: User info grid
        details_box = tb.Frame(session_frame)
        details_box.pack(side=LEFT, fill=X, expand=True)

        info_line1 = f"Operator: {self.current_user.full_name}  |  Username: @{self.current_user.username}  |  Role: {self.current_user.role.upper()}"
        info_line2 = f"Phone: {self.current_user.phone or 'N/A'}  |  Session Started: {self.login_time}  |  Status: 🟢 Active Session"

        tb.Label(
            details_box,
            text=info_line1,
            font=("Segoe UI", 10, "bold"),
            bootstyle=PRIMARY
        ).pack(anchor=W, pady=(0, 2))

        tb.Label(
            details_box,
            text=info_line2,
            font=("Segoe UI", 9),
            bootstyle=SECONDARY
        ).pack(anchor=W)

        # Right side: Logout Session Action Button
        logout_btn = tb.Button(
            session_frame,
            text="🚪 LOGOUT SESSION",
            bootstyle=DANGER,
            width=20,
            command=self.handle_logout
        )
        logout_btn.pack(side=RIGHT, padx=10)

        # 2. HEADER & WELCOME
        header_frame = tb.Frame(self)
        header_frame.pack(fill=X, pady=(0, 10))

        welcome_lbl = tb.Label(
            header_frame,
            text=f"Welcome back, {self.current_user.full_name}! ({self.current_user.role.upper()})",
            font=("Segoe UI", 16, "bold"),
            bootstyle=PRIMARY
        )
        welcome_lbl.pack(side=LEFT)

        refresh_btn = tb.Button(
            header_frame,
            text="🔄 Refresh Data",
            bootstyle=OUTLINE,
            command=self.refresh_dashboard
        )
        refresh_btn.pack(side=RIGHT)

        # 3. KPI SUMMARY CARDS FRAME
        kpi_frame = tb.Frame(self)
        kpi_frame.pack(fill=X, pady=(0, 10))

        # KPI Card 1: Today's Revenue
        card1 = tb.Labelframe(kpi_frame, text=" TODAY'S SALES ", bootstyle=SUCCESS, padding=10)
        card1.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 8))
        self.lbl_revenue = tb.Label(card1, text="₹ 0.00", font=("Segoe UI", 16, "bold"), bootstyle=SUCCESS)
        self.lbl_revenue.pack()

        # KPI Card 2: Today's Orders
        card2 = tb.Labelframe(kpi_frame, text=" TOTAL ORDERS ", bootstyle=INFO, padding=10)
        card2.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 8))
        self.lbl_orders = tb.Label(card2, text="0 Orders", font=("Segoe UI", 16, "bold"), bootstyle=INFO)
        self.lbl_orders.pack()

        # KPI Card 3: Avg Order Value
        card3 = tb.Labelframe(kpi_frame, text=" AVG ORDER VALUE ", bootstyle=WARNING, padding=10)
        card3.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 8))
        self.lbl_avg_order = tb.Label(card3, text="₹ 0.00", font=("Segoe UI", 16, "bold"), bootstyle=WARNING)
        self.lbl_avg_order.pack()

        # KPI Card 4: Tax Collected
        card4 = tb.Labelframe(kpi_frame, text=" GST COLLECTED ", bootstyle=PRIMARY, padding=10)
        card4.pack(side=LEFT, fill=BOTH, expand=True)
        self.lbl_tax = tb.Label(card4, text="₹ 0.00", font=("Segoe UI", 16, "bold"), bootstyle=PRIMARY)
        self.lbl_tax.pack()

        # 4. QUICK ACTIONS BAR
        actions_frame = tb.Labelframe(self, text=" QUICK ACTIONS ", bootstyle=SECONDARY, padding=8)
        actions_frame.pack(fill=X, pady=(0, 10))

        pos_btn = tb.Button(
            actions_frame,
            text="🛒 Create New Order (F1)",
            bootstyle=SUCCESS,
            width=22,
            command=lambda: self.nav_callback("billing")
        )
        pos_btn.pack(side=LEFT, padx=5)

        history_btn = tb.Button(
            actions_frame,
            text="📜 Order History (Ctrl+H)",
            bootstyle=INFO,
            width=22,
            command=lambda: self.nav_callback("history")
        )
        history_btn.pack(side=LEFT, padx=5)

        if self.current_user.role == "admin":
            menu_btn = tb.Button(
                actions_frame,
                text="🍲 Manage Menu (Ctrl+M)",
                bootstyle=PRIMARY,
                width=22,
                command=lambda: self.nav_callback("menu")
            )
            menu_btn.pack(side=LEFT, padx=5)

            reports_btn = tb.Button(
                actions_frame,
                text="📊 Sales Reports (Ctrl+R)",
                bootstyle=WARNING,
                width=22,
                command=lambda: self.nav_callback("reports")
            )
            reports_btn.pack(side=LEFT, padx=5)

        # 5. RECENT ORDERS TABLE (Fills remaining space)
        recent_frame = tb.Labelframe(self, text=" RECENT ORDERS ", bootstyle=PRIMARY, padding=8)
        recent_frame.pack(fill=BOTH, expand=True)

        columns = ("bill_no", "date", "customer", "type", "payment", "total", "status")
        self.tree = tb.Treeview(recent_frame, columns=columns, show="headings", height=5)

        self.tree.heading("bill_no", text="Bill Number")
        self.tree.heading("date", text="Date & Time")
        self.tree.heading("customer", text="Customer")
        self.tree.heading("type", text="Dining Type")
        self.tree.heading("payment", text="Payment Mode")
        self.tree.heading("total", text="Grand Total")
        self.tree.heading("status", text="Status")

        self.tree.column("bill_no", width=140, anchor=CENTER)
        self.tree.column("date", width=160, anchor=CENTER)
        self.tree.column("customer", width=180, anchor=W)
        self.tree.column("type", width=100, anchor=CENTER)
        self.tree.column("payment", width=120, anchor=CENTER)
        self.tree.column("total", width=120, anchor=E)
        self.tree.column("status", width=100, anchor=CENTER)

        scrollbar = tb.Scrollbar(recent_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

    def handle_logout(self):
        """Executes logout callback or navigation to logout."""
        if self.logout_callback:
            self.logout_callback()
        else:
            self.nav_callback("logout")

    def refresh_dashboard(self):
        """Fetches latest summary metrics and populates recent orders table."""
        stats = SalesReport.get_summary_stats("today")
        self.lbl_revenue.config(text=format_currency(stats.get("total_revenue", 0.0)))
        self.lbl_orders.config(text=f"{stats.get('total_orders', 0)} Orders")
        self.lbl_avg_order.config(text=format_currency(stats.get("avg_order_value", 0.0)))
        self.lbl_tax.config(text=format_currency(stats.get("total_tax", 0.0)))

        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Load recent 20 orders
        orders = Order.get_recent_orders(limit=20)
        for ord_data in orders:
            cust_str = f"{ord_data.get('customer_name') or 'Guest'}"
            if ord_data.get('customer_phone'):
                cust_str += f" ({ord_data.get('customer_phone')})"

            self.tree.insert("", END, values=(
                ord_data.get("bill_number"),
                format_datetime(ord_data.get("created_at")),
                cust_str,
                str(ord_data.get("dining_type")).capitalize(),
                str(ord_data.get("payment_method")).upper(),
                format_currency(ord_data.get("grand_total")),
                str(ord_data.get("order_status")).upper()
            ))
