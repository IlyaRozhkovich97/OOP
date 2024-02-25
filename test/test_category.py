import pytest
from utils.category import Category
from utils.product import Product


@pytest.fixture
def reset_totals():
    Category.total_categories = 0
    Category.total_unique_products = 0


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
