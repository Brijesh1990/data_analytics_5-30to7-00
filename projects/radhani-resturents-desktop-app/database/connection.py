import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from mysql.connector import Error
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, DB_CHARSET
from utils.logger import logger

class DatabaseManager:
    """
    Manages MySQL database connection lifecycle, auto-reconnections,
    and automatic database/table initializations.
    """

    @staticmethod
    def get_server_connection():
        """Connects directly to MySQL server instance without selecting a database."""
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASSWORD,
                charset=DB_CHARSET
            )
            return conn
        except Error as e:
            logger.error(f"Failed to connect to MySQL Server at {DB_HOST}:{DB_PORT} - Error: {e}")
            raise e

    @staticmethod
    def get_connection():
        """Connects to the application database (rajdhani_pos_db)."""
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                charset=DB_CHARSET,
                autocommit=True
            )
            return conn
        except Error as e:
            logger.error(f"Database connection error for database '{DB_NAME}': {e}")
            raise e

    @classmethod
    def test_connection(cls) -> tuple[bool, str]:
        """Tests if MySQL server is reachable and database is accessible."""
        try:
            conn = cls.get_connection()
            if conn.is_connected():
                conn.close()
                return True, "Database connected successfully."
        except Error as e:
            return False, str(e)
        return False, "Unknown connection error."

    @classmethod
    def execute_query(cls, query: str, params: tuple = (), fetch_one: bool = False, fetch_all: bool = False, commit: bool = True):
        """Helper method for executing parametrized SQL queries safely."""
        conn = None
        cursor = None
        try:
            conn = cls.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, params)

            result = None
            if fetch_one:
                result = cursor.fetchone()
            elif fetch_all:
                result = cursor.fetchall()
            elif commit:
                result = cursor.lastrowid

            return result
        except Error as e:
            logger.error(f"Query execution error: {e}\nQuery: {query}\nParams: {params}")
            raise e
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()
