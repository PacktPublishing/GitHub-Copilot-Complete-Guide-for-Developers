# nes_demos.py

def calculate_area(length, width):
  """Calculates the area of a rectangle."""
  if length <= 0 or width <= 0:
    print("Error: Dimensions must be positive.")
    return None
  return length * width

def print_details(item_name, length, width):
  """Prints details including the calculated area."""
  area = calculate_area(length, width)
  if area is not None:
    print(f"Item: {item_name}")
    print(f"Dimensions: {length} x {width}")
    print(f"Calculated Area: {area}")
  else:
    print(f"Could not calculate area for {item_name}.")


# --- Usage Example ---
print("Calculating for Box A:")
print_details("Box A", 10, 5)

print("\nCalculating for Sheet B:")
print_details("Sheet B", 20, 15)
