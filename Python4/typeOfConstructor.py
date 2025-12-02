class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa


stu1 = Student("Vineetha", 10)
stu2 = Student("Sailaja", 0.92)
stu3 = Student("Sushma", 10)

print(stu1.get_cgpa())
print(stu2.get_cgpa())
print(stu3.get_cgpa())