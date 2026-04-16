import math

def is_prime(num):
    if num < 2: 
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False 
    return True  

print("Prime numbers from 1 to 100:")
for n in range(1, 101):
    if is_prime(n):
        print(n, end=" ")

print(is_prime(67))