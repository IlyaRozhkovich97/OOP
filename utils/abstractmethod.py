from abc import ABC, abstractmethod


class Product(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_info(self):
        """Абстрактный метод для получения информации о продукте."""
        pass

    @abstractmethod
    def calculate_total_price(self):
        """Абстрактный метод для вычисления общей стоимости продукта."""
        pass


class Smartphone(Product):
    """Класс для смартфонов."""

    def __init__(self, name, description, price, quantity, performance, model, storage_capacity, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color

    def get_info(self):
        return (f"{self.name}, {self.model}, {self.performance}, {self.storage_capacity}, {self.color}, "
                f"{self.price} руб., Остаток: {self.quantity} шт.")

    def calculate_total_price(self):
        return self.price * self.quantity


class LawnGrass(Product):
    """Класс для травы газонной."""

    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def get_info(self):
        return (f"{self.name}, {self.country_of_origin}, {self.germination_period}, {self.color}, "
                f"{self.price} руб., Остаток: {self.quantity} шт.")

    def calculate_total_price(self):
        return self.price * self.quantity
