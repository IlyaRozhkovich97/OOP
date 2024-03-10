from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def create_product(self, **kwargs):
        """Абстрактный метод для создания продукта."""
        pass


class ReprMixin:
    """Миксин для вывода информации о создании объекта в консоль."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__repr__()

    def __repr__(self):
        """Метод вывода информации о созданном объекте."""
        attributes = ', '.join(f"{value}" for value in self.__dict__.values())
        return (f"\033[91mСоздан объект класса\033[0m {self.__class__.__name__} \033[91mс атрибутами: "
                f"\033[0m{attributes}")


class Product_(AbstractProduct, ReprMixin, ABC):
    """Класс для продуктов."""

    def __init__(self, name, description, price, quantity, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.__repr__()

    def create_product(self, **kwargs):
        """Метод для создания нового продукта."""
        return self.__class__(**kwargs)


class Smartphone_(Product_):
    """Класс для смартфонов."""

    def __init__(self, name, description, price, quantity, performance, model, storage_capacity, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color


class LawnGrass_(Product_):
    """Класс для травы газонной."""

    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color


product = Product_('Продукт1', 'Описание продукта', 1200, 10)
smartphone = Smartphone_("Смартфон", "Мощный смартфон", 1000, 10, "Apple",
                         "iPhone 12", "256 ГБ", "Чёрный")
lawn_grass = LawnGrass_("Трава", "Смесь для газонов", 50, 100, "Россия",
                        "30 дней", "Зелёный")

print(product)
print(smartphone)
print(lawn_grass)
