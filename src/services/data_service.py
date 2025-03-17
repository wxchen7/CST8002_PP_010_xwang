"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: March 16, 2025
Author: Xiaochen Wang

This module contains the DataService class for data operations.
Supports creation of different record types.
"""

import csv
from src.models.record import Record, DetailedRecord, SummaryRecord

class DataService:
    """Service class for managing energy export data records."""

    def __init__(self):
        """Initialize DataService."""
        self.filename = "data/natural-gas-liquids-exports-monthly.csv"
        self.records = []
        self.headers = []

    def read_file(self, filename=None):
        """
        Read data from CSV file and create appropriate Record objects.
        Alternates between DetailedRecord and SummaryRecord for demonstration.

        Args:
            filename: Optional custom filename to read from

        Returns:
            bool: True if successful, False otherwise
        """
        if filename:
            self.filename = filename
            
        try:
            self.records = []  # Clear existing records
            with open(self.filename, 'r') as file:
                csv_reader = csv.reader(file)
                self.headers = next(csv_reader)  # Skip header row

                # Read first 100 records
                for i, row in enumerate(csv_reader):
                    if i >= 100:  # Limit to 100 records
                        break
                    # Create alternating record types
                    if i % 2 == 0:
                        record = DetailedRecord(*row)
                    else:
                        record = SummaryRecord(*row)
                    self.records.append(record)
            return True
            
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return False
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return False

    def create_record(self, data, record_type="detailed"):
        """
        Create a new record of specified type.

        Args:
            data: List of record field values
            record_type: String indicating record type ('detailed' or 'summary')

        Returns:
            Record: New record instance of specified type
        """
        if record_type.lower() == "summary":
            return SummaryRecord(*data)
        return DetailedRecord(*data)

    def save_file(self, filename=None):
        """Save records to CSV file."""
        if filename:
            self.filename = filename

        try:
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
                for record in self.records:
                    writer.writerow([
                        record.period, record.year, record.month,
                        record.product, record.origin, record.destination,
                        record.mode, record.volume_m3, record.volume_bbl,
                        record.value_cad, record.value_usd,
                        record.price_cad_cents_per_l, record.price_usd_cents_per_gal
                    ])
            return True
        except Exception as e:
            print(f"Error saving file: {str(e)}")
            return False