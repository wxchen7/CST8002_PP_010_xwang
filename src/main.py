"""
CST8002 Programming Language Research Project
Professor: Stanley Pieda
Due Date: January 26, 2025
Author: Xiaochen Wang

Main module that demonstrates the Record class.
"""

from src.record import Record


def main():
    """Main function to demonstrate Record class."""
    print("=" * 50)
    print("Energy Export Data Analysis")
    print("Author: Xiaochen Wang")
    print("=" * 50)

    # Create a sample record
    sample_record = Record(
        period="2025-01",
        year="2025",
        month="01",
        product="Crude Oil",
        origin="Alberta",
        destination="United States",
        mode="Pipeline",
        volume_m3="1000000",
        volume_bbl="6289811",
        value_cad="50000000",
        value_usd="37500000",
        price_cad_cents_per_l="50",
        price_usd_cents_per_gal="189"
    )

    # Display the record
    print("\nSample Record:")
    print(sample_record)


if __name__ == "__main__":
    main()