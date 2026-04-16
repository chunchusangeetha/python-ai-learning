import math
def prime_check(num):
    if(num <= 1):
        return False
    else:
        for i in range(2,int(math.sqrt(num)) + 1):
            if(num % i == 0):
                 return False
            else:
                return True
  

#number = int(input("Enter a num: "))
print(prime_check(71))

def prime_numbers():
    for num in range(2,101):
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i == 0:
                 break
        else:    
            print(num, end=" ")

prime_numbers()

