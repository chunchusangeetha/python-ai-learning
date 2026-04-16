name = "dgfdgfhgjh"
num = 1128397
def reverse_string(names):
    reverse = ""
    for char in names:
        reverse = char + reverse
    return reverse

print(reverse_string(name))
print(reverse_string("Sangeetha"))

def reverse_num(n):
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = (reverse *10)+digit
        n = n//10
    return reverse

print(reverse_num(num))
print(reverse_num(433454657))       
print(reverse_num(0)) 
