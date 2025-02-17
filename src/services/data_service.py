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
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.record import Record

class DataService:
    """
    Service class for managing data operations including file I/O
    and record management.
    """

    def __init__(self):
        """Initialize DataService with empty records list."""
        self.records = []
        self.filename = "data/natural-gas-liquids-exports-monthly.csv"
        self.headers = None  # add headers attribute

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
            if not filename.startswith('data/'):
                filename = f"data/{filename}"
            self.filename = filename
            
        try:
            self.records = []  # Clear existing records
            with open(self.filename, 'r') as file:
                csv_reader = csv.reader(file)
                self.headers = next(csv_reader)  # 保存表头

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
        """Save records to a new CSV file with UUID filename."""
        try:
            filename = f"data/output_{uuid.uuid4()}.csv"
            print("\nSaving records to file:")
            print(f"Total records to save: {len(self.records)}")
            print("First record in memory:")
            if self.records:
                print(f"  Period: {self.records[0].period}")
                print(f"  Product: {self.records[0].product}")
                print(f"  Mode: {self.records[0].mode}")
            
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                
                # 写入表头
                if self.headers:
                    print("Writing headers:", self.headers)
                    writer.writerow(self.headers)
                
                # 写入记录
                for i, record in enumerate(self.records):
                    row = [
                        record.period, record.year, record.month,
                        record.product, record.origin, record.destination,
                        record.mode, record.volume_m3, record.volume_bbl,
                        record.value_cad, record.value_usd,
                        record.price_cad_cents_per_l, 
                        record.price_usd_cents_per_gal
                    ]
                    writer.writerow(row)
                    if i == 0:
                        print("First record written to file:", row)
                
                print(f"Successfully saved {len(self.records)} records")
                return filename
        except Exception as e:
            print(f"Error saving file: {str(e)}")
            return None