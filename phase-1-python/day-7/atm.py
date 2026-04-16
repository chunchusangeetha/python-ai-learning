class ATM:
    def __init__(self):
        self.balance = 10000

    def check_balance(self):
        print(f"Your account balance is {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
            print(f"Updated balance: {self.balance}")
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        if amount <= 0:
            print("Enter a valid amount")
        else:
            self.balance += amount
            print(f"Amount deposited successfully")
            print(f"Updated balance: {self.balance}")

    def menu(self):
        while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except:
                print("Invalid input! Please enter a number.")
                continue

            if choice == 1:
                self.check_balance()

            elif choice == 2:
                try:
                    amount = int(input("Enter amount to withdraw: "))
                    self.withdraw(amount)
                except:
                    print("Invalid input! Please enter a number.")

            elif choice == 3:
                try:
                    amount = int(input("Enter amount to deposit: "))
                    self.deposit(amount)
                except:
                    print("Invalid input! Please enter a number.")

            elif choice == 4:
                print("Thank you for using our ATM. See you soon!")
                break

            else:
                print("Invalid choice, please try again")

a1 = ATM()
a1.menu()                