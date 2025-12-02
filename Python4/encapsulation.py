class BankAccount:
    def __init__(self, name, balance):
        self.name = name #public
        self.__balance = balance #private
        # _ signifies protected and __ signifies private
        #Python doesn't enforce data hiding but convention can still be followed
        #private attributes are not accessible outside of class in python due to Data Mangling
        #getters and setters can be used to access private attributes
    def get_balance(self):
        return self.balance
    def set_balance(self, new_balance):
        self.__balance = new_balance

#no true protected or no true private attribute in python
account = BankAccount("Vineetha", 10_000)
#OOPS is less about syntax and more about implemmetation
print(f"Account holders name is {account.name} and balance is {account.balance}")