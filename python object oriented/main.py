from car import Car


#Object = a "bundle" of related attributes (variables) and methods(functions)
#ex phone,cup,book
#you need a "class" to create many objects


#class = (blueprint) used to design the structure and layout of an object 



car1= Car("BMW",2023,"black",False)
car2= Car("Mercedes",2022,"white",True)
car3= Car("Audi",2025,"grey",True)



print(car1.model)

car1.drive()

car2.describe()
car2.stop()
