#input() = a function that prompts the user for input and returns it as a string. It can also take an optional argument, which is a string that will be displayed as a prompt to the user.

name = input("what is your name? ") # prompts the user for their name and returns it as a string
age = input("how old are you? ")


age =int(age)

#we can also do : age = int(input("how old are you? ")) # prompts the user for their age and converts it to an integer
age +=1

print("Hello, " + name + "!")
print("HAPPY BIRTHDAYYY QUEEN ")
print(f"You are {age} years old.")


#exercice 1  : Area of a rectangle 

width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))
area = width * height
print(f"The area of the rectangle is: {area}")