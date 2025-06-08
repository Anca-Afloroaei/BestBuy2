class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details: name cannot be empty, and price/quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity: int) -> float:
        if not self.active:
            raise Exception("Product is not active.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise Exception("Not enough stock to complete the purchase.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity



class NonStockedProduct(Product):
    """
    A special type of product that is not tracked by quantity (e.g., digital/non-physical products).
    Always shows quantity as 0 and cannot modify quantity.
    Example: Software licenses.
    """

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        """Prevents changing the quantity for non-stocked products."""
        pass  # Quantity remains 0

    def get_quantity(self):
        return 0

    def buy(self, quantity):
        """Allows purchases without affecting quantity."""
        if not self.active:
            raise Exception(f"Product '{self.name}' is not active.")
        return self.price * quantity

    def show(self) -> str:
        return f"{self.name} (Non-Stocked), Price: {self.price}"


class LimitedProduct(Product):
    """
    A product with a per-order purchase limit (e.g., shipping fee - only once per order).
    """

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        """Overrides base buy method to enforce a maximum quantity per order."""
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} of '{self.name}' in one order.")
        return super().buy(quantity)

    def show(self) -> str:
        return f"{self.name} (Limited to {self.maximum} per order), Price: {self.price}, Quantity: {self.quantity}"

