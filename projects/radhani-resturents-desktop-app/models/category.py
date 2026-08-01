from database.connection import DatabaseManager
from utils.logger import logger

class Category:
    """Category Model for menu categorization."""

    @classmethod
    def get_all(cls, active_only=True):
        """Retrieves all categories ordered by display_order."""
        if active_only:
            query = "SELECT * FROM categories WHERE is_active = 1 ORDER BY display_order ASC, name ASC"
        else:
            query = "SELECT * FROM categories ORDER BY display_order ASC, name ASC"
        try:
            return DatabaseManager.execute_query(query, fetch_all=True) or []
        except Exception as e:
            logger.error(f"Error fetching categories: {e}")
            return []

    @classmethod
    def create(cls, name, display_order=0):
        """Creates a new category."""
        query = "INSERT INTO categories (name, display_order) VALUES (%s, %s)"
        try:
            cat_id = DatabaseManager.execute_query(query, (name, display_order), commit=True)
            logger.info(f"Created category '{name}' (ID: {cat_id})")
            return cat_id
        except Exception as e:
            logger.error(f"Error creating category: {e}")
            return None

    @classmethod
    def update(cls, category_id, name, display_order=0, is_active=1):
        """Updates category details."""
        query = "UPDATE categories SET name = %s, display_order = %s, is_active = %s WHERE id = %s"
        try:
            DatabaseManager.execute_query(query, (name, display_order, is_active, category_id), commit=True)
            logger.info(f"Updated category ID {category_id}")
            return True
        except Exception as e:
            logger.error(f"Error updating category ID {category_id}: {e}")
            return False

    @classmethod
    def delete(cls, category_id):
        """Deletes or deactivates category."""
        query = "UPDATE categories SET is_active = 0 WHERE id = %s"
        try:
            DatabaseManager.execute_query(query, (category_id,), commit=True)
            logger.info(f"Deactivated category ID {category_id}")
            return True
        except Exception as e:
            logger.error(f"Error deleting category ID {category_id}: {e}")
            return False
