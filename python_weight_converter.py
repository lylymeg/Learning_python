
weight= float(input("Enter your weight: "))
unit = input("Is this in (K)g or (L)bs? ")
if unit.upper() == "K":
    weight= weight * 2.205
    unit = "Lbs"
    print(f"Your weight is: {weight:.2f} {unit}")
elif unit.upper() == "L":
    weight= weight / 2.205
    unit = "Kg"
    print(f"Your weight is: {weight:.2f} {unit}")
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")