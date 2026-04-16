def numberCheck(num):
    if num % 2 == 0:
        evenOdd = "even"
    else:
        evenOdd = "odd"

    if num > 0:
        sign = "positive"
    elif num < 0:
        sign = "negative"
    else:
        sign = "zero"

    return f"{num} is {evenOdd} and {sign}"


number = int(input("Enter a number: "))
print(numberCheck(number))