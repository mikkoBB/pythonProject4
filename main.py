class Category:
    '''
    Класс, описывающий категорию товаров, описание названий категорий, свойств и список товаров
    '''
    title: str
    description: str
    products: list
    all_category_quantity = 0
    all_unique_prod_quantity = 0

    def __init__(self, title, description, products):
        '''
        Метод инициализации атрибутов класса
        '''
        self.title = title
        self.description = description
        self.products = products
        self.all_category_quantity = 1

Category.all_unique_prod_quantity += 1



class Product:
    '''
    Класс, описывающий название товара, его описание, также цену и количество
    '''
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        '''
        Метод инициализации атрибутов класса Продукт
        '''
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity




