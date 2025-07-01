class Product:
  """Represents a product with an ID and name."""
  def __init__(self, product_id, name):
    self.product_id = product_id
    self.name = name

# --- Usage Example ---
item1 = Product("A100", "Laptop") # Instantiation 1
item2 = Product("B250", "Keyboard") # Instantiation 2
item3 = Product("C250", "Burger") # Instantiation 3