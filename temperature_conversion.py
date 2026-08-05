

unit = input("Is this in (C)elsius or (F)ahrenheit? ")
temp = float(input("Enter the temperature: "))

if unit.upper() == "C":
    temp = round((temp * 9/5) + 32,1)
    unit = "Fahrenheit"
    print(f"The temperature is: {temp} {unit}")
elif unit.upper() == "F":
    temp = round((temp - 32) * 5/9,1)
    unit = "Celsius"
    print(f"The temperature is: {temp} {unit}")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")