import json
from utils.product import Product


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
        if isinstance(product, Product):
            if product.quantity == 0:
                raise ValueError("Товар с нулевым количеством не может быть добавлен.")
            self.__products.append(product)
            Category.total_unique_products += 1
        else:
            raise TypeError("Можно добавить только объекты класса Product или его наследников.")

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

    def __len__(self):
        """Магический метод для получения длины категории."""
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        """Строковое отображение категории."""
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def create_product(self, **kwargs):
        """Метод для создания нового продукта из словаря с данными."""
        product = Product(**kwargs)
        self.add_product(product)
        print(f"Продукт '{product.name}' успешно создан и добавлен в категорию '{self.name}'.")
        return product

    def average_price(self):
        """Метод для подсчета среднего ценника всех товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            print("Нет товаров в категории.")
            return 0


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
