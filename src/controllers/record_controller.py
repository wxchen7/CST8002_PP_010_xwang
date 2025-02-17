"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: February 16, 2025
Author: Xiaochen Wang

This module contains the RecordController class for managing business logic.
"""

from src.models.record import Record


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
        filename = input("\nEnter filename (press Enter for default 'dataset.csv'): ")
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
        """Add a new record to the collection."""
        record_data = self.view.get_record_input()
        new_record = Record(**record_data)
        self.service.records.append(new_record)
        print("\nRecord added successfully!")

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
        """Delete an existing record."""
        if not self.service.records:
            print("\nNo records to delete.")
            return

        self.display_records()
        try:
            index = int(input("\nEnter record number to delete (1-{}): ".format(len(self.service.records)))) - 1
            if 0 <= index < len(self.service.records):
                del self.service.records[index]
                print("\nRecord deleted successfully!")
            else:
                print("\nInvalid record number.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")