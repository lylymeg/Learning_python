#List comprehension = A concise way to create lists in python 
# Compact and easier to read than traditional loops
# [expression for value in iterable if condition]


doubles=[]

for x in range (1,11):
  doubles.append(x*2)

print(doubles)



doubles =[x*2 for x in range(1,11)]
triples = [x*3 for x in range(1,11)]
squares = [x*x for x in range(1,11)]


print(doubles)
print(triples)
print(squares)


fruits = ["apple","orange","banana","coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)


fruits = ["apple","orange","banana","coconut"]
fruits = [fruit[0]for fruit in fruits]
print(fruits)


numbers = [1,-2,3,-4,5,-6,8,-7]

positive_nums=[num for num in numbers if num>=0]
negative_nums=[num for num in numbers if num<0]
even_nums=[num for num in numbers if num % 2 == 0]
odd_nums=[num for num in numbers if num % 2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)
