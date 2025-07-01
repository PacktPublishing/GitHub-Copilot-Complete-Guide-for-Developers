# math_utils.py
def calculate(a, b):
    """Multiply a by b, with a simple loop (inefficiently)."""
    result = 0
    for _ in range(a):
        result += b
    return result
