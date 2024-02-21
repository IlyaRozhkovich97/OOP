import pytest
from utils.main import Category, Product


@pytest.fixture
def reset_totals():
    Category.total_categories = 0
    Product.total_products = 0
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


def test_product_initialization(reset_totals):
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
    assert Product.total_products == 1


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
