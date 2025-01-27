"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: January 26, 2025
Author: Xiaochen Wang

Main module that demonstrates the Record class.
"""

import csv
from src.record import Record


def read_energy_data(file_path):
    """
    Read energy export data from CSV file.
    Args:
        file_path: Path to the CSV file
    Returns:
        list: A list of Record objects containing the data
    """
    records = []
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row

            # Read first 10 records
            for _ in range(10):
                row = next(csv_reader)
                record = Record(*row)
                records.append(record)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file: {str(e)}")

    return records


def main():
    """
    Main function to run the program.
    Reads data from CSV file and displays records.
    """
    print("=" * 50)
    print("Energy Export Data Analysis")
    print("Author: Xiaochen Wang")
    print("=" * 50)

    # Read data from CSV file
    data_file = "data/natural-gas-liquids-exports-monthly.csv"
    records = read_energy_data(data_file)

    if records:
        print(f"Successfully loaded {len(records)} records:")
        # Loop through and display each record
        for i, record in enumerate(records, 1):
            print(f"\nRecord #{i}:")
            print(record)
            print("-" * 50)
    else:
        print("No records were loaded.")


if __name__ == "__main__":
    main()