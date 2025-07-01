# data_processing/loader.py
import json
import os

class DataLoader:
    """Handles loading data from different file formats."""

    def __init__(self, source_path):
        self.source_path = source_path
        if not os.path.exists(source_path):
             print(f"Warning: Source path {source_path} does not exist yet.")
        # In a real app, you might establish connections or configs here

    def load_json_data(self):
        """Loads numerical data from a JSON file."""
        try:
            with open(self.source_path, 'r') as f:
                raw_data = json.load(f)
            # Assume json contains a list of numbers under a 'values' key
            if isinstance(raw_data, dict) and 'values' in raw_data:
                return [x for x in raw_data['values'] if isinstance(x, (int, float))]
            else:
                print(f"Error: JSON file {self.source_path} does not have expected format.")
                return []
        except FileNotFoundError:
            print(f"Error: File not found at {self.source_path}")
            return []
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from {self.source_path}")
            return []

    def get_source_description(self):
        """Returns a description of the data source."""
        return f"Data loaded from file: {os.path.basename(self.source_path)}"

# Helper function within this module
def check_file_accessibility(filepath):
    """Checks if a file exists and is readable."""
    return os.path.exists(filepath) and os.access(filepath, os.R_OK)

print("Data Loader module loaded.")