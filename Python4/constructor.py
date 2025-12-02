class Student:
    def __init__(self, name, subject, age):
        print("Constructor is called and object is being constructed!!!")
        self.name = name
        self.subject = subject
        self.age = age
    
    def print_attributes(self):
        print(f"name is : {self.name}, subject is {self.subject}, age is {self.age}")

stu1 = Student("vineetha", "Learning python for Machine Learning", 20)
stu2 = Student("Veera Prakash", "Learning python engineering", 19)
stu1.print_attributes()

stu2.print_attributes()
