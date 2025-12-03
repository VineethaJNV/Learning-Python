#Function Overriding(Inheritance)methods in child and basee class
#Duck Typing

class Employee():
    def get_designation(self):
        print("Designation is employee")

class Teacher(Employee):
    def get_designation(self):
        print("Designation is Teacher")

t1 = Teacher()
t1.get_designation()

