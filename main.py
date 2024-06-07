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
        self.__price = float(price)
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity}.'

    def __add__(self, other):
        if self.__class__ == type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError('Нельзя складывать продукты разных типов')

    @classmethod
    def creating_product(cls, product_data: dict):
        return cls(**product_data)

    def adding_product(self, list_of_product):
        for prod in list_of_product:
            if prod.name == self.name:
                prod.quantity += self.quantity
                if self.__price > prod.__price:
                    prod.__price == self.__price
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена введена некорректно')
        else:
            self.__price = new_price
class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,performance: float, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color
class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 manufacturer_country: str, germination_period: str, color: str):
        super().__init__(self, title, description, price, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color


p1 = Product('a', 'x', 10.0, 2)
p2 = Product('a1', 'x1', 10.4, 6)
p3 = Product('a2', 'x2', 14.0, 5)
list_products = [p1, p2, p3]


class Category:
    '''
    Класс, описывающий категорию товаров, описание названий категорий, свойств и список товаров
    '''
    title: str
    description: str
    list_products: list
    all_category_quantity = 0
    all_unique_prod_quantity = 0
    all_category_quantity += 1
    all_unique_prod_quantity += len(set(list_products))

    def __init__(self, title, description, list_products):
        '''
        Метод инициализации атрибутов класса
        '''
        self.title = title
        self.description = description
        self.__list_products = list_products

    def __len__(self):
        count_product = 0
        for product in self.__list_products:
            count_product += product.quantity
            return count_product

    def __str__(self):
        return f'{self.title}, количество продуктов: {len(self)} шт.'

    def adding_product(self, new_product):
        if new_product.quantity == 0:
            raise ValueError('Нельзя складывать товары с нулевым количеством!')
        elif isinstance(new_product, Product):
            self.__list_products.append(new_product)
            all_unique_prod_quantity += 1
        else:
            raise TypeError('Нельзя к продукту добавлять лишние объекты')

    @property
    def getting_list_of_product(self):
        updated_product = ''
        for product in self.__list_products:
            updated_product += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.'
        return updated_product

    @property
    def list_products(self):
        return self.__list_products

    def average(self):
        getting_sum = 0
        try:
            for product in self.__list_products:
                getting_sum += product.price
            result = getting_sum / len(self.__list_products)
            return result
        except ZeroDivisionError:
            return 0