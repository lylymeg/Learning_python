#module = a file containing code you want to include in your program 
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files 



#import math 
#import math as m 
#from math import e 
import examplemod
"""a,b,c,d,e = 1,2,3,4,5

print(e ** a) #the e from math will be replace by the e=5 
print(e ** b)
print(e ** c)
print(math.e ** d)  #we should write math.e to refer to the e from math
print(e ** e)
"""

result = examplemod.pi
result = examplemod.square(3)
result = examplemod.cube(3)
result = examplemod.circumference(3)
result = examplemod.area(3)

print(result)