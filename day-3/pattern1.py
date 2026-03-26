def star_pattern(num):
    for i in range(1,num+1):
        print("*"*i)

star_pattern(5)

def star_pattern_rev(num):
    for i in range(1,num+1):
        print((num - i) * " " + i*"*")

star_pattern_rev(5)