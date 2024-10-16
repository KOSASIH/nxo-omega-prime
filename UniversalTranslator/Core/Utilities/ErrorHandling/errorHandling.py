import sqlite3
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ErrorHandling:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def log_error(self, error_code, user_id=None, spacecraft_id=None, additional_info=None):
        """Log an error occurrence in the database."""
        try:
            # Fetch the error code ID
            self.cursor.execute("SELECT id FROM error_codes WHERE error_code = ?", (error_code,))
            error_code_id = self.cursor.fetchone()
            if error_code_id is None:
                logging.error(f"Error code '{error_code}' not found.")
                return

            # Insert the error log
            self.cursor.execute("""
                INSERT INTO error_logs (error_code_id, user_id, spacecraft_id, additional_info)
                VALUES (?, ?, ?, ?)
            """, (error_code_id[0], user_id, spacecraft_id, additional_info))
            self.connection.commit()
            logging.info(f"Logged error: {error_code} for user ID: {user_id}, spacecraft ID: {spacecraft_id}")
        except Exception as e:
            logging.error(f"Failed to log error: {e}")

    def get_error_info(self, error_code):
        """Retrieve error information based on the error code."""
        try:
            self.cursor.execute("SELECT * FROM error_codes WHERE error_code = ?", (error_code,))
            error_info = self.cursor.fetchone()
            if error_info:
                logging.info(f"Retrieved error info for code '{error_code}': {error_info}")
                return error_info
            else:
                logging.warning(f"No information found for error code '{error_code}'.")
                return None
        except Exception as e:
            logging.error(f"Failed to retrieve error info: {e}")

    def get_error_logs(self, user_id=None, spacecraft_id=None):
        """Retrieve error logs filtered by user ID or spacecraft ID."""
        try:
            query = "SELECT el.timestamp, ec.error_code, ec.error_message FROM error_logs el JOIN error_codes ec ON el.error_code_id = ec.id WHERE 1=1"
            params = []

            if user_id is not None:
                query += " AND el.user_id = ?"
                params.append(user_id)
            if spacecraft_id is not None:
                query += " AND el.spacecraft_id = ?"
                params.append(spacecraft_id)

            self.cursor.execute(query, params)
            logs = self.cursor.fetchall()
            logging.info(f"Retrieved {len(logs)} error logs.")
            return logs
        except Exception as e:
            logging.error(f"Failed to retrieve error logs: {e}")

    def close_connection(self):
        """Close the database connection."""
        self.connection.close()
        logging.info("Database connection closed.")

if __name__ == "__main__":
    # Example usage
    db_path = 'path/to/errorCodes.db'  # Update with the actual path to your database
    error_handler = ErrorHandling(db_path)

    # Log an error
    error_handler.log_error('E001', user_id=1, spacecraft_id=101, additional_info='Engine failure detected.')

    # Retrieve error information
    error_info = error_handler.get_error_info('E001')
    print(error_info)

    # Retrieve error logs for a specific user
    user_logs = error_handler.get_error_logs(user_id=1)
    print(user_logs)

    # Retrieve error logs for a specific spacecraft
    spacecraft_logs = error_handler.get_error_logs(spacecraft_id=101)
    print(spacecraft_logs)

    error_handler.close_connection()
