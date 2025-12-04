#Constructor overloading with default parameters

class Person:
    def __init__(self, address, name="vineetha", age = "20" ):
        self.name = name
        self.age = age
        self.address = address

p = Person("banaglore Hosur")
print(f"{p.name, p.age, p.address}")
p1 = Person("Hyderabad Kukatpally", "vinee", 3)
print(f"{p1.name, p1.age, p1.address}")


