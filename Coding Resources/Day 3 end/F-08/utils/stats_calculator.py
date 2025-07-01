# utils/stats_calculator.py
import math

import logging
logging.basicConfig(level=logging.INFO)
project_logger = logging.getLogger("StatsCalc")

class BasicStats:
    """A simple class to calculate basic statistics."""

    def __init__(self, data):
        if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("Input must be a list of numbers.")
        self.data = data

    def calculate_mean(self):
        """Calculates the mean of the data."""
        project_logger.info(f"Calculating mean for {len(self.data)} items.") # Added logging
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)
    
    def calculate_std_dev(self):
        """Calculates the stdev of the data."""
        if len(self.data) < 2:
            return 0 # requires at least 2 points
        mean = self.calculate_mean()
        variance = sum([(x - mean) ** 2 for x in self.data]) / (len(self.data) - 1)
        return math.sqrt(variance)

def format_report(mean, std_dev):
    """Formats the stats into a simple report string."""
    return f"Statistics Report: Mean = {mean:.2f}, Std Dev = {std_dev:.2f}"

print("Stats Calculator module loaded.") # To confirm import

