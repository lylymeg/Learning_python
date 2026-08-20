#Inheritance = Allows a class to inherit attributes and methos from another class 
# helps with code reusablity and extensibility 
# class Child(Parent)


class Animal:
    def __init__(self,name):
     self.name = name
     self.is_alive = True



    def eat(self):
      print(f"{self.name} is eating")

   
    def sleep(self):
     print(f"{self.name} is sleeping")



class Dog(Animal):
   def speak(self):
      print("Woof!")


class Cat(Animal):
   def speak(self):
      print("Meoow!")

class Mouse(Animal):
   def speak(self):
      print("Squeek!")


dog = Dog("Fox")
cat = Cat("Felix")
mouse = Mouse("Jerry")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

cat.speak()
cat.eat()
