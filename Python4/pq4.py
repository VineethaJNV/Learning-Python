class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self, radius):
        return (3.14*radius*radius)

class Rectancle(Shape):
    def area(self, length, breadth):
        return length*breadth

class Traingle(Shape):
    def area(self, base, height):
        return (0.5*base*height)

t = Traingle()
print(f"{t.area(10, 6)}")

r = Rectancle()
print(f"{r.area(10, 6)}")

c = Circle()
print(f"{c.area(4)}")
