# main.py
"""
Main application script to process data.
"""
from data_processor import DataProcessor
import config

def generate_report(processor):
    """Generates a simple report based on the processed data."""
    print("\n--- Data Report ---")

    # Get total values per category
    category_values = processor.get_total_value_by_category()
    print("\nTotal Value by Category:")
    for category, total in category_values.items():
        if category in config.RELEVANT_CATEGORIES: # Use config
            print(f"- {category}: ${total}")

    # Find high-value items
    high_value = processor.find_high_value_items()
    print(f"\nHigh-Value Items (>${config.HIGH_VALUE_THRESHOLD}):")
    if high_value:
        for item in high_value:
            print(f"- {item['Name']} (${item['Value']})")
    else:
        print("No high-value items found.")

    print("--- End Report ---\n")

def run_analysis():
    """Runs the data analysis process."""
    print(f"Starting analysis using data file: {config.DATA_FILEPATH}")
    processor = DataProcessor() # Uses filepath from config by default

    if processor.get_data(): # Check if data loaded successfully
        generate_report(processor)
    else:
        print("Analysis aborted due to data loading issues.")

if __name__ == "__main__":
    run_analysis()