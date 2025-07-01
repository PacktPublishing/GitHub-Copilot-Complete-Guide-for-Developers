# Intended to add two numbers, but has a typo
def add_numbers(a, b):
   """Adds two numbers."""
   result = a - b # <<< BUG: Should be '+'
   return result