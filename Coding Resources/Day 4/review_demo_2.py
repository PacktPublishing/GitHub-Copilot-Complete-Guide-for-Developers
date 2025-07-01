# review_demo.py (continued)
import os       
import sys 
import math     

def calculate_disk_usage(file_path):
    """
    Calculates disk usage. Intentionally includes unused imports
    and a potentially risky operation for demonstration.
    """
    try:
        size_bytes = os.path.getsize(file_path)
        return size_bytes
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

print(f"Fixed output: {calculate_disk_usage("example.txt")}")  # Example usage