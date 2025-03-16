"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: March 16, 2025
Author: Xiaochen Wang

This module contains the Record class hierarchy for energy export data management.
Implements polymorphic behavior for different display formats.
"""

import uuid

class Record:
    """
    Base class for energy export records.
    Provides foundation for polymorphic display formatting.
    """

    def __init__(self, period, year, month, product, origin, destination,
                 mode, volume_m3, volume_bbl, value_cad, value_usd,
                 price_cad_cents_per_l, price_usd_cents_per_gal):
        """Initialize a new Record instance with the provided data."""
        self.id = str(uuid.uuid4())
        self.period = period
        self.year = year
        self.month = month
        self.product = product
        self.origin = origin
        self.destination = destination
        self.mode = mode
        self.volume_m3 = volume_m3
        self.volume_bbl = volume_bbl
        self.value_cad = value_cad
        self.value_usd = value_usd
        self.price_cad_cents_per_l = price_cad_cents_per_l
        self.price_usd_cents_per_gal = price_usd_cents_per_gal

    def __str__(self):
        """Return a string representation of the record."""
        return (f"Period: {self.period}\n"
                f"Year: {self.year}\n"
                f"Month: {self.month}\n"
                f"Product: {self.product}\n"
                f"Origin: {self.origin}\n"
                f"Destination: {self.destination}\n"
                f"Mode: {self.mode}\n"
                f"Volume (m3): {self.volume_m3}\n"
                f"Volume (bbl): {self.volume_bbl}\n"
                f"Value (CN$): {self.value_cad}\n"
                f"Value (US$): {self.value_usd}\n"
                f"Price (CN cents/L): {self.price_cad_cents_per_l}\n"
                f"Price (US cents/gallon): {self.price_usd_cents_per_gal}")

    def format_data(self):
        """
        Base method for polymorphic data formatting.
        This method will be overridden by subclasses to provide different display formats.

        Returns:
            str: Formatted string representation of the record
        """
        return self.__str__()

    def to_csv_row(self):
        """Convert record to CSV format"""
        return f"{self.period},{self.year},{self.month},{self.product},{self.origin}," \
               f"{self.destination},{self.mode},{self.volume_m3},{self.volume_bbl}," \
               f"{self.value_cad},{self.value_usd},{self.price_cad_cents_per_l}," \
               f"{self.price_usd_cents_per_gal}"

class DetailedRecord(Record):
    """
    Detailed view of energy export records.
    Provides comprehensive formatting with all available fields.
    """

    def format_data(self):
        """
        Override format_data to provide detailed view of record.
        
        Returns:
            str: Formatted string with comprehensive record details
        """
        return (f"=== Detailed Energy Export Record ===\n"
                f"Record ID: {self.id}\n"
                f"Time Information:\n"
                f"  - Period: {self.period}\n"
                f"  - Year: {self.year}\n"
                f"  - Month: {self.month}\n\n"
                f"Product Details:\n"
                f"  - Type: {self.product}\n"
                f"  - Origin: {self.origin}\n"
                f"  - Destination: {self.destination}\n"
                f"  - Transport Mode: {self.mode}\n\n"
                f"Volume Measurements:\n"
                f"  - Cubic Meters: {self.volume_m3}\n"
                f"  - Barrels: {self.volume_bbl}\n\n"
                f"Financial Information:\n"
                f"  - Value (CAD): ${self.value_cad}\n"
                f"  - Value (USD): ${self.value_usd}\n"
                f"  - Price (CAD cents/L): {self.price_cad_cents_per_l}\n"
                f"  - Price (USD cents/gal): {self.price_usd_cents_per_gal}")

class SummaryRecord(Record):
    """
    Summarized view of energy export records.
    Provides concise formatting with key fields only.
    """

    def format_data(self):
        """
        Override format_data to provide summarized view of record.
        
        Returns:
            str: Formatted string with key record information
        """
        return (f"Summary: {self.period} | "
                f"Product: {self.product} | "
                f"Route: {self.origin} → {self.destination} | "
                f"Volume: {self.volume_m3}m³ | "
                f"Value: ${self.value_cad} CAD")