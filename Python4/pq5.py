#Inheritance

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, seats, brand, model):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, engine, brand, model):
        super().__init__(brand, model)
        self.engine = engine

c = Car(4, "Mahindra", 850)
print(f"{c.seats, c.brand, c.model}")

b = Bike("temp_engine", "Maruhti", 800)
print(f"{b.engine, b.brand, b.model}")


