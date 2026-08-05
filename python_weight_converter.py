
weight= float(input("Enter your weight: "))
unit = input("Is this in (K)g or (L)bs? ")
if unit == "K":
    weight= weight * 2.205
    unit = "Lbs"
elif unit == "L":
    weight= weight / 2.205
    unit = "Kg"
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")
    exit()

print(f"Your weight is: {weight:.2f} {unit}")