import pytest
from utils.category import Category
from utils.product import Product


@pytest.fixture
def reset_totals():
    Category.total_categories = 0
    Category.total_unique_products = 0
    Product.total_products = 0


def test_category_initialization(reset_totals):
    category = Category("Смартфоны",
                        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для "
                        "удобства жизни")
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, но и получение дополнительных "
                                    "функций для удобства жизни")
    assert category.products == []
    assert Category.total_categories == 1


def test_add_product_to_category(reset_totals):
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получение дополнительных "
                                     "функций для"
                                     "удобства жизни")
    product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("iPhone 13", "128GB, Синий цвет, 12MP камера", 120000.0, 10)

    category.add_product(product1)
    assert len(category.products) == 1
    assert Category.total_unique_products == 1

    category.add_product(product2)
    assert len(category.products) == 2
    assert Category.total_unique_products == 2


def test_get_products_format(reset_totals):
    category = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получение дополнительных "
                                     "функций для удобства жизни")
    product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("iPhone 13", "128GB, Синий цвет, 12MP камера", 120000.0, 10)

    category.add_product(product1)
    category.add_product(product2)

    expected_output = [
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "iPhone 13, 120000.0 руб. Остаток: 10 шт."
    ]

    assert category.get_products_format == expected_output


def test_len_method(reset_totals):
    category = Category("Тест Category", "Это тестовая категория")
    product1 = Product("Продукт 1", "Описание 1", 100, 5)
    product2 = Product("Продукт 2", "Описание 2", 200, 10)

    assert len(category) == 0

    category.add_product(product1)
    assert len(category) == 5

    category.add_product(product2)
    assert len(category) == 15


def test_str_method(reset_totals):
    category = Category("Тест Category", "Это тестовая категория")
    product1 = Product("Продукт 1", "Описание 1", 100, 5)
    product2 = Product("Продукт 2", "Описание 2", 200, 10)

    assert str(category) == "Тест Category, количество продуктов: 0 шт."

    category.add_product(product1)
    assert str(category) == "Тест Category, количество продуктов: 5 шт."

    category.add_product(product2)
    assert str(category) == "Тест Category, количество продуктов: 15 шт."



def test_product_initialization(reset_totals):
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
    assert Product.total_products == 1


def test_set_price_negative_value(reset_totals):
    product = Product("Xiaomi 14 pro", "256GB, Серый цвет, 200MP камера", 50.0, 100)
    product.price = -10.0
    assert product.price == 50.0


def test_create_product_classmethod(reset_totals):
    product = Product.create_product("Test Product", "Test Description", 50.0, 10)
    assert isinstance(product, Product)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 50.0
    assert product.quantity == 10
    assert Product.total_products == 1


def test_add_method(reset_totals):
    product1 = Product("Продукт A", "Описание продукта A", 100, 10)
    product2 = Product("Продукт B", "Описание продукта B", 200, 2)
    assert (product1 + product2) == "Результат сложений: 1400"
