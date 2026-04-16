

def max_num(num1,num2,num3):
   if (num1 >= num2) and (num1 >= num3):
        return num1
   elif (num2 >= num1) and (num2 >= num3):
       return num2   
   else:
        return num3

num1 = int(input("Eneter a number: "))
num2 = int(input("Eneter a number: "))
num3 = int(input("Eneter a number: "))

print(max_num(num1,num2,num3))