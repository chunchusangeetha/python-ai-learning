# CalCulator

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

operation = input("enter a operation which is (+,-,*,/): ")

if operation == '+':
    print(f"Addition of {a},{b} is " ,a+b)
elif operation == '-':
    print(f"subtraction of  of {a},{b} is " ,a-b)
elif operation == '*':
    print(f"multiplication of {a},{b} is " ,a*b)
elif operation == '/':
    print(f"division  of {a},{b} is " ,a/b)  
else :
    print("invalid operation")      