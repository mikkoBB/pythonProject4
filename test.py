import pytest
from main import Category
from main import Product
import os


@pytest.fixture
def category():
    '''
    Тестирование класса Категория
    '''
    return Category('name_1', 'text_1', 'list_product')

def test_category_init(category):
    '''
    Тестирование инициализации атрибутов класса
    '''
    assert category.title == 'name_1'
    assert category.description == 'text_1'
    assert category.list_product == [Product('a', 'x', 10.0, 2), Product('a1', 'x1', 10.2, 2)]
def test_category_count(category):
    '''
    Тестирование подсчетов уникальных товаров и количества категорий товаров
    '''
    assert Category.all_unique_prod_quantity == 22
    assert Category.all_category_quantity == 2

@pytest.fixture
def product():
    '''
    Тестирование класса Продукт
    '''
    return Product("a", "x", 10.0,2)

def test_product_init(product):
    '''
    Тестирование инициализации названий товаров, их описаний, цен и количества
    '''
    assert product.name == "a"
    assert product.description == "x"
    assert product.price == 10.0
    assert product.quantity == 2


def test_product(product):
    assert product.name == "a"
    assert product.description == "x"
    assert product.price == 10.0
    assert product.quantity == 2




