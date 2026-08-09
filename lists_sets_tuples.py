#collection = single "variable" used to multiple values
#list = [] ordered and changeable . duplicates OK
#set = {} unordered and immutable , but add/remove ok . no duplicates 
#tuple = () ordered and unchangeable . duplicates ok . faster 

fruits = ["apple" , "orange" , "banana", "coconut"]

#print(dir(fruits)) #print the methods that this list can perform 
# print(help(fruits))

print(len(fruits))
print ("apple" in fruits) #return a boolean if the elt exist or not in the list

for fruit in fruits:
    print(fruit)

print()
fruits[2]="pineapple"
fruits.append("watermelon")
fruits.remove("apple")
fruits.insert(0,"pineapple")
fruits.sort()
fruits.reverse()
#fruits.clear() # []
print(fruits.count("pineapple"))
print(fruits.index("orange"))
for fruit in fruits:
    print(fruit)

