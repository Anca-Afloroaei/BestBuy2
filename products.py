class Product:
    """
    Represents a store product with a name, price, quantity, and optional promotion.
    """

    def __init__(self, name: str, price: float, quantity: int):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details: name cannot be empty, and price/quantity must be non-negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # Optional promotion, can be set later


    def get_quantity(self) -> int:
        """Returns the current quantity in stock."""
        return self.quantity


    def set_quantity(self, quantity: int):
        """Sets the quantity and deactivates the product if it reaches zero."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        """Returns True if the product is active."""
        return self.active


    def activate(self):
        """Activates the product."""
        self.active = True


    def deactivate(self):
        """Deactivates the product."""
        self.active = False


    def set_promotion(self, promotion):
        """Sets a promotion on the current product."""
        self.promotion = promotion

    def get_promotion(self):
        """Returns the current promotion."""
        return self.promotion


    def show(self) -> str:
        """Returns a string representation of the product, including promotion if any."""
        product_info = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        if self.promotion:
            product_info += f" [Promotion: {self.promotion}]"
        return product_info


    def buy(self, quantity: int) -> float:
        """
        Handles purchase of a given quantity, applying promotion if set.
        """
        if not self.active:
            raise Exception(f"Product '{self.name}' is not active.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise Exception(f"Only {self.quantity} items available for '{self.name}'.")

        # Apply promotion if available
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        # Update quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price


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

