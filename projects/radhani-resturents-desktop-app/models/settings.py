from database.connection import DatabaseManager
from config import DEFAULT_SETTINGS
from utils.logger import logger

class Settings:
    """Settings Model managing dynamic configuration persistence in database."""

    @classmethod
    def get_all(cls):
        """Retrieves all application settings as a dictionary."""
        query = "SELECT setting_key, setting_value FROM settings"
        settings_dict = DEFAULT_SETTINGS.copy()
        try:
            rows = DatabaseManager.execute_query(query, fetch_all=True)
            if rows:
                for row in rows:
                    settings_dict[row["setting_key"]] = row["setting_value"]
            return settings_dict
        except Exception as e:
            logger.error(f"Error fetching settings: {e}")
            return settings_dict

    @classmethod
    def get(cls, key, default=None):
        """Retrieves a single setting value by key."""
        query = "SELECT setting_value FROM settings WHERE setting_key = %s"
        try:
            row = DatabaseManager.execute_query(query, (key,), fetch_one=True)
            if row:
                return row["setting_value"]
            return DEFAULT_SETTINGS.get(key, default)
        except Exception as e:
            logger.error(f"Error fetching setting key '{key}': {e}")
            return DEFAULT_SETTINGS.get(key, default)

    @classmethod
    def save_setting(cls, key, value, description=""):
        """Saves or updates a single setting key."""
        query = """
            INSERT INTO settings (setting_key, setting_value, description)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE setting_value = %s, description = %s
        """
        try:
            DatabaseManager.execute_query(query, (key, str(value), description, str(value), description), commit=True)
            logger.info(f"Saved setting key '{key}' = '{value}'")
            return True
        except Exception as e:
            logger.error(f"Error saving setting key '{key}': {e}")
            return False

    @classmethod
    def save_all(cls, settings_dict):
        """Saves a batch dictionary of settings."""
        try:
            for key, val in settings_dict.items():
                cls.save_setting(key, val)
            return True
        except Exception as e:
            logger.error(f"Error saving batch settings: {e}")
            return False
