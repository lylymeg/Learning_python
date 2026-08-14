#dictionary = a collection pf {key:value} pairs
# ordered and changeable . no duplicates 


capitals = {"USA" : "Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}


#print(dir(capitals))
#print(help(capitals))
print(capitals.get("USA")) 


if capitals.get("Japan"):
    print("That capital exists")
else:
    print("the capital doesnt exist")


    capitals.update({"Germany":"Berlin"})
    capitals.update({"USA":"Detroit"})
    capitals.pop("China")
    capitals.popitem() #remove the last elt 
    #capitals.clear() #clear the dictionary
    print(capitals)

    keys = capitals.keys()

    for key in capitals.keys():
        print(key)


values = capitals.values()
for value in values:
    print(value)


items = capitals.items()
print(items) #dict_items([('USA', 'Detroit'), ('India', 'New Delhi'), ('Russia', 'Moscow')])


for key,value in capitals.items():
    print(f"{key}: {value}")