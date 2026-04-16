from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

class MyBankATM(ATM):
    def __init__(self, balance):
        self._balance = balance 

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount  
            print(f"Withdrew {amount}. New Balance: {self._balance}")
        else:
            print("Insufficient funds.")

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New Balance: {self._balance}")

atm = MyBankATM(1000)
atm.deposit(500)
atm.withdraw(200)
