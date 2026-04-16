def atm():
    balance = 10000

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
            print(f"Your account balance is {balance}")

        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Enter a valid amount")
            elif amount <= balance:
                balance -= amount
                print("Amount withdrawn successfully")
                print(f"Updated balance: {balance}")
            else:
                print("Insufficient balance")

        elif choice == 3:
            amount = int(input("Enter amount to deposit: "))

            if amount <= 0:
                print("Enter a valid amount")
            else:
                balance += amount
                print(f"Amount deposited successfully")
                print(f"Updated balance: {balance}")

        elif choice == 4:
            print("Thank you for using our ATM. See you soon!")
            break

        else:
            print("Invalid choice, please try again")


atm()