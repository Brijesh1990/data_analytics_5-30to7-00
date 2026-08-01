import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox, simpledialog
from models.category import Category
from models.menu_item import MenuItem
from utils.helpers import format_currency
from utils.logger import logger

class MenuManagementView(tb.Frame):
    """
    Admin CRUD Interface for managing Menu Items and Categories.
    """

    def __init__(self, parent, current_user):
        super().__init__(parent, padding=15)
        self.current_user = current_user
        self.pack(fill=BOTH, expand=True)

        self._create_widgets()
        self.refresh_categories()
        self.refresh_menu_items()

    def _create_widgets(self):
        # Title Bar
        title_frame = tb.Frame(self)
        title_frame.pack(fill=X, pady=(0, 15))

        tb.Label(
            title_frame,
            text="🍲 MENU & CATEGORY MANAGEMENT",
            font=("Segoe UI", 16, "bold"),
            bootstyle=PRIMARY
        ).pack(side=LEFT)

        # Paned Window splitting Left (Categories) and Right (Menu Items)
        paned = tb.Panedwindow(self, orient=HORIZONTAL)
        paned.pack(fill=BOTH, expand=True)

        # Left Frame: Categories Management (30%)
        cat_box = tb.Labelframe(paned, text=" CATEGORIES ", bootstyle=PRIMARY, padding=10)
        paned.add(cat_box, weight=1)

        self.cat_listbox = tb.Treeview(cat_box, columns=("name",), show="headings", height=15)
        self.cat_listbox.heading("name", text="Category Name")
        self.cat_listbox.column("name", width=180, anchor=W)
        self.cat_listbox.pack(fill=BOTH, expand=True, pady=(0, 10))
        self.cat_listbox.bind("<<TreeviewSelect>>", lambda e: self.refresh_menu_items())

        cat_btn_frame = tb.Frame(cat_box)
        cat_btn_frame.pack(fill=X)

        add_cat_btn = tb.Button(cat_btn_frame, text="➕ Add Cat", bootstyle=SUCCESS, command=self.add_category, width=10)
        add_cat_btn.pack(side=LEFT, padx=2)

        edit_cat_btn = tb.Button(cat_btn_frame, text="✏️ Edit", bootstyle=INFO, command=self.edit_category, width=8)
        edit_cat_btn.pack(side=LEFT, padx=2)

        del_cat_btn = tb.Button(cat_btn_frame, text="🗑️ Del", bootstyle=DANGER, command=self.delete_category, width=8)
        del_cat_btn.pack(side=LEFT, padx=2)

        # Right Frame: Menu Items Management (70%)
        item_box = tb.Labelframe(paned, text=" MENU ITEMS CATALOG ", bootstyle=PRIMARY, padding=10)
        paned.add(item_box, weight=3)

        # Search Bar & Action Buttons
        top_bar = tb.Frame(item_box)
        top_bar.pack(fill=X, pady=(0, 10))

        tb.Label(top_bar, text="Search:", font=("Segoe UI", 10, "bold")).pack(side=LEFT, padx=(0, 5))
        self.search_entry = tb.Entry(top_bar, font=("Segoe UI", 10), width=25)
        self.search_entry.pack(side=LEFT, padx=(0, 15))
        self.search_entry.bind("<KeyRelease>", lambda e: self.refresh_menu_items())

        add_item_btn = tb.Button(top_bar, text="➕ Add New Item", bootstyle=SUCCESS, command=self.add_menu_item)
        add_item_btn.pack(side=RIGHT, padx=5)

        edit_item_btn = tb.Button(top_bar, text="✏️ Edit Selected", bootstyle=INFO, command=self.edit_menu_item)
        edit_item_btn.pack(side=RIGHT, padx=5)

        del_item_btn = tb.Button(top_bar, text="🗑️ Toggle Availability", bootstyle=WARNING, command=self.delete_menu_item)
        del_item_btn.pack(side=RIGHT, padx=5)

        # Items Table
        columns = ("id", "code", "name", "category", "price", "type", "stock", "available")
        self.tree = tb.Treeview(item_box, columns=columns, show="headings")

        self.tree.heading("id", text="ID")
        self.tree.heading("code", text="Code")
        self.tree.heading("name", text="Item Name")
        self.tree.heading("category", text="Category")
        self.tree.heading("price", text="Price")
        self.tree.heading("type", text="Type")
        self.tree.heading("stock", text="Stock Qty")
        self.tree.heading("available", text="Available")

        self.tree.column("id", width=40, anchor=CENTER)
        self.tree.column("code", width=70, anchor=CENTER)
        self.tree.column("name", width=180, anchor=W)
        self.tree.column("category", width=140, anchor=W)
        self.tree.column("price", width=80, anchor=E)
        self.tree.column("type", width=80, anchor=CENTER)
        self.tree.column("stock", width=80, anchor=CENTER)
        self.tree.column("available", width=80, anchor=CENTER)

        scrollbar = tb.Scrollbar(item_box, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

    # Category Actions
    def refresh_categories(self):
        for item in self.cat_listbox.get_children():
            self.cat_listbox.delete(item)

        categories = Category.get_all(active_only=False)
        for cat in categories:
            self.cat_listbox.insert("", END, iid=str(cat["id"]), values=(cat["name"],))

    def add_category(self):
        name = simpledialog.askstring("Add Category", "Enter Category Name:", parent=self)
        if name and name.strip():
            Category.create(name.strip())
            self.refresh_categories()

    def edit_category(self):
        selected = self.cat_listbox.selection()
        if not selected:
            messagebox.showwarning("Select Category", "Please select a category to edit.", parent=self)
            return
        cat_id = int(selected[0])
        old_name = self.cat_listbox.item(selected[0])["values"][0]
        new_name = simpledialog.askstring("Edit Category", "Update Category Name:", initialvalue=old_name, parent=self)
        if new_name and new_name.strip():
            Category.update(cat_id, new_name.strip())
            self.refresh_categories()

    def delete_category(self):
        selected = self.cat_listbox.selection()
        if not selected:
            messagebox.showwarning("Select Category", "Please select a category to delete.", parent=self)
            return
        cat_id = int(selected[0])
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to deactivate this category?", parent=self):
            Category.delete(cat_id)
            self.refresh_categories()

    # Menu Item Actions
    def refresh_menu_items(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        cat_id = None
        selected_cat = self.cat_listbox.selection()
        if selected_cat:
            cat_id = int(selected_cat[0])

        search_query = self.search_entry.get().strip()
        items = MenuItem.get_all(category_id=cat_id, search_term=search_query, available_only=False)

        for it in items:
            self.tree.insert("", END, iid=str(it["id"]), values=(
                it["id"],
                it["item_code"],
                it["name"],
                it["category_name"],
                format_currency(it["price"]),
                str(it["food_type"]).upper(),
                it["stock_quantity"],
                "YES" if it["is_available"] else "NO"
            ))

    def add_menu_item(self):
        self._show_item_form_dialog(title="Add New Menu Item")

    def edit_menu_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Item", "Please select a menu item to edit.", parent=self)
            return
        item_id = int(selected[0])
        item = MenuItem.get_by_id(item_id)
        if item:
            self._show_item_form_dialog(title=f"Edit Item - {item['name']}", item_data=item)

    def delete_menu_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Item", "Please select an item to toggle.", parent=self)
            return
        item_id = int(selected[0])
        MenuItem.delete(item_id)
        self.refresh_menu_items()

    def _show_item_form_dialog(self, title="Menu Item Form", item_data=None):
        dialog = tb.Toplevel(self.winfo_toplevel())
        dialog.title(title)
        dialog.geometry("450x550")
        dialog.resizable(False, False)
        dialog.grab_set()

        tb.Label(dialog, text=title, font=("Segoe UI", 12, "bold"), bootstyle=PRIMARY).pack(pady=10)

        form_frame = tb.Frame(dialog, padding=20)
        form_frame.pack(fill=BOTH, expand=True)

        categories = Category.get_all(active_only=True)
        cat_dict = {cat["name"]: cat["id"] for cat in categories}
        cat_names = list(cat_dict.keys())

        # Category Dropdown
        tb.Label(form_frame, text="Category:", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        cat_var = tb.StringVar(value=cat_names[0] if cat_names else "")
        if item_data and item_data.get("category_name") in cat_names:
            cat_var.set(item_data["category_name"])
        cat_combo = tb.Combobox(form_frame, textvariable=cat_var, values=cat_names, state="readonly")
        cat_combo.pack(fill=X, pady=(0, 10))

        # Item Code
        tb.Label(form_frame, text="Item Code (SKU):", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        code_entry = tb.Entry(form_frame)
        code_entry.pack(fill=X, pady=(0, 10))
        if item_data:
            code_entry.insert(0, item_data["item_code"])

        # Item Name
        tb.Label(form_frame, text="Item Name:", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        name_entry = tb.Entry(form_frame)
        name_entry.pack(fill=X, pady=(0, 10))
        if item_data:
            name_entry.insert(0, item_data["name"])

        # Price
        tb.Label(form_frame, text="Price (₹):", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        price_entry = tb.Entry(form_frame)
        price_entry.pack(fill=X, pady=(0, 10))
        if item_data:
            price_entry.insert(0, str(item_data["price"]))

        # Food Type
        tb.Label(form_frame, text="Food Type:", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        type_var = tb.StringVar(value=item_data["food_type"] if item_data else "veg")
        r_frame = tb.Frame(form_frame)
        r_frame.pack(fill=X, pady=(0, 10))
        tb.Radiobutton(r_frame, text="🟢 Veg", variable=type_var, value="veg").pack(side=LEFT, padx=10)
        tb.Radiobutton(r_frame, text="🔴 Non-Veg", variable=type_var, value="non-veg").pack(side=LEFT, padx=10)

        # Stock Qty
        tb.Label(form_frame, text="Initial Stock Quantity:", font=("Segoe UI", 9, "bold")).pack(anchor=W, pady=(5, 2))
        stock_entry = tb.Entry(form_frame)
        stock_entry.pack(fill=X, pady=(0, 10))
        stock_entry.insert(0, str(item_data["stock_quantity"]) if item_data else "100")

        # Save Action
        def save():
            cat_name = cat_var.get()
            code = code_entry.get().strip()
            name = name_entry.get().strip()
            price_str = price_entry.get().strip()
            stock_str = stock_entry.get().strip()

            if not code or not name or not price_str:
                messagebox.showwarning("Validation Error", "Code, Name, and Price are required.", parent=dialog)
                return

            try:
                price = float(price_str)
                stock = int(stock_str)
            except ValueError:
                messagebox.showwarning("Validation Error", "Price must be a number and Stock an integer.", parent=dialog)
                return

            cat_id = cat_dict.get(cat_name)
            food_type = type_var.get()

            if item_data:
                MenuItem.update(item_data["id"], cat_id, code, name, price, "", food_type, stock, 1, 1)
            else:
                MenuItem.create(cat_id, code, name, price, "", food_type, stock, 1, 1)

            dialog.destroy()
            self.refresh_menu_items()

        save_btn = tb.Button(form_frame, text="💾 Save Item", bootstyle=SUCCESS, command=save)
        save_btn.pack(fill=X, pady=15)
