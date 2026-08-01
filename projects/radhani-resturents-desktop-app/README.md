# 👑 Rajdhani Restaurant POS & Billing Management System

A professional, desktop Restaurant Billing & Point-of-Sale (POS) Management Application built using **Python 3**, **Tkinter**, **`ttkbootstrap`**, and **MySQL (`mysql.connector`)**. Designed specifically for fine-dining restaurants, fast-food outlets, and thali dining centers.

---

## 🌟 Features Overview

- 🔐 **Dual Role Login System**:
  - **Admin**: Full access including POS Billing, Menu & Category Management, Sales Reports, Order History, and Restaurant Profile Settings.
  - **Cashier**: Access restricted to POS Billing, Order History, and Dashboard.
- 📊 **Executive Overview Dashboard**: Real-time sales statistics (Today's Sales, Orders count, Average Ticket Value, GST collected) and recent order stream.
- 🍲 **Categorized Menu Catalog**: Includes pre-seeded items for Breakfast, Rajdhani Special Thalis, Starters & Snacks, Main Course (Veg & Non-Veg), Breads & Rice, Beverages, and Desserts.
- 🔍 **Live Search & Filter**: Real-time menu filtering as you type item name, code (SKU), or category.
- 🛒 **Fast POS Billing Interface**:
  - Interactive item cards with Veg/Non-Veg visual badges and prices.
  - Cart item quantity modification (`+`, `-`, remove, edit quantity).
  - Customer phone lookup & automatic visit counter.
  - Dining type toggle: Table Number selector, Takeaway, or Delivery.
  - Automatic Subtotal, GST Tax (5% CGST + SGST), Discount (% or Flat ₹), and Grand Total calculations.
  - Multi-payment mode support: Cash, Card, UPI / QR.
- 🖨️ **Thermal Receipt Printing & Preview**:
  - Automatic bill number generation (`RAJ-YYYYMMDD-XXXX`).
  - Itemized receipt preview modal formatted for 80mm thermal receipt printers.
  - Direct output to Windows / OS default printer.
- 📜 **Order History & Invoice Reprint**: Search past orders by Bill #, Customer Phone, or Date; view line items details, cancel orders, or reprint receipts.
- 📈 **Sales Reports & CSV Export**: Daily, Weekly, and Monthly sales analysis, payment breakdown, top-selling menu items, and one-click CSV export.
- ⚙️ **Inventory-Ready Menu Management**: Complete CRUD for menu items and categories with stock tracking levels.
- ⌨️ **Fast Keyboard Shortcuts**: Engineered for high-speed counter operations.

---

## 🛠️ Prerequisites & System Requirements

1. **Python**: Python 3.10+ installed on Windows, macOS, or Linux.
2. **MySQL Database**: MySQL Server / MariaDB running locally (e.g. via XAMPP, WAMP, MySQL Workbench, or Standalone Server on port `3306`).
   - Default Database: `rajdhani_pos_db`
   - Default User: `root`
   - Default Password: `""` (empty)

---

## 🚀 Quick Setup & Installation

### Step 1: Install Dependencies
Open PowerShell or Command Prompt in the project folder and run:
```bash
pip install -r requirements.txt
```

*(Installed packages include `ttkbootstrap`, `mysql-connector-python`, and `Pillow`).*

### Step 2: Ensure MySQL Server is Running
Start your local MySQL server (e.g. start MySQL module in XAMPP Control Panel).

> **Note**: You **do not** need to manually create the database or tables! The application automatically checks for `rajdhani_pos_db` on startup; if it does not exist, it creates the database, tables, relationships, and loads initial seed data (users, categories, menu items, settings).

### Step 3: Run Application
Launch the POS software:
```bash
python main.py
```

---

## 🔑 Default Login Credentials

| Role | Username | Password | Access Rights |
| :--- | :--- | :--- | :--- |
| **Admin** | `admin` | `admin123` | Full Access (POS, Menu CRUD, Reports, Settings) |
| **Cashier** | `cashier` | `cashier123` | Counter Billing, Dashboard, Order History |

*(Passwords can be changed by the Admin in the Settings module).*

---

## ⌨️ Keyboard Shortcuts Reference

| Shortcut | Description |
| :--- | :--- |
| **`F1`** | Focus Live Quick Search Bar |
| **`F2`** | Clear Current Cart / Reset Order |
| **`F3`** | Focus Customer Phone Number Input |
| **`F4`** | Toggle Dining Type (Table / Takeaway / Delivery) |
| **`F5` / `F8`** | Checkout & Print Thermal Bill Receipt |
| **`Ctrl + H`** | Open Order History View |
| **`Ctrl + M`** | Open Menu Management (Admin) |
| **`Ctrl + R`** | Open Sales Reports (Admin) |
| **`Esc`** | Close Dialogs / Modals |

---

## 📁 Project Architecture (MVC Structure)

```
radhani-resturents-desktop-app/
├── config.py                 # Application metadata, database configuration & settings defaults
├── main.py                   # App entry point & database initialization check
├── schema.sql                # Standalone SQL schema DDL and seed data script
├── requirements.txt          # Third-party Python dependencies
├── README.md                 # Setup guide and documentation
├── database/
│   ├── connection.py         # MySQL connection manager & parametrized query helper
│   └── init_db.py            # Automatic schema & seed data initializer
├── models/
│   ├── user.py               # User authentication & password hashing
│   ├── category.py           # Category model
│   ├── menu_item.py          # Menu items CRUD & stock inventory model
│   ├── customer.py           # Customer details lookup & creation
│   ├── order.py              # Order processing, line items & cart math
│   ├── report.py             # Sales reports aggregator & SQL analytics
│   └── settings.py           # Restaurant settings key-value persistence
├── utils/
│   ├── logger.py             # Application logging to logs/app.log
│   ├── helpers.py            # Currency, date formatting & validation utilities
│   ├── printer.py            # Thermal receipt formatting & OS print trigger
│   └── exporter.py           # CSV exporter utility for analytics
└── ui/
    ├── app.py                # Main window layout, header navbar & view router
    ├── login_view.py         # Login screen (Admin / Cashier)
    ├── dashboard_view.py     # Summary dashboard with quick stats
    ├── pos_billing_view.py   # Primary POS billing UI (Menu Grid, Cart, Checkout)
    ├── menu_mgmt_view.py     # Menu & Category CRUD interface
    ├── order_history_view.py # Order search, detail viewer, cancel & receipt reprint
    ├── reports_view.py       # Sales analytics reports & CSV exporter
    └── settings_view.py      # Restaurant settings & password update
```
