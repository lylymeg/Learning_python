from script1 import *

# we can execute the code within script1.py here if there is not main in script1


def favorite_drink(drink):
  print(f"Your favorite drink is {drink}")


def main():
    print("This is script2")
    favorite_food("sushi")
    favorite_drink("coffee")
    print("Goodbye")

if __name__ == '__main__':
  main()