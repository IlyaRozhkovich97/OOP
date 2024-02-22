import json


class Category:
    """Класс категории"""
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str):
        """
        Инициализатор класса Category.
        name: Название категории.
        description: Описание категории.
        products: Список продуктов в данной категории.
        """
        self.name = name
        self.description = description
        self.__products = []
        Category.total_categories += 1

    def add_product(self, product):
        """Добавление продукта в категорию"""
        self.__products.append(product)
        Category.total_unique_products += 1

    @property
    def products(self):
        """Геттер для списка товаров."""
        return self.__products

    @property
    def get_products_format(self):
        """Метод для форматирования списка товаров."""
        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return product_list


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


def load_data_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    categories = []
    for category_data in data:
        category = Category(category_data['name'], category_data['description'])
        for product_data in category_data['products']:
            product = Product(product_data['name'], product_data['description'], product_data['price'],
                              product_data['quantity'])
            category.add_product(product)
        categories.append(category)
    return categories


categories = load_data_from_json('products.json')

for category in categories:
    print(f"Категория: {category.name}")
    print(f"Описание: {category.description}")
    print("Список товаров:")
    for product_format in category.get_products_format:
        print(product_format)
    print()

print(f"Всего категорий: {Category.total_categories}")
print(f"Общее количество продуктов: {Product.total_products}")
print(f"Общее количество уникальных продуктов: {Category.total_unique_products}\n")

product = Product.create_product("Xiaomi 14 pro", "256GB, Серый цвет, 200MP камера", 50.0, 100)

# Вывод информации о созданном продукте
print("Проврека нового товара:")
print("Товар:", product.name)
print("Описание:", product.description)
print("Цена:", product.price)
print(f"Количество: {product.quantity}\n")

print("Проверка отрицательно значения:")
#new_price = int(input("Введите новую цену: "))
product.price = -500
print("Текущая цена после попыток изменения:", product.price)
