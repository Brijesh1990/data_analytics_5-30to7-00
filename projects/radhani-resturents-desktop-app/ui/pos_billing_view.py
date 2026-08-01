import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox, simpledialog, Canvas
from models.category import Category
from models.menu_item import MenuItem
from models.customer import Customer
from models.order import Order
from models.settings import Settings
from utils.helpers import format_currency, validate_phone
from utils.printer import ReceiptPrinter
from utils.logger import logger

class POSBillingView(tb.Frame):
    """
    Main Point-of-Sale (POS) Billing Interface.
    Features: Category Tabs, Real-time Search, Menu Cards, Cart Table,
    Customer Lookup, Automatic Calculations, Payment Options, Shortcuts, and Thermal Receipt Printing.
    """

    def __init__(self, parent, current_user):
        super().__init__(parent, padding=10)
        self.current_user = current_user
        self.pack(fill=BOTH, expand=True)

        # Cart State: list of dicts [{'id', 'code', 'name', 'price', 'quantity'}]
        self.cart = []
        self.current_category_id = "0"  # 0 means All

        # Settings Cache
        self.app_settings = Settings.get_all()

        self._create_layout()
        self.load_categories()
        self.load_menu_items()

    def _create_layout(self):
        # PanedWindow splitting Left (Menu Grid) and Right (Cart & Billing)
        paned = tb.Panedwindow(self, orient=HORIZONTAL)
        paned.pack(fill=BOTH, expand=True)

        # Left Frame: Menu Catalog & Search (60% width)
        left_frame = tb.Frame(paned, padding=(0, 0, 10, 0))
        paned.add(left_frame, weight=3)

        # Right Frame: Cart, Customer & Checkout (40% width)
        right_frame = tb.Labelframe(paned, text=" CURRENT ORDER SUMMARY ", bootstyle=PRIMARY, padding=10)
        paned.add(right_frame, weight=2)

        # ==========================================
        # LEFT PANEL WIDGETS
        # ==========================================
        # 1. Search Bar & Shortcuts Hint
        search_frame = tb.Frame(left_frame)
        search_frame.pack(fill=X, pady=(0, 10))

        tb.Label(search_frame, text="🔍 Search (F1):", font=("Segoe UI", 10, "bold")).pack(side=LEFT, padx=(0, 5))
        self.search_entry = tb.Entry(search_frame, font=("Segoe UI", 11))
        self.search_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))
        self.search_entry.bind("<KeyRelease>", lambda e: self.load_menu_items())

        clear_search_btn = tb.Button(search_frame, text="Clear", bootstyle=SECONDARY, command=self._clear_search)
        clear_search_btn.pack(side=RIGHT)

        # 2. Categories Scrollable Buttons Bar
        self.cat_frame = tb.Frame(left_frame)
        self.cat_frame.pack(fill=X, pady=(0, 10))

        # 3. Menu Items Scrollable Container
        self.menu_canvas_frame = tb.Frame(left_frame)
        self.menu_canvas_frame.pack(fill=BOTH, expand=True)

        self.canvas = Canvas(self.menu_canvas_frame, borderwidth=0, highlightthickness=0)
        self.scrollbar = tb.Scrollbar(self.menu_canvas_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scrollable_grid = tb.Frame(self.canvas)

        self.scrollable_grid.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_grid, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Enable Mouse Wheel Scrolling on Canvas
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self.canvas_window, width=e.width))

        # ==========================================
        # RIGHT PANEL WIDGETS (Cart & Billing)
        # ==========================================
        # 1. Customer Details & Dining Type
        cust_frame = tb.Labelframe(right_frame, text=" CUSTOMER & TABLE DETAILS ", bootstyle=INFO, padding=10)
        cust_frame.pack(fill=X, pady=(0, 10))

        # Row 1: Phone + Lookup
        r1 = tb.Frame(cust_frame)
        r1.pack(fill=X, pady=2)
        tb.Label(r1, text="Phone (F3):", font=("Segoe UI", 9, "bold"), width=10).pack(side=LEFT)
        self.cust_phone_entry = tb.Entry(r1, font=("Segoe UI", 10), width=16)
        self.cust_phone_entry.pack(side=LEFT, fill=X, expand=True, padx=(0, 5))
        self.cust_phone_entry.bind("<KeyRelease>", lambda e: self._auto_lookup_customer())

        lookup_btn = tb.Button(r1, text="🔍", bootstyle=INFO, command=self._auto_lookup_customer, width=3)
        lookup_btn.pack(side=RIGHT)

        # Row 2: Customer Name
        r2 = tb.Frame(cust_frame)
        r2.pack(fill=X, pady=2)
        tb.Label(r2, text="Name:", font=("Segoe UI", 9, "bold"), width=10).pack(side=LEFT)
        self.cust_name_entry = tb.Entry(r2, font=("Segoe UI", 10))
        self.cust_name_entry.pack(side=LEFT, fill=X, expand=True)

        # Row 3: Dining Type & Table Selector
        r3 = tb.Frame(cust_frame)
        r3.pack(fill=X, pady=2)
        tb.Label(r3, text="Type (F4):", font=("Segoe UI", 9, "bold"), width=10).pack(side=LEFT)
        
        self.dining_type_var = tb.StringVar(value="table")
        self.dining_combo = tb.Combobox(
            r3,
            textvariable=self.dining_type_var,
            values=["table", "takeaway", "delivery"],
            state="readonly",
            width=12
        )
        self.dining_combo.pack(side=LEFT, padx=(0, 10))
        self.dining_combo.bind("<<ComboboxSelected>>", lambda e: self._on_dining_type_change())

        tb.Label(r3, text="Table #:", font=("Segoe UI", 9, "bold")).pack(side=LEFT, padx=(0, 5))
        self.table_var = tb.StringVar(value="T-01")
        self.table_combo = tb.Combobox(
            r3,
            textvariable=self.table_var,
            values=[f"T-{i:02d}" for i in range(1, 21)] + ["VIP-1", "VIP-2", "Takeaway"],
            width=8
        )
        self.table_combo.pack(side=LEFT)

        # 2. Cart Items Table
        cart_frame = tb.Frame(right_frame)
        cart_frame.pack(fill=BOTH, expand=True, pady=(0, 10))

        cart_cols = ("item", "qty", "rate", "total")
        self.cart_tree = tb.Treeview(cart_frame, columns=cart_cols, show="headings", selectmode="browse")
        self.cart_tree.heading("item", text="Item Name")
        self.cart_tree.heading("qty", text="Qty")
        self.cart_tree.heading("rate", text="Rate")
        self.cart_tree.heading("total", text="Subtotal")

        self.cart_tree.column("item", width=140, anchor=W)
        self.cart_tree.column("qty", width=45, anchor=CENTER)
        self.cart_tree.column("rate", width=65, anchor=E)
        self.cart_tree.column("total", width=75, anchor=E)

        cart_scroll = tb.Scrollbar(cart_frame, orient=VERTICAL, command=self.cart_tree.yview)
        self.cart_tree.configure(yscrollcommand=cart_scroll.set)

        self.cart_tree.pack(side=LEFT, fill=BOTH, expand=True)
        cart_scroll.pack(side=RIGHT, fill=Y)

        # Cart Control Buttons (+, -, Delete)
        cart_btn_bar = tb.Frame(right_frame)
        cart_btn_bar.pack(fill=X, pady=(0, 10))

        plus_btn = tb.Button(cart_btn_bar, text="➕ Qty (+)", bootstyle=OUTLINE, command=self._increment_cart_qty)
        plus_btn.pack(side=LEFT, expand=True, fill=X, padx=2)

        minus_btn = tb.Button(cart_btn_bar, text="➖ Qty (-)", bootstyle=OUTLINE, command=self._decrement_cart_qty)
        minus_btn.pack(side=LEFT, expand=True, fill=X, padx=2)

        del_btn = tb.Button(cart_btn_bar, text="🗑️ Remove", bootstyle=DANGER, command=self._remove_cart_item)
        del_btn.pack(side=LEFT, expand=True, fill=X, padx=2)

        clear_cart_btn = tb.Button(cart_btn_bar, text="🧹 Clear (F2)", bootstyle=SECONDARY, command=self.clear_cart)
        clear_cart_btn.pack(side=LEFT, expand=True, fill=X, padx=2)

        # 3. Totals & Math Summary Box
        calc_frame = tb.Labelframe(right_frame, text=" PAYMENT & TOTALS ", bootstyle=PRIMARY, padding=10)
        calc_frame.pack(fill=X)

        # Subtotal Row
        r_sub = tb.Frame(calc_frame)
        r_sub.pack(fill=X, pady=1)
        tb.Label(r_sub, text="Subtotal:", font=("Segoe UI", 10)).pack(side=LEFT)
        self.lbl_subtotal = tb.Label(r_sub, text="₹ 0.00", font=("Segoe UI", 10, "bold"))
        self.lbl_subtotal.pack(side=RIGHT)

        # Discount Row
        r_disc = tb.Frame(calc_frame)
        r_disc.pack(fill=X, pady=2)
        tb.Label(r_disc, text="Discount:", font=("Segoe UI", 10)).pack(side=LEFT)

        self.disc_val_var = tb.StringVar(value="0")
        self.disc_type_var = tb.StringVar(value="flat")

        disc_entry = tb.Entry(r_disc, textvariable=self.disc_val_var, width=6, font=("Segoe UI", 9))
        disc_entry.pack(side=RIGHT, padx=(5, 0))
        disc_entry.bind("<KeyRelease>", lambda e: self.recalculate_totals())

        disc_type_combo = tb.Combobox(
            r_disc,
            textvariable=self.disc_type_var,
            values=["flat", "percent"],
            state="readonly",
            width=7,
            font=("Segoe UI", 9)
        )
        disc_type_combo.pack(side=RIGHT)
        disc_type_combo.bind("<<ComboboxSelected>>", lambda e: self.recalculate_totals())

        # GST Tax Row
        r_tax = tb.Frame(calc_frame)
        r_tax.pack(fill=X, pady=1)
        tax_rate = float(self.app_settings.get("tax_rate", 5.0))
        self.lbl_tax_title = tb.Label(r_tax, text=f"GST ({tax_rate}%):", font=("Segoe UI", 10))
        self.lbl_tax_title.pack(side=LEFT)

        self.lbl_tax_amt = tb.Label(r_tax, text="₹ 0.00", font=("Segoe UI", 10))
        self.lbl_tax_amt.pack(side=RIGHT)

        tb.Separator(calc_frame, orient=HORIZONTAL).pack(fill=X, pady=5)

        # Grand Total Row
        r_grand = tb.Frame(calc_frame)
        r_grand.pack(fill=X, pady=2)
        tb.Label(r_grand, text="GRAND TOTAL:", font=("Segoe UI", 12, "bold"), bootstyle=SUCCESS).pack(side=LEFT)
        self.lbl_grand_total = tb.Label(r_grand, text="₹ 0.00", font=("Segoe UI", 16, "bold"), bootstyle=SUCCESS)
        self.lbl_grand_total.pack(side=RIGHT)

        # Payment Method Radio Options
        pm_frame = tb.Frame(calc_frame)
        pm_frame.pack(fill=X, pady=(10, 5))

        tb.Label(pm_frame, text="Pay Mode:", font=("Segoe UI", 9, "bold")).pack(side=LEFT, padx=(0, 5))
        self.payment_mode_var = tb.StringVar(value="cash")

        for mode, text in [("cash", "💵 Cash"), ("upi", "📱 UPI / QR"), ("card", "💳 Card")]:
            rb = tb.Radiobutton(
                pm_frame,
                text=text,
                variable=self.payment_mode_var,
                value=mode,
                bootstyle=PRIMARY
            )
            rb.pack(side=LEFT, padx=5)

        # Checkout & Print Button
        self.checkout_btn = tb.Button(
            calc_frame,
            text="💳 CHECKOUT & PRINT BILL (F5 / F8)",
            bootstyle=SUCCESS,
            padding=10,
            command=self.process_checkout
        )
        self.checkout_btn.pack(fill=X, pady=(10, 0))

    # ==========================================
    # LOGIC & METHODS
    # ==========================================
    def load_categories(self):
        """Populates top category filter buttons."""
        for widget in self.cat_frame.winfo_children():
            widget.destroy()

        categories = Category.get_all(active_only=True)
        all_cats = [{"id": 0, "name": "All Items"}] + categories

        for cat in all_cats:
            cat_id = str(cat["id"])
            btn_style = SUCCESS if cat_id == self.current_category_id else OUTLINE

            btn = tb.Button(
                self.cat_frame,
                text=cat["name"],
                bootstyle=btn_style,
                command=lambda cid=cat_id: self.select_category(cid)
            )
            btn.pack(side=LEFT, padx=3, pady=2)

    def select_category(self, cat_id):
        self.current_category_id = str(cat_id)
        self.load_categories()
        self.load_menu_items()

    def _clear_search(self):
        self.search_entry.delete(0, END)
        self.load_menu_items()

    def load_menu_items(self):
        """Renders grid of menu item cards based on current category and search query."""
        for widget in self.scrollable_grid.winfo_children():
            widget.destroy()

        search_query = self.search_entry.get().strip()
        items = MenuItem.get_all(category_id=self.current_category_id, search_term=search_query)

        if not items:
            empty_lbl = tb.Label(
                self.scrollable_grid,
                text="No menu items found matching search filter.",
                font=("Segoe UI", 11, "italic"),
                bootstyle=SECONDARY
            )
            empty_lbl.pack(pady=40, anchor=CENTER)
            return

        # Render Cards in 3-column Grid
        columns_count = 3
        for idx, item in enumerate(items):
            row = idx // columns_count
            col = idx % columns_count

            card = tb.Labelframe(
                self.scrollable_grid,
                text=f" {item['item_code']} ",
                bootstyle=SECONDARY,
                padding=10,
                cursor="hand2"
            )
            card.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

            # Veg / Non-Veg Icon Badge
            veg_tag = "🟢 VEG" if item["food_type"] == "veg" else "🔴 NON-VEG"
            veg_color = SUCCESS if item["food_type"] == "veg" else DANGER

            top_bar = tb.Frame(card)
            top_bar.pack(fill=X)
            tb.Label(top_bar, text=veg_tag, font=("Segoe UI", 8, "bold"), bootstyle=veg_color).pack(side=LEFT)

            # Price Tag
            tb.Label(top_bar, text=format_currency(item["price"]), font=("Segoe UI", 11, "bold"), bootstyle=PRIMARY).pack(side=RIGHT)

            # Item Name
            name_lbl = tb.Label(
                card,
                text=item["name"],
                font=("Segoe UI", 11, "bold"),
                wraplength=180,
                justify=LEFT
            )
            name_lbl.pack(anchor=W, pady=(5, 2))

            # Category & Description
            if item.get("description"):
                desc_text = item["description"][:35] + "..." if len(item["description"]) > 35 else item["description"]
                tb.Label(card, text=desc_text, font=("Segoe UI", 8), bootstyle=SECONDARY, wraplength=180).pack(anchor=W)

            # Add to Cart Button
            add_btn = tb.Button(
                card,
                text="➕ Add to Cart",
                bootstyle=SUCCESS,
                command=lambda it=item: self.add_to_cart(it)
            )
            add_btn.pack(fill=X, pady=(8, 0))

            # Bind Card Click to Add to Cart
            card.bind("<Button-1>", lambda e, it=item: self.add_to_cart(it))
            name_lbl.bind("<Button-1>", lambda e, it=item: self.add_to_cart(it))

    def add_to_cart(self, item):
        """Adds or increments an item in the cart list."""
        for cart_item in self.cart:
            if cart_item["id"] == item["id"]:
                cart_item["quantity"] += 1
                self.update_cart_display()
                return

        # New Item in Cart
        self.cart.append({
            "id": item["id"],
            "code": item["item_code"],
            "name": item["name"],
            "price": float(item["price"]),
            "quantity": 1
        })
        self.update_cart_display()

    def update_cart_display(self):
        """Refreshes Treeview and recalculates totals."""
        for item in self.cart_tree.get_children():
            self.cart_tree.delete(item)

        for c_item in self.cart:
            item_total = c_item["price"] * c_item["quantity"]
            self.cart_tree.insert("", END, iid=str(c_item["id"]), values=(
                c_item["name"],
                c_item["quantity"],
                f"{c_item['price']:.2f}",
                f"{item_total:.2f}"
            ))

        self.recalculate_totals()

    def recalculate_totals(self):
        """Calculates subtotal, discount, tax, and grand total."""
        tax_rate = float(self.app_settings.get("tax_rate", 5.0))
        disc_type = self.disc_type_var.get()
        try:
            disc_val = float(self.disc_val_var.get() or 0)
        except ValueError:
            disc_val = 0.0

        totals = Order.calculate_totals(self.cart, tax_rate=tax_rate, discount_type=disc_type, discount_value=disc_val)

        self.lbl_subtotal.config(text=format_currency(totals["subtotal"]))
        self.lbl_tax_amt.config(text=format_currency(totals["tax_amount"]))
        self.lbl_grand_total.config(text=format_currency(totals["grand_total"]))

    def _increment_cart_qty(self):
        selected = self.cart_tree.selection()
        if not selected:
            return
        item_id = int(selected[0])
        for c_item in self.cart:
            if c_item["id"] == item_id:
                c_item["quantity"] += 1
                break
        self.update_cart_display()

    def _decrement_cart_qty(self):
        selected = self.cart_tree.selection()
        if not selected:
            return
        item_id = int(selected[0])
        for c_item in self.cart:
            if c_item["id"] == item_id:
                c_item["quantity"] -= 1
                if c_item["quantity"] <= 0:
                    self.cart.remove(c_item)
                break
        self.update_cart_display()

    def _remove_cart_item(self):
        selected = self.cart_tree.selection()
        if not selected:
            return
        item_id = int(selected[0])
        self.cart = [c for c in self.cart if c["id"] != item_id]
        self.update_cart_display()

    def clear_cart(self):
        """Resets current order cart and customer details."""
        self.cart.clear()
        self.cust_phone_entry.delete(0, END)
        self.cust_name_entry.delete(0, END)
        self.disc_val_var.set("0")
        self.update_cart_display()

    def _on_dining_type_change(self):
        dtype = self.dining_type_var.get()
        if dtype == "takeaway":
            self.table_var.set("Takeaway")
        elif dtype == "delivery":
            self.table_var.set("Delivery")
        else:
            self.table_var.set("T-01")

    def _auto_lookup_customer(self):
        phone = self.cust_phone_entry.get().strip()
        if phone and len(phone) >= 10:
            cust = Customer.get_by_phone(phone)
            if cust:
                self.cust_name_entry.delete(0, END)
                self.cust_name_entry.insert(0, cust["name"])

    def process_checkout(self):
        """Processes and saves order to MySQL, then triggers thermal receipt modal."""
        if not self.cart:
            messagebox.showwarning("Empty Cart", "Please add at least one item to the cart before checkout.", parent=self)
            return

        phone = self.cust_phone_entry.get().strip()
        name = self.cust_name_entry.get().strip() or "Guest Customer"
        dining_type = self.dining_type_var.get()
        table_no = self.table_combo.get().strip()
        payment_method = self.payment_mode_var.get()

        tax_rate = float(self.app_settings.get("tax_rate", 5.0))
        disc_type = self.disc_type_var.get()
        try:
            disc_val = float(self.disc_val_var.get() or 0)
        except ValueError:
            disc_val = 0.0

        # Save or get customer record
        customer_id = None
        if phone:
            customer_id = Customer.save_or_get(name, phone)

        try:
            result = Order.create_order(
                cashier_id=self.current_user.id,
                customer_id=customer_id,
                dining_type=dining_type,
                table_number=table_no,
                cart_items=self.cart,
                tax_rate=tax_rate,
                discount_type=disc_type,
                discount_value=disc_val,
                payment_method=payment_method
            )

            # Build data dict for receipt preview
            order_data = {
                "bill_number": result["bill_number"],
                "created_at": None,
                "cashier_name": self.current_user.full_name,
                "customer_name": name,
                "customer_phone": phone or "N/A",
                "dining_type": dining_type,
                "table_number": table_no,
                "payment_method": payment_method,
                "subtotal": result["totals"]["subtotal"],
                "discount_amount": result["totals"]["discount_amount"],
                "tax_rate": tax_rate,
                "tax_amount": result["totals"]["tax_amount"],
                "grand_total": result["totals"]["grand_total"]
            }

            # Show thermal receipt preview & print dialog
            ReceiptPrinter.show_receipt_dialog(self.winfo_toplevel(), order_data, self.cart, self.app_settings)

            # Clear cart for next order
            self.clear_cart()

        except Exception as e:
            messagebox.showerror("Order Creation Failed", f"An error occurred while saving the order:\n{e}", parent=self)

    # Keyboard Shortcuts Handlers
    def focus_search(self):
        self.search_entry.focus()
        self.search_entry.select_range(0, END)

    def focus_phone(self):
        self.cust_phone_entry.focus()
        self.cust_phone_entry.select_range(0, END)

    def toggle_dining_type(self):
        current = self.dining_type_var.get()
        types = ["table", "takeaway", "delivery"]
        nxt = types[(types.index(current) + 1) % len(types)]
        self.dining_type_var.set(nxt)
        self._on_dining_type_change()
