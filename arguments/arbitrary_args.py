# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
# *unpacking operator 
# arbitrary 


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3))


#*kwargs


def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")


print_address(street="123 Fake St.",
              city="Detroit",
              state="MI",
              zip="54321")



def shipping_label(*args, **kwargs):
    for arg in args :
        print(arg, end=" ")
    print()

    if "apt" in kwargs :
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
         print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}" )

shipping_label("Dr.","spongebob","Squarepants",
               street="123 Fake street",
               city="Detroit",
               state="MI",
               zip="54321")


         
      
           