from database.connection import DatabaseManager
from utils.logger import logger

class Customer:
    """Customer Model for customer lookup, creation, and order associations."""

    @classmethod
    def get_by_phone(cls, phone):
        """Finds customer record by phone number."""
        if not phone:
            return None
        query = "SELECT * FROM customers WHERE phone = %s"
        try:
            return DatabaseManager.execute_query(query, (phone.strip(),), fetch_one=True)
        except Exception as e:
            logger.error(f"Error fetching customer by phone '{phone}': {e}")
            return None

    @classmethod
    def save_or_get(cls, name, phone, email="", address=""):
        """
        Saves new customer or returns existing customer ID.
        If customer exists, updates total_visits count.
        """
        if not phone:
            return None

        phone = phone.strip()
        name = name.strip() if name else "Guest Customer"

        existing = cls.get_by_phone(phone)
        if existing:
            # Update visits and info
            update_query = """
                UPDATE customers
                SET name = %s, total_visits = total_visits + 1
                WHERE id = %s
            """
            try:
                DatabaseManager.execute_query(update_query, (name, existing["id"]), commit=True)
                return existing["id"]
            except Exception as e:
                logger.error(f"Error updating customer visits: {e}")
                return existing["id"]
        else:
            # Create new customer
            insert_query = """
                INSERT INTO customers (name, phone, email, address, total_visits)
                VALUES (%s, %s, %s, %s, 1)
            """
            try:
                cust_id = DatabaseManager.execute_query(insert_query, (name, phone, email, address), commit=True)
                logger.info(f"Created customer '{name}' ({phone}) with ID {cust_id}")
                return cust_id
            except Exception as e:
                logger.error(f"Error creating new customer: {e}")
                return None
