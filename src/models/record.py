"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: January 26, 2025
Author: Xiaochen Wang

This module contains the Record class.
"""

import uuid

class Record:
    """A class to represent energy export data records."""

    def __init__(self, period, year, month, product, origin, destination,
                 mode, volume_m3, volume_bbl, value_cad, value_usd,
                 price_cad_cents_per_l, price_usd_cents_per_gal):
        """Initialize a new Record instance."""
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

    def to_csv_row(self):
        """Convert record to CSV format"""
        return f"{self.period},{self.year},{self.month},{self.product},{self.origin}," \
               f"{self.destination},{self.mode},{self.volume_m3},{self.volume_bbl}," \
               f"{self.value_cad},{self.value_usd},{self.price_cad_cents_per_l}," \
               f"{self.price_usd_cents_per_gal}"