from abc import ABC, abstractmethod

class Promotion(ABC):
    """
    Abstract base class for all promotions.
    """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass

    def __str__(self):
        return self.name


class PercentDiscount(Promotion):
    """
    Applies a percentage-based discount.
    """
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        discount_price = product.price * (1 - self.percent / 100)
        return discount_price * quantity


class SecondHalfPrice(Promotion):
    """
    Every second item is 50% off.
    """
    def apply_promotion(self, product, quantity) -> float:
        full_price = product.price
        half_price_items = quantity // 2
        normal_items = quantity - half_price_items
        return (normal_items * full_price) + (half_price_items * full_price * 0.5)


class ThirdOneFree(Promotion):
    """
    For every 3 items, 1 is free (Buy 2 Get 1 Free).
    """
    def apply_promotion(self, product, quantity) -> float:
        group_count = quantity // 3
        paid_items = quantity - group_count
        return paid_items * product.price
