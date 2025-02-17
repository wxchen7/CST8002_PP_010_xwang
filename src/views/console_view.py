"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: Feb 16, 2025
Author: Xiaochen Wang

This module contains the ConsoleView class for user interface.
"""

class ConsoleView:
    def __init__(self):
        self.author = "Xiaochen Wang"

    def display_header(self):
        """Display program header with author name"""
        print("\n" + "=" * 50)
        print("CST8002 Energy Export Data Analysis")
        print(f"Program by {self.author}")
        print("=" * 50 + "\n")

    def display_menu(self):
        """Display main menu options"""
        self.display_header()
        print("Menu Options:")
        print("1. Load/Reload Data")
        print("2. Save Data")
        print("3. Display Records")
        print("4. Add New Record")
        print("5. Edit Record")
        print("6. Delete Record")
        print("7. Exit")

    def get_user_choice(self):
        """Get user menu choice"""
        return input("\nEnter your choice (1-7): ")

    def display_records(self, records):
        """Display records with author name every 10 records"""
        if not records:
            print("No records to display.")
            return

        for i, record in enumerate(records, 1):
            print(f"\nRecord #{i}:")
            print(record)
            if i % 10 == 0:
                self.display_header()

    def get_record_input(self):
        """Get input for a new record"""
        print("\nEnter record details:")
        return {
            'period': input("Period (YYYY-MM): "),
            'year': input("Year: "),
            'month': input("Month: "),
            'product': input("Product: "),
            'origin': input("Origin: "),
            'destination': input("Destination: "),
            'mode': input("Mode: "),
            'volume_m3': input("Volume (m3): "),
            'volume_bbl': input("Volume (bbl): "),
            'value_cad': input("Value (CAD): "),
            'value_usd': input("Value (USD): "),
            'price_cad_cents_per_l': input("Price (CAD cents/L): "),
            'price_usd_cents_per_gal': input("Price (USD cents/gal): ")
        }