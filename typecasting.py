#typecasting is the process of converting a variable from one data type to another. In Python, there are several built-in functions that can be used for typecasting, such as int(), float(), str(), and bool().

name ="lydia"
gpa = 3.5
age =23


print(type(name)) # <class 'str'>
gpa =int(gpa) # convert float to integer
print(type(gpa)) # <class 'int'> 
print(gpa) # 3

age=str(age) # convert integer to string
print(type(age)) # <class 'str'>
print(age) # "23"


#age+= 1 # error; can only concatenate str (not "int") to str

age+="1"
print(age) # "231" because age is now a string, so it concatenates "


name = bool(name) # convert string to boolean
print(type(name)) # <class 'bool'>
print(name) # True

nickname=""
nickname=bool(nickname) # convert empty string to boolean
print(nickname) # False