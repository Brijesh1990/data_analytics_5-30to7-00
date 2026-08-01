import sys
from tkinter import messagebox
import ttkbootstrap as tb
from database.init_db import initialize_database
from database.connection import DatabaseManager
from utils.logger import logger
from ui.app import RajdhaniPOSApp

def main():
    """
    Main application entry point.
    Bootstraps database initialization and launches Tkinter UI event loop.
    """
    logger.info("===========================================")
    logger.info("Starting Rajdhani Restaurant POS System")
    logger.info("===========================================")

    # Initialize database tables & seed data
    db_ok, db_msg = initialize_database()
    if not db_ok:
        logger.warning(f"Database initialization warning: {db_msg}")
        # Show prompt allowing user to retry or continue anyway
        root = tb.Window(hidden=True)
        resp = messagebox.askretrycancel(
            "Database Connection Warning",
            f"Could not connect to MySQL database on localhost:3306.\n\nError details: {db_msg}\n\n"
            "Please ensure your MySQL service (XAMPP / WAMP / MySQL Server) is running.\n\n"
            "Click Retry to attempt reconnection or Cancel to launch in offline mode.",
            parent=root
        )
        root.destroy()
        if not resp:
            sys.exit(1)

    try:
        app = RajdhaniPOSApp()
        app.mainloop()
    except Exception as e:
        logger.critical(f"Unhandled exception in main loop: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
