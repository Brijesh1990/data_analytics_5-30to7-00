import csv
import os
import datetime
from config import EXPORTS_DIR
from utils.logger import logger

class CSVExporter:
    """Utility for exporting reports and data tables to CSV files."""

    @classmethod
    def export_to_csv(cls, filename_prefix, headers, rows):
        """
        Exports headers and list of row dicts or tuples to a CSV file in exports directory.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{filename_prefix}_{timestamp}.csv"
        file_path = os.path.join(EXPORTS_DIR, file_name)

        try:
            with open(file_path, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(headers)

                for row in rows:
                    if isinstance(row, dict):
                        row_vals = [row.get(h, "") for h in headers]
                        writer.writerow(row_vals)
                    elif isinstance(row, (list, tuple)):
                        writer.writerow(row)

            logger.info(f"Successfully exported {len(rows)} rows to {file_path}")
            return True, file_path
        except Exception as e:
            msg = f"Failed to export CSV: {e}"
            logger.error(msg)
            return False, msg
