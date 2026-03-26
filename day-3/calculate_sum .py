num = int(input("Enter a num: "))


def calculate_sum (n):
   initial_sum = 0
   for i in range(1,n+1):
      initial_sum +=i 
   return initial_sum


print(calculate_sum (num))



