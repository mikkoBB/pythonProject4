class Category:
    title: str
    description: str
    products: list
    all_category_quantity = 0
    all_unique_prod_quantity = 0

    def __init__(self, title, description, products):
        self.title = title
        self.description = description
        self.products = products
        self.all_category_quantity = 1

Category.all_unique_prod_quantity += 1



class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity




