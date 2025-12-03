class Employee:
    start_time = "9am"
    end_time = "6pm"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role


class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary


acc = Accountant(10000, "Developer")

print(acc.salary, acc.start_time, acc.end_time, acc.role)