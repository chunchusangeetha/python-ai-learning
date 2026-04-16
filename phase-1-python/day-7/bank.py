class BankAccount:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        if amount > self.balance or amount <= 0:
            print("Invalid deposit amount!")
        else:
            print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance or amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")


a = BankAccount("John Doe", 1000)
a.check_balance()
a.deposit(500)
a.withdraw(200)
a.check_balance()