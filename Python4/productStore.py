class Product:
    total_products_count = 0
    def __init__(self, name, price):
        Product.total_products_count+=1
        self.name = name
        self.price = price

    def print_info(self):
        print(f"Product's name is {self.name} and price is {self.price}")
    
    @staticmethod
    def calc_discount(price, discount):
        return price - price*(discount/100)

    @classmethod
    def get_product_count(cls):
        return  cls.total_products_count

p1 = Product("Lenovo Ideapad", 50000)
p2 = Product("Macbook", 70000)
p3 = Product("Moto Egde 50", 20000)

p2.print_info()
print(f"Total products are : {p3.get_product_count()}")
