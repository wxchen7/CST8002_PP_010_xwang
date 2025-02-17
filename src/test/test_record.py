"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: Feb 16, 2025
Author: Xiaochen Wang

Unit tests for Record class.
"""

import unittest
from src.models.record import Record

class TestRecord(unittest.TestCase):
    def setUp(self):
        """Set up test case"""
        print("\n" + "=" * 50)
        print("Program by Xiaochen Wang")
        print("Testing Record Class")
        print("=" * 50 + "\n")

        self.test_record = Record(
            "2023-01", "2023", "01", "Natural Gas", "Alberta", "USA",
            "Pipeline", "1000", "6289.8", "1000000", "750000",
            "10.0", "3.78"
        )

    def test_to_csv_row(self):
        """Test if record can be converted to CSV format correctly"""
        print("Testing CSV conversion...")
        expected_csv = "2023-01,2023,01,Natural Gas,Alberta,USA,Pipeline,1000,6289.8,1000000,750000,10.0,3.78"
        actual_csv = self.test_record.to_csv_row()
        self.assertEqual(expected_csv, actual_csv)
        print("CSV conversion test passed!")

if __name__ == '__main__':
    unittest.main(verbosity=2)