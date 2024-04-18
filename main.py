class Product:
    '''
    Класс, описывающий название товара, его описание, также цену и количество
    '''
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name, description, price,quantity):
        '''
        Метод инициализации атрибутов класса Продукт
        '''
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity
p1 = Product('a', 'x', 10.0, 2)
p2 = Product('a1', 'x1', 10.4, 6)
list_products = [p1, p2]


class Category:
    '''
    Класс, описывающий категорию товаров, описание названий категорий, свойств и список товаров
    '''
    title: str
    description: str
    products: list
    all_category_quantity = 0
    all_unique_prod_quantity = 0
    all_category_quantity += 1
    all_unique_prod_quanti += len(set(list_products))

    def __init__(self, title, description, list_products):
        '''
        Метод инициализации атрибутов класса
        '''
        self.title = title
        self.description = description
        self.list_products = list_products



