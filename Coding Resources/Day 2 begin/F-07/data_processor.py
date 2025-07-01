# data_processor.py
"""
Contains the DataProcessor class for loading and analyzing data.
"""
import csv
import config # Import configuration

class DataProcessor:
    def __init__(self, filepath=config.DATA_FILEPATH):
        """Initializes the DataProcessor with a file path."""
        self.filepath = filepath
        self.data = []
        self.load_data() # Load data on initialization

    def load_data(self):
        """Loads data from the CSV file specified in the config."""
        try:
            with open(self.filepath, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
            print(f"Successfully loaded {len(self.data)} records from {self.filepath}")
        except FileNotFoundError:
            print(f"Error: File not found at {self.filepath}")
            self.data = []
        except Exception as e:
            print(f"An unexpected error occurred during loading: {e}")
            self.data = []

    def get_total_value_by_category(self):
        """Calculates the total value for each category."""
        category_totals = {}
        for row in self.data:
            category = row.get('Category', 'Unknown')
            try:
                value = int(row.get('Value', 0))
                category_totals[category] = category_totals.get(category, 0) + value
            except (ValueError, TypeError):
                print(f"Warning: Skipping row with invalid 'Value': {row}")
        return category_totals

    def find_high_value_items(self):
        """Finds items exceeding the high value threshold from config."""
        high_value_items = []
        for row in self.data:
            try:
                if int(row.get('Value', 0)) > config.HIGH_VALUE_THRESHOLD:
                    high_value_items.append(row)
            except (ValueError, TypeError):
                continue # Ignore rows with invalid values for this check
        return high_value_items

    def get_data(self):
        """Returns the loaded data."""
        return self.data

# Example of a standalone function (could be used for #symbol demo)
def check_file_exists(path):
    """Simple function to check if a file exists."""
    import os
    return os.path.exists(path)