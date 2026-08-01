import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from models.report import SalesReport
from utils.helpers import format_currency
from utils.exporter import CSVExporter
from utils.logger import logger

class ReportsView(tb.Frame):
    """
    Sales Reports & Analytics View featuring period selectors, summary KPIs,
    payment method distribution, top selling menu items, and CSV exports.
    """

    def __init__(self, parent, current_user):
        super().__init__(parent, padding=15)
        self.current_user = current_user
        self.current_period = "today"
        self.pack(fill=BOTH, expand=True)

        self._create_widgets()
        self.refresh_reports()

    def _create_widgets(self):
        # Header Bar
        header = tb.Frame(self)
        header.pack(fill=X, pady=(0, 15))

        tb.Label(
            header,
            text="📊 SALES REPORTS & ANALYTICS",
            font=("Segoe UI", 16, "bold"),
            bootstyle=PRIMARY
        ).pack(side=LEFT)

        # Period Filter Buttons
        btn_frame = tb.Frame(header)
        btn_frame.pack(side=RIGHT)

        self.btn_today = tb.Button(btn_frame, text="Today", bootstyle=SUCCESS, command=lambda: self.set_period("today"))
        self.btn_today.pack(side=LEFT, padx=3)

        self.btn_weekly = tb.Button(btn_frame, text="Weekly (7 Days)", bootstyle=OUTLINE, command=lambda: self.set_period("weekly"))
        self.btn_weekly.pack(side=LEFT, padx=3)

        self.btn_monthly = tb.Button(btn_frame, text="Monthly (30 Days)", bootstyle=OUTLINE, command=lambda: self.set_period("monthly"))
        self.btn_monthly.pack(side=LEFT, padx=3)

        export_btn = tb.Button(header, text="📥 Export CSV", bootstyle=INFO, command=self.export_csv)
        export_btn.pack(side=RIGHT, padx=(0, 15))

        # KPI Summary Row
        kpi_frame = tb.Frame(self)
        kpi_frame.pack(fill=X, pady=(0, 20))

        # KPI 1: Revenue
        c1 = tb.Labelframe(kpi_frame, text=" TOTAL REVENUE ", bootstyle=SUCCESS, padding=10)
        c1.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))
        self.lbl_revenue = tb.Label(c1, text="₹ 0.00", font=("Segoe UI", 18, "bold"), bootstyle=SUCCESS)
        self.lbl_revenue.pack()

        # KPI 2: Total Orders
        c2 = tb.Labelframe(kpi_frame, text=" COMPLETED ORDERS ", bootstyle=INFO, padding=10)
        c2.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))
        self.lbl_orders = tb.Label(c2, text="0", font=("Segoe UI", 18, "bold"), bootstyle=INFO)
        self.lbl_orders.pack()

        # KPI 3: Avg Order Value
        c3 = tb.Labelframe(kpi_frame, text=" AVG TICKET VALUE ", bootstyle=WARNING, padding=10)
        c3.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))
        self.lbl_avg = tb.Label(c3, text="₹ 0.00", font=("Segoe UI", 18, "bold"), bootstyle=WARNING)
        self.lbl_avg.pack()

        # KPI 4: Total GST
        c4 = tb.Labelframe(kpi_frame, text=" TOTAL GST COLLECTED ", bootstyle=PRIMARY, padding=10)
        c4.pack(side=LEFT, fill=BOTH, expand=True)
        self.lbl_gst = tb.Label(c4, text="₹ 0.00", font=("Segoe UI", 18, "bold"), bootstyle=PRIMARY)
        self.lbl_gst.pack()

        # Paned Window for Payment Method & Top Items
        paned = tb.Panedwindow(self, orient=HORIZONTAL)
        paned.pack(fill=BOTH, expand=True)

        # Payment Methods Box (40%)
        pm_box = tb.Labelframe(paned, text=" PAYMENT MODE BREAKDOWN ", bootstyle=PRIMARY, padding=10)
        paned.add(pm_box, weight=2)

        pm_cols = ("mode", "count", "revenue")
        self.pm_tree = tb.Treeview(pm_box, columns=pm_cols, show="headings", height=10)
        self.pm_tree.heading("mode", text="Payment Mode")
        self.pm_tree.heading("count", text="Orders")
        self.pm_tree.heading("revenue", text="Total Revenue")

        self.pm_tree.column("mode", width=120, anchor=CENTER)
        self.pm_tree.column("count", width=80, anchor=CENTER)
        self.pm_tree.column("revenue", width=120, anchor=E)
        self.pm_tree.pack(fill=BOTH, expand=True)

        # Top Items Box (60%)
        top_box = tb.Labelframe(paned, text=" TOP SELLING MENU ITEMS ", bootstyle=PRIMARY, padding=10)
        paned.add(top_box, weight=3)

        top_cols = ("item", "category", "qty", "revenue")
        self.top_tree = tb.Treeview(top_box, columns=top_cols, show="headings", height=10)
        self.top_tree.heading("item", text="Item Name")
        self.top_tree.heading("category", text="Category")
        self.top_tree.heading("qty", text="Qty Sold")
        self.top_tree.heading("revenue", text="Total Sales")

        self.top_tree.column("item", width=180, anchor=W)
        self.top_tree.column("category", width=130, anchor=W)
        self.top_tree.column("qty", width=80, anchor=CENTER)
        self.top_tree.column("revenue", width=110, anchor=E)

        top_scroll = tb.Scrollbar(top_box, orient=VERTICAL, command=self.top_tree.yview)
        self.top_tree.configure(yscrollcommand=top_scroll.set)

        self.top_tree.pack(side=LEFT, fill=BOTH, expand=True)
        top_scroll.pack(side=RIGHT, fill=Y)

    def set_period(self, period):
        self.current_period = period
        self.btn_today.config(bootstyle=SUCCESS if period == "today" else OUTLINE)
        self.btn_weekly.config(bootstyle=SUCCESS if period == "weekly" else OUTLINE)
        self.btn_monthly.config(bootstyle=SUCCESS if period == "monthly" else OUTLINE)
        self.refresh_reports()

    def refresh_reports(self):
        # Summary Stats
        stats = SalesReport.get_summary_stats(self.current_period)
        self.lbl_revenue.config(text=format_currency(stats.get("total_revenue")))
        self.lbl_orders.config(text=str(stats.get("total_orders", 0)))
        self.lbl_avg.config(text=format_currency(stats.get("avg_order_value")))
        self.lbl_gst.config(text=format_currency(stats.get("total_tax")))

        # Payment Breakdown Table
        for item in self.pm_tree.get_children():
            self.pm_tree.delete(item)

        pm_data = SalesReport.get_payment_breakdown(self.current_period)
        for row in pm_data:
            self.pm_tree.insert("", END, values=(
                str(row["payment_method"]).upper(),
                row["count"],
                format_currency(row["total_amount"])
            ))

        # Top Items Table
        for item in self.top_tree.get_children():
            self.top_tree.delete(item)

        top_data = SalesReport.get_top_selling_items(self.current_period, limit=15)
        for row in top_data:
            self.top_tree.insert("", END, values=(
                row["item_name"],
                row["category_name"] or "General",
                row["total_qty"],
                format_currency(row["total_sales"])
            ))

    def export_csv(self):
        """Exports top selling items report to CSV file."""
        top_data = SalesReport.get_top_selling_items(self.current_period, limit=100)
        headers = ["item_name", "category_name", "total_qty", "total_sales"]
        success, path_or_msg = CSVExporter.export_to_csv(f"sales_report_{self.current_period}", headers, top_data)
        if success:
            messagebox.showinfo("Export Successful", f"Sales Report exported successfully to:\n{path_or_msg}", parent=self)
        else:
            messagebox.showerror("Export Failed", path_or_msg, parent=self)
