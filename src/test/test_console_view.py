"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: Feb 16, 2025
Author: Xiaochen Wang

This module contains unit tests for the ConsoleView class.
Tests the display functionality and user interface components.
"""

import unittest
import io
import sys
from src.views.console_view import ConsoleView

class TestConsoleView(unittest.TestCase):
    def setUp(self):
        """
        Set up test fixtures before each test method.
        Initializes the ConsoleView instance and captures stdout.
        """
        print("\n" + "=" * 50)
        print("Program by Xiaochen Wang")
        print("Testing ConsoleView Class")
        print("=" * 50 + "\n")
        
        self.view = ConsoleView()
        # Capture standard output for testing
        self.held_output = io.StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        """
        Clean up after each test method.
        Restores the standard output.
        """
        sys.stdout = sys.__stdout__

    def test_display_header(self):
        """
        Test case: Verify header display includes author name.
        Ensures the program header shows the author's name correctly.
        """
        self.view.display_header()
        output = self.held_output.getvalue()
        self.assertIn("Xiaochen Wang", output)
        print("Header display test passed!")

    def test_display_menu(self):
        """
        Test case: Verify menu display functionality.
        Ensures all menu options are displayed correctly.
        """
        self.view.display_menu()
        output = self.held_output.getvalue()
        self.assertIn("Menu Options:", output)
        self.assertIn("1. Load/Reload Data", output)
        self.assertIn("7. Exit", output)
        print("Menu display test passed!")

if __name__ == '__main__':
    unittest.main(verbosity=2)