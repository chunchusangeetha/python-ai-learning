def factorial(n):
   result = 1
   if(n < 0):
    return "Factorial is not defined for negative numbers."
   else: 
       for i in range(1,n+1):
        result *=i 
   return result

num = int(input("Enter a num: "))
print(factorial(num))