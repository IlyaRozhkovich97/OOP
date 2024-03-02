import pytest
from utils.product import Product


@pytest.fixture
def reset_totals():
    Product.total_products = 0


def test_product_initialization(reset_totals):
    product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5
    assert Product.total_products == 1


def test_set_price_negative_value():
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


def test_add_method():
    product1 = Product("Продукт A", "Описание продукта A", 100, 10)
    product2 = Product("Продукт B", "Описание продукта B", 200, 2)
    assert (product1 + product2) == 1400
