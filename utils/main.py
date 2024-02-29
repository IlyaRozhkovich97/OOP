from category import Category, load_data_from_json
from utils.product import Product
from inherited_class import Smartphone, LawnGrass

categories = load_data_from_json('products.json')

print("\n\033[91mПроверка категорий:\033[0m")
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
print("\033[91mПроверка нового товара:\033[0m")
print("Товар:", product.name)
print("Описание:", product.description)
print("Цена:", product.price)
print(f"Количество: {product.quantity}\n")

# Проверка отрицательно значения
print("\033[91mПроверка отрицательно значения:\033[0m")
# new_price = int(input("Введите новую цену: "))
product.price = -500
print(f"Текущая цена после попыток изменения:, {product.price}\n")

# Проверяем __str__ в классе Product
product = Product("Название продукта", "Описание продукта", 80, 15)
print(f"\033[91mПроверяем __str__ в классе Product:\033[0m\n{product}\n")

# Проверяем __str__  и __len__ в классе Category
category = Category("Название категории", "Описание категории")
product1 = Product("Продукт 1", "Описание продукта 1", 100, 5)
product2 = Product("Продукт 2", "Описание продукта 2", 200, 3)
other_object = "Просто строка"
print(f"\033[91mПроверяем __str__  и __len__ в классе Category:\033[0m\n{category}\n")

# Проверяем __add__ в классе Product
product3 = Product("Продукт A", "Описание продукта A", 100, 10)
product4 = Product("Продукт B", "Описание продукта B", 200, 2)
result = product4 + product4
print(f"\033[91mПроверяем __add__ в классе Product:\033[0m\n{result}\n")

# Проверяем наследования
print(f"\033[91mПроверяем наследования:\033[0m")

smartphone = Smartphone("Смартфон", "Мощный смартфон", 1000, 10, "Apple",
                        "iPhone 12", "256 ГБ", "Чёрный")
lawn_grass = LawnGrass("Трава", "Смесь для газонов", 50, 100, "Россия",
                       "30 дней", "Зелёный")
print(smartphone)
print(lawn_grass)

# Проверка сложения продуктов разных типов
print("\n\033[91mПроверка сложения продуктов разных типов:\033[0m")
try:
    mixed_result = smartphone + lawn_grass
except TypeError as e:
    print(e)

print("\n\033[91mДобавление продукта в категорию add_product:\033[0m")
# Создаем категорию "Электроника"
electronics_category = Category("Электроника", "Товары электроники и бытовой техники")

# Создаем несколько продуктов
product1 = Product("Ноутбук", "Мощный ноутбук для работы и игр", 1500, 10)
product2 = Product("Смартфон", "Смартфон с высоким разрешением камеры", 800, 20)
product3 = Product("Наушники", "Беспроводные наушники с хорошим звуком", 200, 30)
# other_object = "Ничего"
# Добавляем продукты в категорию "Электроника"
try:
    electronics_category.add_product(product1)
    electronics_category.add_product(product2)
    electronics_category.add_product(product3)
    # electronics_category.add_product(other_object)
    print("Продукты успешно добавлены в категорию!")
except TypeError as e:
    print(f"Ошибка при добавлении продукта: {e}")

# Выводим информацию о категории после добавления продуктов
print("Список продуктов в категории 'Электроника':")
for product in electronics_category.products:
    print(product)

# Метод для создания нового продукта из словаря с данными
print("\n\033[91mCоздания нового продукта из словаря с данными:\033[0m")
new_product = category.create_product(name="Новый продукт", description="Описание продукта", price=100, quantity=50)
print(new_product)
