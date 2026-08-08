# while loop = execute  some code while some condition is true

name = input("what is your name? ")
while name == "":
    print("You didn't enter your name. Please try again.")
    name = input("what is your name? ")
print(f"Hello, {name}!")


food =input("what is your favorite food? print q to quit ")
while not food == "q":
    print(f"You like {food}.")
    food =input("what other food do you like? print q to quit ")
print("You have exited the loop. Goodbye!")

num = int(input("Enter a number between 1 and 10: "))
while not num >= 1 or num > 10:
    print("Invalid input. Please enter a number between 1 and 10.")
    num = int(input("Enter a number between 1 and 10: "))
print(f"You entered the number {num}.")