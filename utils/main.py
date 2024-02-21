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
        self.products = []
        Category.total_categories += 1

    def add_product(self, product):
        """Добавление продукта в категорию"""
        self.products.append(product)
        Category.total_unique_products += 1


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
        self.price = price
        self.quantity = quantity
        Product.total_products += 1


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
    for product in category.products:
        print(
            f" - Товар: {product.name}, Описание: {product.description}, Цена: {product.price},"
            f"Количество: {product.quantity}")
    print()


print(f"Всего категорий: {Category.total_categories}")
print(f"Общее количество продуктов: {Product.total_products}")
print(f"Общее количество уникальных продуктов: {Category.total_unique_products}")
