"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: March 16, 2025
Author: Xiaochen Wang

This module contains unit tests for the Record class hierarchy.
Tests polymorphic behavior of different record formats.
"""

import unittest
from src.models.record import Record, DetailedRecord, SummaryRecord

class TestRecordFormats(unittest.TestCase):
    """Test cases for Record class hierarchy and polymorphic behavior."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        print("\n" + "=" * 50)
        print("Program by Xiaochen Wang")
        print("Testing Record Format Classes")
        print("=" * 50 + "\n")

        # Test data
        self.test_data = [
            "2023-01", "2023", "01", "Natural Gas", "Alberta", "USA",
            "Pipeline", "1000", "6289.8", "1000000", "750000",
            "10.0", "3.78"
        ]

    def test_polymorphic_behavior(self):
        """
        Test polymorphic behavior of record formats.
        Verifies that each record type formats data differently.
        """
        # Create different types of records
        base_record = Record(*self.test_data)
        detailed_record = DetailedRecord(*self.test_data)
        summary_record = SummaryRecord(*self.test_data)

        # Store in list of base type to demonstrate polymorphism
        records = [base_record, detailed_record, summary_record]

        # Test each record's format
        base_output = records[0].format_data()
        detailed_output = records[1].format_data()
        summary_output = records[2].format_data()

        # Verify each format is different
        self.assertNotEqual(base_output, detailed_output)
        self.assertNotEqual(base_output, summary_output)
        self.assertNotEqual(detailed_output, summary_output)

        # Verify specific format characteristics
        self.assertIn("=== Detailed Energy Export Record ===", detailed_output)
        self.assertIn("Summary:", summary_output)
        
        print("Polymorphic behavior test passed!")

    def test_inheritance_relationship(self):
        """
        Test inheritance relationships between classes.
        Verifies proper class hierarchy implementation.
        """
        detailed_record = DetailedRecord(*self.test_data)
        summary_record = SummaryRecord(*self.test_data)

        # Test inheritance
        self.assertIsInstance(detailed_record, Record)
        self.assertIsInstance(summary_record, Record)
        
        print("Inheritance relationship test passed!")

if __name__ == '__main__':
    unittest.main(verbosity=2) 