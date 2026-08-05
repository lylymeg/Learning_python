import math



x= 3.14
y = -4
z = 5
r= 9
result = round(x) # 3
result = abs(y) # 4
result = pow(z, 2) # 25
max = max(x, y, z) # 5
min = min(x, y, z) # -4

print(max)
print(min)

print(result)

print (math.pi)
print (math.e)
print (math.sqrt(9)) # 3.0
print (math.ceil(3.14)) # 4 up 
print (math.floor(3.14)) # 3 down

#Exercice : circumference of a circle

radius = float(input("Enter the radius of the circle: "))
pi = math.pi
circumference= 2*pi*radius 
print(f"the circumference of the circle is: {round(circumference, 2)} cm")
print(f"the circumference of the circle is: {circumference:.2f} cm")

area = pi*pow(radius, 2)
print(f"the area of the circle is: {round(area, 2)} cm²")

#hypotenuse of a right triangle

a=float(input("enter the length of side a: "))
b=float(input("enter the length of side b: "))

#c=math.hypot(a, b)
c= math.sqrt(pow(a, 2) + pow(b, 2))


print(f"the length of the hypotenuse is: {round(c, 2)}")