"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: March 16, 2025
Author: Xiaochen Wang

This module contains the ConsoleView class for user interface.
Supports polymorphic record display.
"""

class ConsoleView:
    def __init__(self):
        """Initialize ConsoleView with author information."""
        self.author = "Xiaochen Wang"

    def display_header(self):
        """Display program header with author name."""
        print("\n" + "=" * 50)
        print("CST8002 Energy Export Data Analysis")
        print(f"Program by {self.author}")
        print("=" * 50 + "\n")

    def display_menu(self):
        """Display main menu options."""
        self.display_header()
        print("Menu Options:")
        print("1. Load/Reload Data")
        print("2. Save Data")
        print("3. Display Records (Detailed)")
        print("4. Display Records (Summary)")
        print("5. Add New Record")
        print("6. Edit Record")
        print("7. Delete Record")
        print("8. Multi-Column Sort")
        print("9. Exit")

    def get_user_choice(self):
        """Get user menu choice."""
        return input("\nEnter your choice (1-9): ")

    def display_records(self, records, format_type="detailed"):
        """
        Display records with polymorphic formatting.
        
        Args:
            records: List of Record objects
            format_type: String indicating display format ('detailed' or 'summary')
        """
        if not records:
            print("No records to display.")
            return
        
        from src.models.record import DetailedRecord, SummaryRecord
        
        for i, record in enumerate(records, 1):
            print(f"\nRecord #{i}:")
            
            # 根据选择的format_type临时创建对应类型的记录
            if format_type.lower() == "detailed":
                # 创建详细记录类型
                temp_record = DetailedRecord(
                    record.period, record.year, record.month, record.product,
                    record.origin, record.destination, record.mode, record.volume_m3,
                    record.volume_bbl, record.value_cad, record.value_usd,
                    record.price_cad_cents_per_l, record.price_usd_cents_per_gal
                )
                print(temp_record.format_data())
            else:  # summary
                # 创建摘要记录类型
                temp_record = SummaryRecord(
                    record.period, record.year, record.month, record.product,
                    record.origin, record.destination, record.mode, record.volume_m3,
                    record.volume_bbl, record.value_cad, record.value_usd,
                    record.price_cad_cents_per_l, record.price_usd_cents_per_gal
                )
                print(temp_record.format_data())
            
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