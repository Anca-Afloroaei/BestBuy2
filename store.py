from typing import List, Tuple
from products import Product


class Store:
    """
    Represents a store containing a list of products.
    Provides functionality to add/remove products, retrieve available products,
    get total quantity, and process customer orders.
    """

    def __init__(self, products: List[Product]):
        """
        Initializes the store with a list of products.
        """
        self.products = products


    def add_product(self, product: Product):
        """
        Adds a new product to the store
        """
        self.products.append(product)


    def remove_product(self, product: Product):
        """
        Removes a product from the store, if it exists.
        """

        if product in self.products:
            self.products.remove(product)


    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products in the store.
        """
        return sum(product.get_quantity() for product in self.products)


    def get_all_products(self) -> List[Product]:
        """
        Returns a list of all active products in the store.
        """
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """
        Processes an order consisting of a list of (product, quantity) tuples.
        """
        total_cost = 0.0
        for product, quantity in shopping_list:
            total_cost += product.buy(quantity)
        return total_cost
