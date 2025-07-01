def calculate_difference_between_two_dates(date1, date2, difference_type):
    """
    Calculate the difference between two dates in days, weeks, or months.

    Args:
        date1 (str): The first date in 'YYYY-MM-DD' format.
        date2 (str): The second date in 'YYYY-MM-DD' format.
        difference_type (str): The type of difference to calculate ('days', 'weeks', 'months', 'minutes', 'hours').
    returns:
        int: The difference between the two dates in the specified unit.
    """
    from datetime import datetime, timedelta

    # Convert string dates to datetime objects
    date1 = datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')

    # Calculate the difference between the two dates
    delta = abs((date2 - date1).days)

    if difference_type == 'days':
        return delta
    elif difference_type == 'weeks':
        return delta // 7
    elif difference_type == 'months':
        return (date2.year - date1.year) * 12 + (date2.month - date1.month)
    elif difference_type == 'minutes':
        return delta * 24 * 60
    elif difference_type == 'hours':
        return delta * 24
    else:
        raise ValueError("Invalid difference type. Choose from 'days', 'weeks', 'months', 'minutes', or 'hours'.")  