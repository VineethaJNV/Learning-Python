class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, value):
        self.balance = self.balance+value

    def withdraw(self, withdraw):
        self.balance = self.balance-withdraw

    def check_balance(self):
        print(f"the balance in your account is {self.balance}")

account = BankAccount("abc123", "vineetha", 10_000)
account.check_balance()

account.deposit(1000)
account.check_balance()

account.withdraw(2000)
account.check_balance()
    