import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime

# Updated data to match the graph
values = [
    4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.1, 3.9, 3.8, 3.9, 4.0, 4.1,
    4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.6, 4.5, 4.4, 4.3, 4.2, 4.3,
    4.4, 4.5, 4.6, 4.7, 4.5, 4.4, 4.3, 4.2, 4.3, 4.4, 4.5, 4.6,
    4.7, 4.5, 4.4, 4.3, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.5, 4.4,
    4.3, 4.2
]

# Adjust the dates to match the length of values
dates = pd.date_range(start="2024-05-01", periods=len(values), freq="D")

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(dates, values, label="Value", color="blue")

# Add a horizontal line at 4.3090
plt.axhline(y=4.3090, color="red", linestyle="--", label="4.3090")

# Format the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_minor_locator(mdates.WeekdayLocator())
plt.gcf().autofmt_xdate()

# Add labels, title, and legend
plt.title("Exchange Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Exchange Rate")
plt.legend()

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
