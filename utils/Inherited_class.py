from product import Product


class Smartphone(Product):
    """Класс для смартфонов."""

    def __init__(self, name, description, price, quantity, performance, model, storage_capacity, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.storage_capacity = storage_capacity
        self.color = color

    def __str__(self):
        return (f"{self.name}, {self.model}, {self.performance}, {self.storage_capacity}, {self.color}, "
                f"{self.price} руб., Остаток: {self.quantity} шт.")


class LawnGrass(Product):
    """Класс для травы газонной."""

    def __init__(self, name, description, price, quantity, country_of_origin, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (f"{self.name}, {self.country_of_origin}, {self.germination_period}, {self.color}, "
                f"{self.price} руб., Остаток: {self.quantity} шт.")


# Создание экземпляров продуктов
smartphone = Smartphone("Смартфон", "Мощный смартфон", 1000, 10, "Apple", "iPhone 12", "256 ГБ", "Чёрный")
lawn_grass = LawnGrass("Трава", "Смесь для газонов", 50, 100, "Россия", "30 дней", "Зелёный")

# Вывод информации о продуктах
print(smartphone)
print(lawn_grass)
