#first parameter in instance method is self, can access class attributes
#first parameter in class method is cls
#the things that belong to the class, they also belong to objects by default
#Static methods are created when we neither use instance attributes nor we use classs attributes
#Static methods are stand alone functions
class MobilePhone:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
    
    def print_info(self):
        print(f"mobile phones RAM is {self.RAM} and storage is {self.storage} and type is {self.storage_type}")


    @classmethod
    def get_storage_type(cls):
        print(f"Storage type is {cls.storage_type}")

    @staticmethod
    def get_price_after_discount(price, discount):
        return price - price*(discount/100)

mp = MobilePhone("16GB", "512GB")
mp.print_info()
MobilePhone.get_storage_type()
print(f"Price after discount : {mp.get_price_after_discount(20_000, 10)}")
