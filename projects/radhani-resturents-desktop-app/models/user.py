from database.connection import DatabaseManager
from utils.helpers import hash_password
from utils.logger import logger

class User:
    """User Model representing system operators (Admin / Cashier)."""

    def __init__(self, user_id=None, username="", full_name="", role="cashier", phone="", is_active=True):
        self.id = user_id
        self.username = username
        self.full_name = full_name
        self.role = role
        self.phone = phone
        self.is_active = is_active

    @classmethod
    def authenticate(cls, username, password):
        """
        Authenticates user against username and SHA-256 hashed password.
        Returns User instance if valid, None if invalid.
        """
        hashed_pwd = hash_password(password)
        query = "SELECT * FROM users WHERE username = %s AND password_hash = %s AND is_active = 1"
        try:
            row = DatabaseManager.execute_query(query, (username, hashed_pwd), fetch_one=True)
            if row:
                logger.info(f"User '{username}' logged in successfully as {row['role']}.")
                return cls(
                    user_id=row["id"],
                    username=row["username"],
                    full_name=row["full_name"],
                    role=row["role"],
                    phone=row.get("phone", ""),
                    is_active=bool(row.get("is_active", 1))
                )
            else:
                logger.warning(f"Failed login attempt for username: '{username}'")
                return None
        except Exception as e:
            logger.error(f"Authentication error: {e}")
            return None

    @classmethod
    def get_all(cls):
        """Retrieves all registered system users."""
        query = "SELECT id, username, full_name, role, phone, is_active, created_at FROM users ORDER BY id ASC"
        try:
            rows = DatabaseManager.execute_query(query, fetch_all=True)
            return rows or []
        except Exception as e:
            logger.error(f"Error fetching users: {e}")
            return []

    @classmethod
    def change_password(cls, user_id, new_password):
        """Updates user password to new SHA-256 hash."""
        hashed_pwd = hash_password(new_password)
        query = "UPDATE users SET password_hash = %s WHERE id = %s"
        try:
            DatabaseManager.execute_query(query, (hashed_pwd, user_id), commit=True)
            logger.info(f"Password updated for user ID: {user_id}")
            return True
        except Exception as e:
            logger.error(f"Error changing password: {e}")
            return False
