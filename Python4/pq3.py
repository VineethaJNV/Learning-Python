class Student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks
    
    def get_name(self):
        return self.__name

    def get_roll_no(self):
        return self.__roll_no
    
    def get_marks(self):
        return self.__marks
    
    def set_marks(self, new_marks):
        if(new_marks < 0):
            print(f"Marks can't be negative")
        self.__marks = new_marks
    
    def set_name(self, new_name):
        if(new_name == " "):
            print(f"name can't be empty!")
        self.__name = new_name

    def set_roll_no(self, new_roll_no):
        if(new_roll_no > 100 and new_roll_no <1):
            print(f"Invalid roll no!")
        self.__roll_no = new_roll_no

    def print_details(self):
        print(self.__name, self.__roll_no, self.__marks)

s = Student("vineetha", 37, 100)
print(f'{s.get_name()}')
s.set_name("varshitha")
print(f'{s.get_name()}')
print(f"{s.get_roll_no}")
s.set_roll_no(40)
print(f"{s.get_roll_no}")
s.print_details()

s.set_marks(90)
s.print_details()
