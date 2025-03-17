"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: February 16, 2025
Author: Xiaochen Wang

This module contains unit tests for the RecordController class.
Tests the business logic and user interaction handling.
"""

import unittest
import io
import sys
from src.controllers.record_controller import RecordController
from src.views.console_view import ConsoleView
from src.services.data_service import DataService
from src.models.record import Record


class TestRecordController(unittest.TestCase):
    def setUp(self):
        """
        Set up test fixtures before each test method.
        Initializes the controller with mock data.
        """
        print("\n" + "=" * 50)
        print("Program by Xiaochen Wang")
        print("Testing RecordController Class")

        self.view = ConsoleView()
        self.service = DataService()
        self.controller = RecordController(self.view, self.service)

        # Add test record
        self.test_record = Record(
            "2023-01", "2023", "01", "Natural Gas", "Alberta", "USA",
            "Pipeline", "1000", "6289.8", "1000000", "750000",
            "10.0", "3.78"
        )
        self.service.records.append(self.test_record)

    def test_display_records(self):
        """
        Test case: Verify records display functionality.
        Ensures the controller can display records correctly.
        """
        # Capture stdout
        held_output = io.StringIO()
        sys.stdout = held_output

        # Test display
        self.controller.display_records()
        output = held_output.getvalue()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify output
        self.assertIn("Natural Gas", output)
        self.assertIn("Alberta", output)
        print("Display records test passed!")

    def test_delete_record(self):
        """
        Test case: Verify record deletion.
        Ensures records can be deleted by ID.
        """
        initial_count = len(self.service.records)
        self.controller.delete_record()
        self.assertEqual(len(self.service.records), initial_count - 1)
        print("Delete record test passed!")


if __name__ == '__main__':
    unittest.main(verbosity=2)