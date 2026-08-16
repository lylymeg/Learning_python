#function = a block of reusable code 


def happybirthday(name,age):   #the position of the parameters matters
    print(f"happy birthday {name}")
    print(f"you are {age} yo")
    print("happy birthday to you")
    print()


happybirthday("lydia",22)
happybirthday("carlos",30)
happybirthday("francissco",35)


#return = statement used to end a function and send a result back to the caller

def add(x,y):
    z = x+y
    return z


def substract(x,y):
    z = x-y
    return z


def multiply(x,y):
    z = x*y
    return z

def divide(x,y):
    z = x/y
    return z

print(add(1,2))
print(substract(1,2))
print(multiply(1,2))
print(divide(1,2))



def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("bro","code")


print(full_name)
