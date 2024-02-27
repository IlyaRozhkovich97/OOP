from category import Category, load_data_from_json
from product import Product
from Inherited_class import Smartphone, LawnGrass

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
# new_price = int(input("Введите новую цену: "))
product.price = -500
print(f"Текущая цена после попыток изменения:, {product.price}\n")

# Проверяем __str__ в классе Product
product = Product("Название продукта", "Описание продукта", 80, 15)
print(f"Проверяем __str__ в классе Product:\n{product}\n")

# Проверяем __str__  и __len__ в классе Category
category = Category("Название категории", "Описание категории")
product1 = Product("Продукт 1", "Описание продукта 1", 100, 5)
product2 = Product("Продукт 2", "Описание продукта 2", 200, 3)
category.add_product(product1)
category.add_product(product2)
print(f"Проверяем __str__  и __len__ в классе Category:\n{category}\n")

# Проверяем __add__ в классе Product
product1 = Product("Продукт A", "Описание продукта A", 100, 10)
product2 = Product("Продукт B", "Описание продукта B", 200, 2)
result = product1 + product2
print(f"Проверяем __add__ в классе Product:\n{result}\n")

print(f"Проверяем наследования:")
# Создание экземпляров продуктов
smartphone = Smartphone("Смартфон", "Мощный смартфон", 1000, 10, "Apple",
                        "iPhone 12", "256 ГБ", "Чёрный")
lawn_grass = LawnGrass("Трава", "Смесь для газонов", 50, 100, "Россия",
                       "30 дней", "Зелёный")

# Вывод информации о продуктах
print(smartphone)
print(lawn_grass)

print("\nПроверка сложения продуктов разных типов:")
try:
    mixed_result = smartphone + lawn_grass
except TypeError as e:
    print(e)
