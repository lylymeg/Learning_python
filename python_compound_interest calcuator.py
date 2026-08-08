
principle = 0 
rate = 0
time = 0


while principle <=0:
    principle = float(input("Enter the principle amount: "))
    if principle <=0:
        print("Principle amount must be greater than 0")

while rate <=0:
    rate = float(input("Enter the rate of interest: "))
    if rate <=0:
        print("Rate of interest must be greater than 0")

while time <=0:
    time = int(input("Enter the time period: "))
    if time <=0:
        print("Time period must be greater than 0")

total = principle * (1 + (rate/100)) ** time
print(f"The total amount after {time} years is: ${total:.2f}")