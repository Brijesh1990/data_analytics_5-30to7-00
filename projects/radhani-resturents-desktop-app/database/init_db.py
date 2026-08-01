import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mysql.connector
from mysql.connector import Error
from config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME, BASE_DIR
from database.connection import DatabaseManager
from utils.logger import logger

def initialize_database():
    """
    Checks if database and required tables exist.
    If not, creates the database and executes schema.sql to populate structure and seed data.
    """
    logger.info("Initializing Rajdhani POS database...")
    try:
        # Step 1: Connect to MySQL server without database
        conn = DatabaseManager.get_server_connection()
        cursor = conn.cursor()

        # Step 2: Create Database if not exists
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        cursor.close()
        conn.close()
        logger.info(f"Database `{DB_NAME}` checked/created successfully.")

        # Step 3: Connect to rajdhani_pos_db and run schema.sql
        db_conn = DatabaseManager.get_connection()
        db_cursor = db_conn.cursor()

        schema_path = os.path.join(BASE_DIR, "schema.sql")
        if os.path.exists(schema_path):
            with open(schema_path, "r", encoding="utf-8") as f:
                sql_script = f.read()

            # Parse statements cleanly skipping comments
            statements = []
            current_stmt = []
            for line in sql_script.splitlines():
                line_str = line.strip()
                if not line_str or line_str.startswith("--") or line_str.startswith("#"):
                    continue
                current_stmt.append(line)
                if line_str.endswith(";"):
                    statements.append("\n".join(current_stmt))
                    current_stmt = []

            for stmt in statements:
                clean_stmt = stmt.strip()
                if clean_stmt:
                    try:
                        db_cursor.execute(clean_stmt)
                    except Error as err:
                        if err.errno != 1062:  # Ignore duplicate entry on seed re-runs
                            logger.warning(f"SQL statement execution notice ({err.errno}): {err.msg}")

            logger.info("Schema & sample seed data applied successfully.")
        else:
            logger.warning(f"schema.sql not found at {schema_path}. Manual schema setup required.")

        db_cursor.close()
        db_conn.close()
        return True, "Database initialization completed."

    except Error as e:
        msg = f"Database initialization failed: {e}"
        logger.error(msg)
        return False, msg
    except Exception as ex:
        msg = f"Unexpected error during DB init: {ex}"
        logger.error(msg)
        return False, msg

if __name__ == "__main__":
    success, message = initialize_database()
    print(message)
