import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from models.order import Order
from models.settings import Settings
from utils.helpers import format_currency, format_datetime
from utils.printer import ReceiptPrinter
from utils.logger import logger

class OrderHistoryView(tb.Frame):
    """
    Order History interface with multi-criteria search, order details modal,
    bill reprinting, and order cancellation capabilities.
    """

    def __init__(self, parent, current_user):
        super().__init__(parent, padding=15)
        self.current_user = current_user
        self.app_settings = Settings.get_all()
        self.pack(fill=BOTH, expand=True)

        self._create_widgets()
        self.refresh_orders()

    def _create_widgets(self):
        # Header Bar
        header = tb.Frame(self)
        header.pack(fill=X, pady=(0, 15))

        tb.Label(
            header,
            text="📜 ORDER HISTORY & INVOICE REPRINT",
            font=("Segoe UI", 16, "bold"),
            bootstyle=PRIMARY
        ).pack(side=LEFT)

        # Search Filters Bar
        filter_box = tb.Labelframe(self, text=" SEARCH & FILTERS ", bootstyle=SECONDARY, padding=10)
        filter_box.pack(fill=X, pady=(0, 15))

        tb.Label(filter_box, text="Search (Bill # / Phone / Name):", font=("Segoe UI", 9, "bold")).pack(side=LEFT, padx=(0, 5))
        self.search_entry = tb.Entry(filter_box, font=("Segoe UI", 10), width=30)
        self.search_entry.pack(side=LEFT, padx=(0, 15))
        self.search_entry.bind("<KeyRelease>", lambda e: self.refresh_orders())

        search_btn = tb.Button(filter_box, text="🔍 Search", bootstyle=PRIMARY, command=self.refresh_orders)
        search_btn.pack(side=LEFT, padx=5)

        reset_btn = tb.Button(filter_box, text="🔄 Reset", bootstyle=OUTLINE, command=self._reset_filters)
        reset_btn.pack(side=LEFT, padx=5)

        # Action Buttons on Right
        reprint_btn = tb.Button(filter_box, text="🖨️ Reprint Bill", bootstyle=SUCCESS, command=self.reprint_selected)
        reprint_btn.pack(side=RIGHT, padx=5)

        details_btn = tb.Button(filter_box, text="📄 View Line Items", bootstyle=INFO, command=self.view_details)
        details_btn.pack(side=RIGHT, padx=5)

        if self.current_user.role == "admin":
            cancel_btn = tb.Button(filter_box, text="🚫 Cancel Order", bootstyle=DANGER, command=self.cancel_selected)
            cancel_btn.pack(side=RIGHT, padx=5)

        # Orders Table
        table_box = tb.Frame(self)
        table_box.pack(fill=BOTH, expand=True)

        columns = ("bill_no", "date", "customer", "phone", "type", "cashier", "payment", "total", "status")
        self.tree = tb.Treeview(table_box, columns=columns, show="headings")

        self.tree.heading("bill_no", text="Bill Number")
        self.tree.heading("date", text="Date & Time")
        self.tree.heading("customer", text="Customer Name")
        self.tree.heading("phone", text="Phone")
        self.tree.heading("type", text="Dining Type")
        self.tree.heading("cashier", text="Cashier")
        self.tree.heading("payment", text="Payment Mode")
        self.tree.heading("total", text="Grand Total")
        self.tree.heading("status", text="Status")

        self.tree.column("bill_no", width=140, anchor=CENTER)
        self.tree.column("date", width=150, anchor=CENTER)
        self.tree.column("customer", width=160, anchor=W)
        self.tree.column("phone", width=120, anchor=CENTER)
        self.tree.column("type", width=100, anchor=CENTER)
        self.tree.column("cashier", width=130, anchor=W)
        self.tree.column("payment", width=110, anchor=CENTER)
        self.tree.column("total", width=110, anchor=E)
        self.tree.column("status", width=100, anchor=CENTER)

        scrollbar = tb.Scrollbar(table_box, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.tree.bind("<Double-1>", lambda e: self.view_details())

    def _reset_filters(self):
        self.search_entry.delete(0, END)
        self.refresh_orders()

    def refresh_orders(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        query = self.search_entry.get().strip()
        orders = Order.get_recent_orders(limit=100, search_query=query)

        for ord_data in orders:
            self.tree.insert("", END, iid=ord_data["bill_number"], values=(
                ord_data["bill_number"],
                format_datetime(ord_data["created_at"]),
                ord_data.get("customer_name") or "Guest Customer",
                ord_data.get("customer_phone") or "N/A",
                str(ord_data.get("dining_type")).capitalize(),
                ord_data.get("cashier_name"),
                str(ord_data.get("payment_method")).upper(),
                format_currency(ord_data.get("grand_total")),
                str(ord_data.get("order_status")).upper()
            ))

    def view_details(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Order", "Please select an order to view line items.", parent=self)
            return

        bill_no = selected[0]
        order_data = Order.get_order_by_bill_number(bill_no)
        if not order_data:
            return

        items = Order.get_order_items(order_data["id"])

        dialog = tb.Toplevel(self.winfo_toplevel())
        dialog.title(f"Order Details - {bill_no}")
        dialog.geometry("500x500")
        dialog.grab_set()

        tb.Label(dialog, text=f"Order Line Items - Bill #{bill_no}", font=("Segoe UI", 12, "bold"), bootstyle=PRIMARY).pack(pady=10)

        # Meta Info
        meta_lbl = tb.Label(
            dialog,
            text=f"Customer: {order_data.get('customer_name') or 'Guest'} ({order_data.get('customer_phone') or 'N/A'})\n"
                 f"Cashier: {order_data.get('cashier_name')} | Date: {format_datetime(order_data.get('created_at'))}",
            font=("Segoe UI", 9),
            bootstyle=SECONDARY
        )
        meta_lbl.pack(pady=(0, 10))

        # Items Table
        cols = ("item", "qty", "rate", "subtotal")
        tree = tb.Treeview(dialog, columns=cols, show="headings", height=10)
        tree.heading("item", text="Item Name")
        tree.heading("qty", text="Qty")
        tree.heading("rate", text="Unit Price")
        tree.heading("subtotal", text="Subtotal")

        tree.column("item", width=200, anchor=W)
        tree.column("qty", width=60, anchor=CENTER)
        tree.column("rate", width=90, anchor=E)
        tree.column("subtotal", width=100, anchor=E)

        for it in items:
            tree.insert("", END, values=(
                it["item_name"],
                it["quantity"],
                format_currency(it["unit_price"]),
                format_currency(it["subtotal"])
            ))

        tree.pack(fill=BOTH, expand=True, padx=15, pady=5)

        # Total Label
        tot_lbl = tb.Label(
            dialog,
            text=f"Grand Total: {format_currency(order_data.get('grand_total'))}",
            font=("Segoe UI", 12, "bold"),
            bootstyle=SUCCESS
        )
        tot_lbl.pack(pady=10)

    def reprint_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Order", "Please select an order to reprint.", parent=self)
            return

        bill_no = selected[0]
        order_data = Order.get_order_by_bill_number(bill_no)
        if not order_data:
            return

        items = Order.get_order_items(order_data["id"])
        ReceiptPrinter.show_receipt_dialog(self.winfo_toplevel(), order_data, items, self.app_settings)

    def cancel_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Order", "Please select an order to cancel.", parent=self)
            return

        bill_no = selected[0]
        order_data = Order.get_order_by_bill_number(bill_no)
        if not order_data:
            return

        if messagebox.askyesno("Confirm Cancel", f"Are you sure you want to void/cancel Bill #{bill_no}?", parent=self):
            Order.cancel_order(order_data["id"])
            self.refresh_orders()
