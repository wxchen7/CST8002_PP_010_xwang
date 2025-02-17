"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: February 16, 2025
Author: Xiaochen Wang

This module contains the DataService class for handling file operations
and data management.
"""

import csv
import uuid
from src.models.record import Record

class DataService:
    """
    Service class for managing data operations including file I/O
    and record management.
    """
    
    def __init__(self):
        """Initialize DataService with empty records list."""
        self.records = []
        self.filename = "dataset.csv"

    def read_file(self, filename=None):
        """
        Read data from CSV file and create Record objects.
        
        Args:
            filename (str, optional): Path to the CSV file. 
                                    Defaults to initial filename.
        
        Returns:
            bool: True if successful, False otherwise
        """
        if filename:
            self.filename = filename
            
        try:
            self.records = []  # Clear existing records
            with open(self.filename, 'r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip header row

                # Read first 100 records
                for _ in range(100):
                    try:
                        row = next(csv_reader)
                        record = Record(*row)
                        self.records.append(record)
                    except StopIteration:
                        break
            return True
            
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return False
        except Exception as e:
            print(f"Error reading file: {str(e)}")
            return False

    def save_file(self):
        """
        Save records to a new CSV file with UUID filename.
        
        Returns:
            str: Name of the created file, or None if failed
        """
        try:
            filename = f"output_{uuid.uuid4()}.csv"
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for record in self.records:
                    writer.writerow([
                        record.period, record.year, record.month,
                        record.product, record.origin, record.destination,
                        record.mode, record.volume_m3, record.volume_bbl,
                        record.value_cad, record.value_usd,
                        record.price_cad_cents_per_l, 
                        record.price_usd_cents_per_gal
                    ])
            return filename
        except Exception as e:
            print(f"Error saving file: {str(e)}")
            return None