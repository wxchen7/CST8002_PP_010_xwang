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
        # Special case for test data
        if filename == "test":
            self._load_test_data()
            return True
            
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

    def _load_test_data(self):
        """Load test data for sort demonstration."""
        self.records = []
        self.headers = ['period', 'year', 'month', 'product', 'origin', 'destination',
                        'mode', 'volume_m3', 'volume_bbl', 'value_cad', 'value_usd',
                        'price_cad_cents_per_l', 'price_usd_cents_per_gal']
        
        # Create sample test data with various values to demonstrate sorting
        test_data = [
            ['2023-01', '2023', '1', 'Propane', 'Alberta', 'USA', 'Pipeline', '1000', '6290', '500000', '375000', '50', '160'],
            ['2023-01', '2023', '1', 'Butane', 'Ontario', 'Mexico', 'Ship', '2000', '12580', '800000', '600000', '40', '130'],
            ['2023-02', '2023', '2', 'Propane', 'Alberta', 'Japan', 'Ship', '1500', '9435', '700000', '525000', '46', '150'],
            ['2023-01', '2023', '1', 'Ethane', 'Quebec', 'USA', 'Pipeline', '3000', '18870', '900000', '675000', '30', '95'],
            ['2023-03', '2023', '3', 'Propane', 'Alberta', 'China', 'Ship', '2500', '15725', '1200000', '900000', '48', '155'],
            ['2023-02', '2023', '2', 'Butane', 'Ontario', 'USA', 'Pipeline', '1800', '11322', '750000', '562500', '42', '135'],
            ['2023-01', '2023', '1', 'Propane', 'Alberta', 'Mexico', 'Ship', '2200', '13838', '950000', '712500', '43', '140'],
            ['2023-03', '2023', '3', 'Ethane', 'Quebec', 'Japan', 'Ship', '2800', '17612', '1100000', '825000', '39', '125'],
            ['2023-02', '2023', '2', 'Propane', 'Alberta', 'USA', 'Pipeline', '1600', '10064', '650000', '487500', '41', '132'],
            ['2023-03', '2023', '3', 'Butane', 'Ontario', 'China', 'Ship', '3200', '20128', '1300000', '975000', '41', '131']
        ]
        
        # Create alternating record types from test data
        for i, row in enumerate(test_data):
            if i % 2 == 0:
                record = DetailedRecord(*row)
            else:
                record = SummaryRecord(*row)
            self.records.append(record)
        
        print("Test data loaded successfully!")

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
            
    def sort_records_multi_column(self, sort_columns, sort_orders):
        """
        Sort records based on multiple columns simultaneously.

        Args:
            sort_columns: List of column names to sort by
            sort_orders: List of sort directions (True for ascending, False for descending)

        Returns:
            list: Sorted list of records
        """
        if not self.records:
            return []
            
        if not sort_columns:
            return self.records
            
        # Create a copy of records to sort
        sorted_records = self.records.copy()
        
        # Sort records by each column in reverse order to get correct multi-column sort
        for i in range(len(sort_columns) - 1, -1, -1):
            column = sort_columns[i]
            is_ascending = sort_orders[i]
            
            # Convert numeric values to appropriate types for sorting
            def get_sort_key(record):
                value = getattr(record, column)
                
                # Handle numeric fields
                numeric_fields = ['year', 'month', 'volume_m3', 'volume_bbl', 
                                 'value_cad', 'value_usd', 'price_cad_cents_per_l', 
                                 'price_usd_cents_per_gal']
                                 
                if column in numeric_fields:
                    try:
                        return float(value) if value else 0
                    except (ValueError, TypeError):
                        return 0
                return value if value else ""
            
            sorted_records.sort(key=get_sort_key, reverse=not is_ascending)
        
        return sorted_records