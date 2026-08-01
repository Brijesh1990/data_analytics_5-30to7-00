import hashlib
import datetime
import re
from config import DEFAULT_SETTINGS

def hash_password(password: str) -> str:
    """Returns SHA-256 hash of a plain text password."""
    if not password:
        return ""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def format_currency(amount: float, symbol: str = None) -> str:
    """Formats numeric value into currency format e.g. ₹ 150.00"""
    if amount is None:
        amount = 0.0
    if symbol is None:
        symbol = DEFAULT_SETTINGS.get("currency_symbol", "₹")
    try:
        val = float(amount)
        return f"{symbol} {val:,.2f}"
    except (ValueError, TypeError):
        return f"{symbol} 0.00"

def format_datetime(dt=None, fmt: str = "%d-%b-%Y %I:%M %p") -> str:
    """Formats datetime object or string to user readable format."""
    if dt is None:
        dt = datetime.datetime.now()
    if isinstance(dt, str):
        try:
            dt = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return dt
    return dt.strftime(fmt)

def generate_bill_number(last_id: int = 1) -> str:
    """Generates unique invoice number formatted as RAJ-YYYYMMDD-XXXX."""
    today_str = datetime.datetime.now().strftime("%Y%m%d")
    return f"RAJ-{today_str}-{last_id:04d}"

def validate_phone(phone: str) -> bool:
    """Validates 10-12 digit mobile phone numbers."""
    if not phone:
        return False
    clean_phone = re.sub(r'[\s\-\+\(\)]', '', phone)
    return bool(re.match(r'^\d{10,12}$', clean_phone))

def validate_email(email: str) -> bool:
    """Validates basic email format."""
    if not email:
        return True  # Email is optional
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))
