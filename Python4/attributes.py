#class Attributes

#Instance Attributes

class Student:
    college = "RGUKT"
    PI = 3.1
    def __init__(self, name, subject, cgpa):
        self.name = name
        self.subject = subject
        self.cgpa = cgpa
        self.PI = 3.14

stu1 = Student("Vineetha", "Python", 9.5)
print(f"The student name is {stu1.name}, Subject is {stu1.subject}, cgpa is {stu1.cgpa}")
print(stu1.college)#class attribute
print(Student.college)#class attribute


print(stu1.PI)
#Instance attributes have higher priority, as it will have unique values 
#we can use instance to access class attributes as well

