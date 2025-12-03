class Employee:
    start_time = "10Am"
    end_time = "6pm"

    def change_time(self, new_time):
        self.end_time = new_time

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

t1 = Teacher("Python")
t1.change_time("4pm")
print(t1.subject, t1.start_time, t1.end_time)
