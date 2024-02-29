import pytest
from utils.inherited_class import Smartphone, LawnGrass


@pytest.fixture
def smartphone_instance():
    return Smartphone("Смартфон", "Мощный смартфон", 1000, 10, "Apple", "iPhone 12", "256 ГБ", "Чёрный")


@pytest.fixture
def lawn_grass_instance():
    return LawnGrass("Трава", "Смесь для газонов", 50, 100, "Россия", "30 дней", "Зелёный")


def test_smartphone_instance_creation(smartphone_instance):
    assert isinstance(smartphone_instance, Smartphone)


def test_smartphone_attributes(smartphone_instance):
    assert smartphone_instance.name == "Смартфон"
    assert smartphone_instance.description == "Мощный смартфон"
    assert smartphone_instance.price == 1000
    assert smartphone_instance.quantity == 10
    assert smartphone_instance.performance == "Apple"
    assert smartphone_instance.model == "iPhone 12"
    assert smartphone_instance.storage_capacity == "256 ГБ"
    assert smartphone_instance.color == "Чёрный"


def test_lawn_grass_instance_creation(lawn_grass_instance):
    assert isinstance(lawn_grass_instance, LawnGrass)


def test_lawn_grass_attributes(lawn_grass_instance):
    assert lawn_grass_instance.name == "Трава"
    assert lawn_grass_instance.description == "Смесь для газонов"
    assert lawn_grass_instance.price == 50
    assert lawn_grass_instance.quantity == 100
    assert lawn_grass_instance.country_of_origin == "Россия"
    assert lawn_grass_instance.germination_period == "30 дней"
    assert lawn_grass_instance.color == "Зелёный"
