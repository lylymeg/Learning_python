



foods =[]
prices = []
total = 0

while True:
    food = input("enter a food to buy (q to quit) :  ")
    if food.lower() == "q":
        break
    else: 
        price=float(input(f"enter the price of a {food} : $"))
        foods.append(food)
        prices.append(price)
        total = total + price


print("------YOUR CART -----")

for food in foods :
    print(food,end=" ")

print(f"your total is: ${total}")