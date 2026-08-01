import os

# ==========================================
# RAJDHANI RESTAURANT POS CONFIGURATION
# ==========================================

# Application Metadata
APP_NAME = "Rajdhani Restaurant POS & Billing Management System"
APP_VERSION = "1.0.0"
COMPANY_NAME = "Rajdhani Restaurant"
RESTAURANT_TAGLINE = "Authentic Indian Flavors & Fine Dining"

# Database Configuration (MySQL)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin")
DB_NAME = os.getenv("DB_NAME", "rajdhani_pos_db")
DB_CHARSET = "utf8mb4"

# Default Restaurant Settings
DEFAULT_SETTINGS = {
    "restaurant_name": "Rajdhani Restaurant",
    "tagline": "Taste of Tradition & Luxury",
    "address": "123 Heritage Palace Road, Near City Center, New Delhi - 110001",
    "phone": "+91 98765 43210",
    "email": "contact@rajdhanirestaurant.com",
    "gstin": "07AAAAA0000A1Z5",
    "currency_symbol": "₹",
    "tax_rate": 5.0,  # 5% GST (2.5% CGST + 2.5% SGST)
    "cgst_rate": 2.5,
    "sgst_rate": 2.5,
    "enable_tax": "true",
    "receipt_footer": "Thank you for dining with Rajdhani Restaurant! Visit Again!",
    "theme": "cosmo"  # ttkbootstrap theme: cosmo, flatly, superhero, darkly, litera, etc.
}

# Keyboard Shortcuts Reference
KEYBOARD_SHORTCUTS = {
    "F1": "Quick Search Focus",
    "F2": "New Order / Clear Cart",
    "F3": "Customer Phone Input Focus",
    "F4": "Toggle Dining Type (Table / Takeaway)",
    "F5": "Checkout & Complete Payment",
    "F8": "Print Current Receipt",
    "Ctrl+R": "Open Reports",
    "Ctrl+M": "Manage Menu",
    "Ctrl+H": "Order History",
    "Esc": "Cancel / Close Modal"
}

# File Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(EXPORTS_DIR, exist_ok=True)
