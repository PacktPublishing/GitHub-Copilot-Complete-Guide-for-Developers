import matplotlib.pyplot as plt

# Data from the graph
years = [1990, 1992, 1994, 1996, 1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024]
unemployment_rate = [5.6, 7.5, 6.9, 5.6, 4.9, 4.2, 4.7, 5.5, 4.6, 5.8, 9.3, 8.1, 6.2, 5.3, 3.9, 8.1, 3.6, 4.0]

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(years, unemployment_rate, marker='o', color='blue', label='Unemployment Rate')

# Adding labels and title
plt.title('Unemployment Rate Over Time', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Unemployment Rate (%)', fontsize=12)
plt.ylim(3, 10)  # Setting y-axis limits
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.legend()

# Show the graph
plt.tight_layout()
plt.show()
