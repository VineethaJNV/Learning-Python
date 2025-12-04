from abc import ABC, abstractmethod

class Employee:
    @abstractmethod
    def calc_salary(self):
        pass
class Intern(Employee):
    def calc_salary(self):
        print(f"Only Stifund")

class FullTimeEmploee(Employee):
    def calc_salary(self):
        print(f"HRA+BASE+Relocation Bonus+ Joining Bonus+ Standard Benefits")
class ContractEmployee(Employee):
    def calc_salary(self):
        print(f"Only salary with few components")

fte = FullTimeEmploee()
fte.calc_salary()