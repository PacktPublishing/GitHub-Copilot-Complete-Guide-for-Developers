import pandas as pd
import matplotlib.pyplot as plt

def visualize_profit(data_frame):
    """
    Visualizes the profit by product using a bar chart.
    """
    # check if the required columns exist in the DataFrame
    if 'Sales' not in data_frame.columns or 'Cost' not in data_frame.columns:
        raise ValueError("DataFrame must contain 'Sales' and 'Cost' columns")
    data_frame['Profit'] = data_frame['sales'] - data_frame['Cost']
    data_frame.plot(x='Product', y='Profit', kind='bar', legend=False, title='Profit by Product')
    plt.ylabel('Profit')
    plt.show()