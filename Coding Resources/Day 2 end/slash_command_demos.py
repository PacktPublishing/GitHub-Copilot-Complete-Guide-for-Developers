# Function to calculate factorial iteratively
def calculate_factorial(n):
    if not isinstance(n, int) or n < 0:
        # Raising an error for invalid input
        raise ValueError("Input must be a non-negative integer")
    if n == 0 or n == 1:
        return 1

    result = 1
    # Loop from 2 up to n (inclusive)
    for i in range(2, n + 1):
        result *= i # Multiply result by current number
    return result

# Example usage (optional, helps Copilot context)
# print(f"Factorial of 5 is: {calculate_factorial(5)}")