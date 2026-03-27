
def cal_sum(a,b):
    return a+b

def cal_sub(a,b):
    return a-b

def cal_mul(a,b):
    return a*b

def cal_div(a,b):
    if b == 0:
        return "Error! Division by zero."
    return a/b

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

choice_operation = input("enter your operation{+,-,*,/}: ")

if choice_operation == '+':
     print(f"Result: {cal_sum(num1, num2)}")
elif choice_operation == '-':
     print(f"Result: {cal_sub(num1, num2)}")
elif choice_operation == '*':
     print(f"Result: {cal_mul(num1, num2)}")
elif choice_operation == '/':
     print(f"Result: {cal_div(num1, num2)}")               
else:
    print("Invalid Input")     