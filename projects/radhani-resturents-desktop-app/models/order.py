from database.connection import DatabaseManager
from utils.helpers import generate_bill_number
from models.menu_item import MenuItem
from utils.logger import logger

class Order:
    """Order Model managing order processing, line items, cart math, and invoice persistence."""

    @staticmethod
    def calculate_totals(cart_items, tax_rate=5.0, discount_type="flat", discount_value=0.0):
        """
        Calculates subtotal, tax amount, discount amount, and grand total.
        cart_items format: list of dicts [{'id', 'name', 'price', 'quantity'}, ...]
        """
        subtotal = 0.0
        for item in cart_items:
            subtotal += float(item["price"]) * int(item["quantity"])

        # Calculate discount
        discount_amount = 0.0
        discount_value = float(discount_value)
        if discount_type == "percent":
            discount_amount = (subtotal * discount_value) / 100.0
        else:
            discount_amount = discount_value

        if discount_amount > subtotal:
            discount_amount = subtotal

        taxable_amount = max(0.0, subtotal - discount_amount)
        tax_amount = (taxable_amount * float(tax_rate)) / 100.0
        grand_total = taxable_amount + tax_amount

        return {
            "subtotal": round(subtotal, 2),
            "discount_type": discount_type,
            "discount_value": round(discount_value, 2),
            "discount_amount": round(discount_amount, 2),
            "taxable_amount": round(taxable_amount, 2),
            "tax_rate": round(float(tax_rate), 2),
            "tax_amount": round(tax_amount, 2),
            "grand_total": round(grand_total, 2)
        }

    @classmethod
    def get_next_bill_number(cls) -> str:
        """Retrieves the next auto-increment integer ID to generate formatted bill number."""
        query = "SELECT MAX(id) AS max_id FROM orders"
        try:
            res = DatabaseManager.execute_query(query, fetch_one=True)
            max_id = (res["max_id"] or 0) + 1 if res else 1
            return generate_bill_number(max_id)
        except Exception:
            return generate_bill_number(1)

    @classmethod
    def create_order(cls, cashier_id, customer_id, dining_type, table_number, cart_items,
                     tax_rate=5.0, discount_type="flat", discount_value=0.0,
                     payment_method="cash", notes=""):
        """
        Saves a complete order with items & payment record into database in a single flow.
        """
        if not cart_items:
            raise ValueError("Cart cannot be empty for checkout.")

        totals = cls.calculate_totals(cart_items, tax_rate, discount_type, discount_value)
        bill_number = cls.get_next_bill_number()

        conn = None
        cursor = None
        try:
            conn = DatabaseManager.get_connection()
            cursor = conn.cursor()

            # 1. Insert Order Header
            order_sql = """
                INSERT INTO orders (
                    bill_number, customer_id, user_id, dining_type, table_number,
                    subtotal, discount_type, discount_value, discount_amount,
                    tax_rate, tax_amount, grand_total, payment_method, payment_status,
                    order_status, notes
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'paid', 'completed', %s)
            """
            order_params = (
                bill_number, customer_id, cashier_id, dining_type, table_number or "N/A",
                totals["subtotal"], totals["discount_type"], totals["discount_value"], totals["discount_amount"],
                totals["tax_rate"], totals["tax_amount"], totals["grand_total"], payment_method, notes
            )
            cursor.execute(order_sql, order_params)
            order_id = cursor.lastrowid

            # 2. Insert Order Line Items & update inventory stock
            item_sql = """
                INSERT INTO order_items (order_id, menu_item_id, item_name, unit_price, quantity, subtotal)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            for item in cart_items:
                item_subtotal = float(item["price"]) * int(item["quantity"])
                cursor.execute(item_sql, (order_id, item["id"], item["name"], item["price"], item["quantity"], item_subtotal))
                
                # Update inventory stock
                MenuItem.update_stock(item["id"], item["quantity"])

            # 3. Insert Payment Record
            payment_sql = """
                INSERT INTO payments (order_id, payment_method, amount_paid)
                VALUES (%s, %s, %s)
            """
            cursor.execute(payment_sql, (order_id, payment_method, totals["grand_total"]))

            logger.info(f"Order created successfully. Bill #: {bill_number}, ID: {order_id}, Total: {totals['grand_total']}")
            return {
                "order_id": order_id,
                "bill_number": bill_number,
                "totals": totals
            }

        except Exception as e:
            logger.error(f"Error creating order: {e}")
            raise e
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    @classmethod
    def get_order_by_bill_number(cls, bill_number):
        """Retrieves order header and customer/cashier details by bill number."""
        query = """
            SELECT o.*, c.name AS customer_name, c.phone AS customer_phone, u.full_name AS cashier_name
            FROM orders o
            LEFT JOIN customers c ON o.customer_id = c.id
            JOIN users u ON o.user_id = u.id
            WHERE o.bill_number = %s
        """
        try:
            return DatabaseManager.execute_query(query, (bill_number.strip(),), fetch_one=True)
        except Exception as e:
            logger.error(f"Error fetching order by bill number '{bill_number}': {e}")
            return None

    @classmethod
    def get_order_items(cls, order_id):
        """Retrieves list of items for a given order ID."""
        query = "SELECT * FROM order_items WHERE order_id = %s ORDER BY id ASC"
        try:
            return DatabaseManager.execute_query(query, (order_id,), fetch_all=True) or []
        except Exception as e:
            logger.error(f"Error fetching items for order ID {order_id}: {e}")
            return []

    @classmethod
    def get_recent_orders(cls, limit=100, search_query=None, start_date=None, end_date=None):
        """Retrieves orders list for order history view with filters."""
        query = """
            SELECT o.*, c.name AS customer_name, c.phone AS customer_phone, u.full_name AS cashier_name
            FROM orders o
            LEFT JOIN customers c ON o.customer_id = c.id
            JOIN users u ON o.user_id = u.id
            WHERE 1=1
        """
        params = []

        if search_query:
            query += " AND (o.bill_number LIKE %s OR c.name LIKE %s OR c.phone LIKE %s)"
            pattern = f"%{search_query}%"
            params.extend([pattern, pattern, pattern])

        if start_date:
            query += " AND DATE(o.created_at) >= %s"
            params.append(start_date)

        if end_date:
            query += " AND DATE(o.created_at) <= %s"
            params.append(end_date)

        query += " ORDER BY o.created_at DESC LIMIT %s"
        params.append(limit)

        try:
            return DatabaseManager.execute_query(query, tuple(params), fetch_all=True) or []
        except Exception as e:
            logger.error(f"Error fetching recent orders: {e}")
            return []

    @classmethod
    def cancel_order(cls, order_id):
        """Cancels/voids an order."""
        query = "UPDATE orders SET order_status = 'cancelled' WHERE id = %s"
        try:
            DatabaseManager.execute_query(query, (order_id,), commit=True)
            logger.info(f"Order ID {order_id} marked as cancelled.")
            return True
        except Exception as e:
            logger.error(f"Error cancelling order ID {order_id}: {e}")
            return False
