"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: February 16, 2025
Author: Xiaochen Wang

Main module that implements MVC pattern for energy export data management.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from views.console_view import ConsoleView
from services.data_service import DataService
from controllers.record_controller import RecordController

def main():
    """
    Main program entry point.
    Initializes MVC components and starts the application.
    """
    # Initialize MVC components
    view = ConsoleView()
    service = DataService()
    controller = RecordController(view, service)

    # Start the application
    try:
        controller.run()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
    finally:
        print("\nThank you for using the program!")
        print(f"Program by Xiaochen Wang")

if __name__ == "__main__":
    main()