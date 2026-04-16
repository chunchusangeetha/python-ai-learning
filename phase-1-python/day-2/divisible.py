num = int(input("Enter a number: "))

if (num % 5 == 0):
    divisible = "divisible by 5"
else:
    divisible = "not divisible by 5"   

if (num % 2 == 0) :
    evenorOdd = "even"
else:
    evenorOdd = "odd"  

print(f"given num is {evenorOdd} and it is {divisible}")             
     
  