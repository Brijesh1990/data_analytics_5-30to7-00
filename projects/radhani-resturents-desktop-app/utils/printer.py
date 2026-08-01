import os
import tempfile
import platform
import subprocess
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox, scrolledtext
from config import DEFAULT_SETTINGS
from utils.helpers import format_currency, format_datetime
from utils.logger import logger

class ReceiptPrinter:
    """
    Handles thermal receipt formatting, interactive preview dialogs,
    and direct system printer execution.
    """

    @classmethod
    def generate_receipt_text(cls, order_data, order_items, settings=None):
        """
        Generates standard 48-column thermal receipt formatted text.
        """
        if settings is None:
            settings = DEFAULT_SETTINGS

        rest_name = settings.get("restaurant_name", "RAJDHANI RESTAURANT").upper()
        tagline = settings.get("tagline", "Authentic Indian Flavors & Fine Dining")
        address = settings.get("address", "123 Heritage Palace Road, New Delhi")
        phone = settings.get("phone", "+91 98765 43210")
        gstin = settings.get("gstin", "")
        footer = settings.get("receipt_footer", "Thank you for dining with us!")

        bill_no = order_data.get("bill_number", "N/A")
        date_str = format_datetime(order_data.get("created_at"))
        cashier = order_data.get("cashier_name", "Cashier")
        customer_name = order_data.get("customer_name") or "Guest Customer"
        customer_phone = order_data.get("customer_phone") or "N/A"
        dining_type = str(order_data.get("dining_type", "table")).capitalize()
        table_no = order_data.get("table_number", "N/A")
        payment_method = str(order_data.get("payment_method", "cash")).upper()

        width = 44
        sep_double = "=" * width
        sep_single = "-" * width

        lines = []
        # Header
        lines.append(rest_name.center(width))
        if tagline:
            lines.append(tagline.center(width))
        lines.append(address.center(width))
        lines.append(f"Phone: {phone}".center(width))
        if gstin:
            lines.append(f"GSTIN: {gstin}".center(width))
        lines.append(sep_double)

        # Invoice Metadata
        lines.append(f"INVOICE #: {bill_no}")
        lines.append(f"Date/Time: {date_str}")
        lines.append(f"Cashier: {cashier}")
        lines.append(f"Customer: {customer_name} ({customer_phone})")
        lines.append(f"Type: {dining_type} | Table/Ref: {table_no}")
        lines.append(sep_single)

        # Items Header
        # Item Name (22 chars), Qty (4), Rate (8), Amount (10)
        lines.append(f"{'ITEM':<20} {'QTY':>4} {'RATE':>8} {'TOTAL':>10}")
        lines.append(sep_single)

        # Items Rows
        for item in order_items:
            name = item.get("item_name") or item.get("name", "Item")
            if len(name) > 20:
                name = name[:18] + ".."
            qty = item.get("quantity", 1)
            rate = float(item.get("unit_price") or item.get("price", 0.0))
            subtotal = float(item.get("subtotal") or (rate * qty))

            lines.append(f"{name:<20} {qty:>4} {rate:>8.2f} {subtotal:>10.2f}")

        lines.append(sep_single)

        # Totals Math
        subtotal_val = float(order_data.get("subtotal", 0.0))
        discount_val = float(order_data.get("discount_amount", 0.0))
        tax_val = float(order_data.get("tax_amount", 0.0))
        grand_val = float(order_data.get("grand_total", 0.0))
        tax_rate = float(order_data.get("tax_rate", 5.0))

        lines.append(f"{'Subtotal:':<32} ₹ {subtotal_val:>9.2f}")

        if discount_val > 0:
            lines.append(f"{'Discount:':<32}-₹ {discount_val:>9.2f}")

        if tax_val > 0:
            cgst = tax_val / 2.0
            sgst = tax_val / 2.0
            lines.append(f"{f'CGST ({tax_rate/2:.1f}%):':<32} ₹ {cgst:>9.2f}")
            lines.append(f"{f'SGST ({tax_rate/2:.1f}%):':<32} ₹ {sgst:>9.2f}")

        lines.append(sep_double)
        lines.append(f"{'GRAND TOTAL:':<30} ₹ {grand_val:>11.2f}")
        lines.append(sep_double)

        lines.append(f"Payment Mode: {payment_method}")
        lines.append(f"Status: PAID")
        lines.append(sep_single)

        lines.append(footer.center(width))
        lines.append("Powered by Rajdhani POS System".center(width))
        lines.append("\n\n")

        return "\n".join(lines)

    @classmethod
    def print_receipt(cls, receipt_text):
        """
        Sends receipt text to standard OS default printer.
        """
        try:
            # Save receipt to a temporary text file
            with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix="_receipt.txt", encoding="utf-8") as f:
                f.write(receipt_text)
                temp_filename = f.name

            sys_os = platform.system().lower()
            if sys_os == "windows":
                # Use Windows shell print command
                os.startfile(temp_filename, "print")
                logger.info("Sent receipt to default Windows printer.")
            elif sys_os == "darwin" or "linux" in sys_os:
                subprocess.run(["lp", temp_filename], check=False)
                logger.info("Sent receipt to Unix printer spooler via lp.")
            else:
                logger.warning(f"Unsupported OS '{sys_os}' for direct raw printing.")

            return True, "Bill sent to system printer."
        except Exception as e:
            logger.error(f"Printing failed: {e}")
            return False, f"Could not print receipt: {e}"

    @classmethod
    def show_receipt_dialog(cls, parent_window, order_data, order_items, settings=None):
        """
        Displays an interactive Receipt Preview modal with a Print button.
        """
        receipt_str = cls.generate_receipt_text(order_data, order_items, settings)

        dialog = tb.Toplevel(parent_window)
        dialog.title(f"Receipt Preview - Bill #{order_data.get('bill_number')}")
        dialog.geometry("450x650")
        dialog.resizable(False, False)
        dialog.grab_set()

        # Title Label
        title_lbl = tb.Label(
            dialog,
            text=f"Receipt Preview - {order_data.get('bill_number')}",
            font=("Segoe UI", 12, "bold"),
            bootstyle=PRIMARY
        )
        title_lbl.pack(pady=10)

        # Scrolled Text Box for Receipt Content
        txt_box = scrolledtext.ScrolledText(
            dialog,
            width=50,
            height=28,
            font=("Courier New", 10),
            wrap="word",
            background="#1E1E1E" if "dark" in str(dialog.style.theme.name) else "#F8F9FA",
            foreground="#00FF66" if "dark" in str(dialog.style.theme.name) else "#212529"
        )
        txt_box.pack(padx=15, pady=5, fill=BOTH, expand=True)
        txt_box.insert(END, receipt_str)
        txt_box.config(state="disabled")

        # Action Buttons Frame
        btn_frame = tb.Frame(dialog)
        btn_frame.pack(pady=10, fill=X, padx=15)

        def on_print_click():
            success, msg = cls.print_receipt(receipt_str)
            if success:
                messagebox.showinfo("Success", msg, parent=dialog)
            else:
                messagebox.showwarning("Printer Notice", f"{msg}\nReceipt saved to preview.", parent=dialog)

        print_btn = tb.Button(
            btn_frame,
            text="🖨️ Print Receipt (F8)",
            bootstyle=SUCCESS,
            command=on_print_click
        )
        print_btn.pack(side=RIGHT, padx=5)

        close_btn = tb.Button(
            btn_frame,
            text="Close (Esc)",
            bootstyle=SECONDARY,
            command=dialog.destroy
        )
        close_btn.pack(side=RIGHT, padx=5)

        # Bind Esc to close
        dialog.bind("<Escape>", lambda e: dialog.destroy())
        dialog.bind("<F8>", lambda e: on_print_click())
