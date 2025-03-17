"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: March 16, 2025
Author: Xiaochen Wang

This module contains unit tests for the DataService class.
Tests file operations and data management functionality.
"""

import unittest
import os
from src.services.data_service import DataService


class TestDataService(unittest.TestCase):
    def setUp(self):
        """
        Set up test fixtures before each test method.
        Initializes the DataService instance.
        """
        print("\n" + "=" * 50)
        print("Program by Xiaochen Wang")
        print("Testing DataService Class")
        print("=" * 50 + "\n")

        self.service = DataService()

    def test_file_not_found(self):
        """
        Test case: Verify error handling for non-existent file.
        Ensures the service handles missing files appropriately.
        """
        result = self.service.read_file("nonexistent.csv")
        self.assertFalse(result)
        print("File not found test passed!")


if __name__ == '__main__':
    unittest.main(verbosity=2)