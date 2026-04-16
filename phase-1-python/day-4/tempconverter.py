def temp_converter(value,unit):
    unit = unit.upper()
    if unit == "C":
        result = (value * 9/5) + 32
        return f"{value}°C is {result:.2f}°F"
    elif unit == "F":
        result = (value - 32) * 5/9
        return f"{value}°F is {result:.2f}°C"
    else:
        return "Invalid Unit! Use 'C' for Celsius or 'F' for Fahrenheit."

value = int(input("Enter temp: "))
unit = input("Is this in (C)elsius or (F)ahrenheit? ").strip()

print(temp_converter(value,unit)) 
