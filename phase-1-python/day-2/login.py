correct_username = "admin"
correct_password = "1234"

username = input("Enetr username: ")
password = input("Enter password: ")

if (username == correct_username  and password == correct_password):
    print("Login success")
else:
    print("Invalid credentials")    