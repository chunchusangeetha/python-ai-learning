name = "sangeetha"

def count_chars(val):
    count = 0
    for char in val:
        count += 1
    return count
    
print(count_chars(name))

def count_digit_num(n):
    count = 0
    while n > 0:
        n = n//10
        count += 1
    return count

print(count_digit_num(12564565734))
