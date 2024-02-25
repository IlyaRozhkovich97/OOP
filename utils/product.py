class Product:
    """Классы продукт"""

    total_products = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализатор класса Product.
        name: Название продукта.
        description: Описание продукта.
        price: Цена продукта.
        quantity: Количество продукта.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.total_products += 1

    @classmethod
    def create_product(cls, name: str, description: str, price: float, quantity: int):
        """Создает и возвращает объект продукта."""
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для цены."""
        if value > 0:
            self.__price = value
        else:
            print("Цена введена некорректно.")

    def __str__(self):
        """Строковое отображение продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        total_price = (self.price * self.quantity) + (other.price * other.quantity)
        return f"Результат сложений: {total_price}"
