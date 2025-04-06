"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: March 16, 2025
Author: Xiaochen Wang

This module contains the RecordController class for managing business logic.
Supports polymorphic record handling and display.
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
                self.display_records("detailed")
            elif choice == '4':
                self.display_records("summary")
            elif choice == '5':
                self.add_record()
            elif choice == '6':
                self.edit_record()
            elif choice == '7':
                self.delete_record()
            elif choice == '8':
                self.multi_column_sort()
            elif choice == '9':
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

    def display_records(self, format_type="detailed"):
        """
        Display records in specified format.
        
        Args:
            format_type: String indicating display format ('detailed' or 'summary')
        """
        if not self.service.records:
            print("\nNo records to display. Please load data first.")
            return
        self.view.display_records(self.service.records, format_type)

    def add_record(self):
        """Add a new record with user input."""
        print("\nEnter record details:")
        try:
            data = [
                input("Period (YYYY-MM): "),
                input("Year: "),
                input("Month: "),
                input("Product: "),
                input("Origin: "),
                input("Destination: "),
                input("Mode: "),
                input("Volume (m3): "),
                input("Volume (bbl): "),
                input("Value (CAD): "),
                input("Value (USD): "),
                input("Price (CAD cents/L): "),
                input("Price (USD cents/gal): ")
            ]
            
            format_type = input("\nEnter record type (detailed/summary): ").lower()
            record = self.service.create_record(data, format_type)
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
        """Delete a record by index."""
        if not self.service.records:
            print("\nNo records to delete. Please load data first.")
            return

        # Display current records
        self.display_records()
        
        try:
            index = int(input("\nEnter the record number to delete (1-N): ")) - 1
            if 0 <= index < len(self.service.records):
                deleted_record = self.service.records.pop(index)
                print(f"\nRecord #{index + 1} deleted successfully.")
            else:
                print("\nInvalid record number.")
        except ValueError:
            print("\nPlease enter a valid number.")
            
    def multi_column_sort(self):
        """Sort records based on multiple columns."""
        if not self.service.records:
            print("\nNo records to sort. Please load data first.")
            return
            
        # Show available columns to sort by
        available_columns = [
            'period', 'year', 'month', 'product', 'origin', 'destination',
            'mode', 'volume_m3', 'volume_bbl', 'value_cad', 'value_usd',
            'price_cad_cents_per_l', 'price_usd_cents_per_gal'
        ]
        
        print("\nAvailable columns for sorting:")
        for i, column in enumerate(available_columns, 1):
            print(f"{i}. {column}")
        
        # Get columns to sort by
        try:
            sort_columns = []
            sort_orders = []
            
            # Get number of columns to sort by
            num_columns = int(input("\nHow many columns do you want to sort by? (1-3): "))
            if num_columns < 1 or num_columns > 3:
                print("Invalid number. Please enter a number between 1 and 3.")
                return
                
            for i in range(num_columns):
                # Get column selection
                column_num = int(input(f"\nSelect column #{i+1} (1-{len(available_columns)}): "))
                if 1 <= column_num <= len(available_columns):
                    selected_column = available_columns[column_num - 1]
                    sort_columns.append(selected_column)
                    
                    # Get sort direction
                    direction = input(f"Sort {selected_column} in ascending order? (y/n): ").lower()
                    sort_orders.append(direction == 'y')
                else:
                    print("Invalid column number.")
                    return
            
            # Perform the sort
            sorted_records = self.service.sort_records_multi_column(sort_columns, sort_orders)
            
            # Update the records in service
            self.service.records = sorted_records
            
            # Display sorted records
            print("\nRecords sorted successfully!")
            self.display_records()
            
        except ValueError:
            print("\nInvalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"\nError sorting records: {str(e)}")