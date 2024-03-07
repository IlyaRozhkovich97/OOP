from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def create_product(self, **kwargs):
        """Абстрактный метод для создания продукта."""
        pass


class ReprMixin:
    def __repr__(self):
        attributes = ', '.join(f"{value}" for value in self.__dict__.values())
        return f"{self.__class__.__name__}({attributes})"


class Product(AbstractProduct, ReprMixin):
    """Класс для продуктов."""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @staticmethod
    def create_product(**kwargs):
        """Метод для создания нового продукта из словаря с данными."""
        return Product(**kwargs)


class Smartphone(Product):
    """Класс для смартфонов."""

    def __init__(self, name, description, price, quantity, performance, model, storage_capacity, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color

    @staticmethod
    def create_product(**kwargs):
        """Метод для создания нового смартфона из словаря с данными."""
        return Smartphone(**kwargs)


class LawnGrass(Product):
    """Класс для травы газонной."""

    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    @staticmethod
    def create_product(**kwargs):
        """Метод для создания новой травы газонной из словаря с данными."""
        return LawnGrass(**kwargs)


product = Product('Продукт1', 'Описание продукта', 1200, 10)
print(product)

smartphone = Smartphone("Смартфон", "Мощный смартфон", 1000, 10, "Apple",
                        "iPhone 12", "256 ГБ", "Чёрный")
print(smartphone)

lawn_grass = LawnGrass("Трава", "Смесь для газонов", 50, 100, "Россия",
                       "30 дней", "Зелёный")
print(lawn_grass)
