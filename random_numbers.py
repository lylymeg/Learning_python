import random

#print(help(random))



low =1
high = 100
num= random.randint(low,high)
options = ("rock","paper","scissors")
cards = ["2","3","1","J","Q","A"]

# num = random.random() : it generates a random number beetween 0 and 1

choice = random.choice(options)
print(num)
print(choice)
random.shuffle(cards) #melanger 
print(cards)