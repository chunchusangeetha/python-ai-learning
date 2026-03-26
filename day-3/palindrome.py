
def check_palindrome(n):
    original = n
    reverse = 0
    while n >0:
        digit = n % 10
        reverse = (reverse *10)+digit
        n = n//10
    if(original == reverse):
        print(f'{original} is palindrome')
    else:
       print(f'{original} is not palindrome') 
        
        

num = int(input("Enter a number: "))
check_palindrome(num)