class ReprMixin:
    def __repr__(self):
        attributes = ', '.join(f"{value}" for value in self.__dict__.values())
        return f"{self.__class__.__name__}({attributes})"


class Product(ReprMixin):
    """Базовый класс для всех продуктов."""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Smartphone(ReprMixin):
    """Класс для смартфонов."""

    def __init__(self, name, description, price, quantity, performance, model, storage_capacity, color):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.performance = performance
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color


class LawnGrass(ReprMixin):
    """Класс для травы газонной."""

    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color


# Пример использования
product = Product('Продукт1', 'Описание продукта', 1200, 10)
print(product)

smartphone = Smartphone("Смартфон", "Мощный смартфон", 1000, 10, "Apple",
                        "iPhone 12", "256 ГБ", "Чёрный")
print(smartphone)

lawn_grass = LawnGrass("Трава", "Смесь для газонов", 50, 100, "Россия",
                       "30 дней", "Зелёный")
print(lawn_grass)
