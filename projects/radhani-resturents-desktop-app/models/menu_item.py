from database.connection import DatabaseManager
from utils.logger import logger

class MenuItem:
    """Menu Item Model handling item details, pricing, and stock."""

    @classmethod
    def get_all(cls, category_id=None, search_term=None, available_only=True):
        """
        Retrieves menu items with optional category filter and search term.
        """
        query = """
            SELECT m.*, c.name AS category_name
            FROM menu_items m
            JOIN categories c ON m.category_id = c.id
            WHERE 1=1
        """
        params = []

        if available_only:
            query += " AND m.is_available = 1 AND c.is_active = 1"

        if category_id and str(category_id) != "0" and str(category_id).lower() != "all":
            query += " AND m.category_id = %s"
            params.append(category_id)

        if search_term:
            query += " AND (m.name LIKE %s OR m.item_code LIKE %s OR m.description LIKE %s)"
            pattern = f"%{search_term}%"
            params.extend([pattern, pattern, pattern])

        query += " ORDER BY c.display_order ASC, m.item_code ASC"

        try:
            return DatabaseManager.execute_query(query, tuple(params), fetch_all=True) or []
        except Exception as e:
            logger.error(f"Error fetching menu items: {e}")
            return []

    @classmethod
    def get_by_id(cls, item_id):
        """Retrieves a single menu item by ID."""
        query = "SELECT m.*, c.name AS category_name FROM menu_items m JOIN categories c ON m.category_id = c.id WHERE m.id = %s"
        try:
            return DatabaseManager.execute_query(query, (item_id,), fetch_one=True)
        except Exception as e:
            logger.error(f"Error fetching menu item by ID {item_id}: {e}")
            return None

    @classmethod
    def create(cls, category_id, item_code, name, price, description="", food_type="veg", stock_quantity=100, is_inventory_tracked=0, is_available=1):
        """Creates a new menu item."""
        query = """
            INSERT INTO menu_items (category_id, item_code, name, price, description, food_type, stock_quantity, is_inventory_tracked, is_available)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (category_id, item_code, name, price, description, food_type, stock_quantity, is_inventory_tracked, is_available)
        try:
            item_id = DatabaseManager.execute_query(query, params, commit=True)
            logger.info(f"Created menu item '{name}' ({item_code}) with ID {item_id}")
            return item_id
        except Exception as e:
            logger.error(f"Error creating menu item: {e}")
            return None

    @classmethod
    def update(cls, item_id, category_id, item_code, name, price, description="", food_type="veg", stock_quantity=100, is_inventory_tracked=0, is_available=1):
        """Updates an existing menu item."""
        query = """
            UPDATE menu_items
            SET category_id = %s, item_code = %s, name = %s, price = %s, description = %s, food_type = %s, stock_quantity = %s, is_inventory_tracked = %s, is_available = %s
            WHERE id = %s
        """
        params = (category_id, item_code, name, price, description, food_type, stock_quantity, is_inventory_tracked, is_available, item_id)
        try:
            DatabaseManager.execute_query(query, params, commit=True)
            logger.info(f"Updated menu item ID {item_id}")
            return True
        except Exception as e:
            logger.error(f"Error updating menu item ID {item_id}: {e}")
            return False

    @classmethod
    def delete(cls, item_id):
        """Soft deletes / marks menu item as unavailable."""
        query = "UPDATE menu_items SET is_available = 0 WHERE id = %s"
        try:
            DatabaseManager.execute_query(query, (item_id,), commit=True)
            logger.info(f"Deactivated menu item ID {item_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting menu item ID {item_id}: {e}")
            return False

    @classmethod
    def update_stock(cls, item_id, quantity_sold):
        """Decrements stock quantity for inventory tracked items."""
        query = """
            UPDATE menu_items
            SET stock_quantity = GREATEST(0, stock_quantity - %s)
            WHERE id = %s AND is_inventory_tracked = 1
        """
        try:
            DatabaseManager.execute_query(query, (quantity_sold, item_id), commit=True)
        except Exception as e:
            logger.error(f"Error updating stock for item ID {item_id}: {e}")
