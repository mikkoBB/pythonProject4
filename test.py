import pytest
from main import Category, Product

@pytest.fixture
def category():
    return Category('name_1', 'text_1', [])

def test_category_init(category):
    assert category.title == 'name_1'
    assert category.description == 'text_1'
    assert category.products == []
def test_category_count(category):
    assert category.all_unique_prod_quantity == 1
    assert category.all_category_quantity == 1
@pytest.fixture
def product():
    return Product("a", "x", 10.0,2)

def test_product_init(product):
    assert product.name == "a"
    assert product.description == "x"
    assert product.price == 10.0
    assert product.quantity == 2


def test_product(product):
    assert product.name == "a"
    assert product.description == "x"
    assert product.price == 10.0
    assert product.quantity == 2




