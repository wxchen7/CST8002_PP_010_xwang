"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: February 16, 2025
Author: Xiaochen Wang

This module contains the RecordController class for managing business logic.
"""

from src.models.record import Record
from src.services.data_service import DataService
from src.views.console_view import ConsoleView


class RecordController:
    """
    Controller class for managing business logic between View and Service layers.
    Handles user interactions and data operations.
    """

    def __init__(self, view, service):
        """
        Initialize RecordController with view and service instances.

        Args:
            view: ConsoleView instance for user interface
            service: DataService instance for data operations
        """
        self.view = view
        self.service = service

    def run(self):
        """Main program loop handling user interactions."""
        while True:
            self.view.display_menu()
            choice = self.view.get_user_choice()

            if choice == '1':
                self.load_data()
            elif choice == '2':
                self.save_data()
            elif choice == '3':
                self.display_records()
            elif choice == '4':
                self.add_record()
            elif choice == '5':
                self.edit_record()
            elif choice == '6':
                self.delete_record()
            elif choice == '7':
                print("\nExiting program...")
                break
            else:
                print("\nInvalid choice. Please try again.")

    def load_data(self):
        """Load or reload data from file."""
        filename = input("\nEnter filename (press Enter for default 'natural-gas-liquids-exports-monthly.csv'): ")
        if filename and not filename.startswith('data/'):
            # add data/ prefix if not provided
            filename = f"data/{filename}"
        if self.service.read_file(filename if filename else None):
            print("Data loaded successfully!")
        else:
            print("Failed to load data.")

    def save_data(self):
        """Save current records to a new file."""
        filename = self.service.save_file()
        if filename:
            print(f"\nData saved successfully to {filename}")
        else:
            print("\nFailed to save data.")

    def display_records(self):
        """Display all records."""
        self.view.display_records(self.service.records)

    def add_record(self):
        """Add a new record."""
        if len(self.service.records) >= 100:
            print("\nMaximum number of records (100) reached. Cannot add more records.")
            return

        print("\nEnter record details:")
        try:
            period = input("Period (e.g., 01/01/1990): ")
            year = input("Year (e.g., 1990): ")
            month = input("Month (e.g., January): ")
            product = input("Product (e.g., Butane): ")
            origin = input("Origin (e.g., Alberta): ")
            destination = input("Destination / PADD: ")
            mode = input("Mode of Transportation: ")
            volume_m3 = input("Volume (m3): ")
            volume_bbl = input("Volume (bbl): ")
            value_cad = input("Value (CN$): ")
            value_usd = input("Value (US$): ")
            price_cad_cents_per_l = input("Price (CN cents/L): ")
            price_usd_cents_per_gal = input("Price (US cents/gallon): ")

            record = Record(
                period, year, month, product, origin, destination, mode,
                volume_m3, volume_bbl, value_cad, value_usd,
                price_cad_cents_per_l, price_usd_cents_per_gal
            )
            
            self.service.records.append(record)
            print("\nRecord added successfully!")
            
        except Exception as e:
            print(f"\nError adding record: {str(e)}")

    def edit_record(self):
        """Edit an existing record."""
        if not self.service.records:
            print("\nNo records to edit.")
            return

        self.display_records()
        try:
            index = int(input("\nEnter record number to edit (1-{}): ".format(len(self.service.records)))) - 1
            if 0 <= index < len(self.service.records):
                record_data = self.view.get_record_input()
                self.service.records[index] = Record(**record_data)
                print("\nRecord updated successfully!")
            else:
                print("\nInvalid record number.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

    def delete_record(self):
        """Delete a record by ID."""
        if not self.service.records:
            print("\nNo records to delete.")
            return

        print("\nCurrent Records:")
        for i, record in enumerate(self.service.records, 1):
            print(f"\nRecord #{i}")
            print(f"Record ID: {record.id}")
            print("Period:", record.period)
            print("Year:", record.year)
            print("Product:", record.product)
            print("Origin:", record.origin)
            print("Mode:", record.mode)  # add more fields for identification
            print("-" * 30)

        print("\nProgram by Xiaochen Wang")
        
        try:
            record_id = input("\nEnter the record ID to delete: ").strip()
            print(f"\nAttempting to delete record with ID: {record_id}")
            
            # print the number of records before deletion
            print(f"Records before deletion: {len(self.service.records)}")
            
            found = False
            for i, record in enumerate(self.service.records):
                print(f"Checking record #{i+1}:")
                print(f"  ID: {record.id}")
                print(f"  Period: {record.period}")
                print(f"  Product: {record.product}")
                
                if record.id == record_id:
                    # print the detailed information of the record to delete
                    print(f"\nFound matching record at position {i+1}:")
                    print(f"  Current record: {record.period}, {record.product}, {record.origin}")
                    
                    deleted_record = self.service.records.pop(i)
                    print(f"\nSuccessfully deleted record #{i+1}:")
                    print(deleted_record)
                    found = True
                    
                    # print the number of records after deletion
                    print(f"Records after deletion: {len(self.service.records)}")
                    break
            
            if not found:
                print(f"\nRecord with ID {record_id} was not found.")
            
        except Exception as e:
            print(f"\nError deleting record: {str(e)}")
            print(f"Error type: {type(e)}")
            import traceback
            traceback.print_exc()