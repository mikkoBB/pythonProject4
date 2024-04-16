class Category:
    '''
    Класс, описывающий категорию товаров, описание названий категорий, свойств и список товаров
    '''
    title: str
    description: str
    list_product: list
    all_category_quantity = 0
    all_unique_prod_quantity = 0

    def __init__(self, title, description, list_product):
        '''
        Метод инициализации атрибутов класса
        '''
        self.title = title
        self.description = description
        self.list_product = list_product
        Category.all_category_quantity += 1
        Category.all_unique_prod_quantity += len(set(list_product))
        list_product = [Product("a", "x", 10.0, 2), Product("a1", "x1", 10.2, 2)]




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





