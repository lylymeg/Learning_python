
name=input("what is your name? ")
phone_num=input("what is your phone number? ")



length = len(name)
print(length)

position = name.find("i") #the first caracter will have the index of 0 , it returns the first occurence of the character in the string, if it is not found it will return -1
print(position)

result = name.rfind("i") #it returns the last occurence of the character in the string, if it is not found it will return -1
print(result)

result2=name.capitalize() #it will capitalize the first letter of the string
result3=name.upper() #it will convert the string to uppercase
result4=name.lower() #it will convert the string to lowercase
print(result2)
print(result3)
print(result4)

result6=phone_num.isdigit() #it will return True if the string is a digit, False otherwise
print(result6)

result5=name.isalpha() #it will return True if the string is alphabetic, False otherwise
print(result5)

count=phone_num.count("5") #it will return the number of occurrences of the character in the string
print(count)

result7=phone_num.replace("5", "-") #it will replace all occurrences of the character in the string with the new character
print(result7)

print(help(str)) #it will display the documentation of the string class and its methods

#exercise : validate user input 


username=input("please enter your username:")

if(len(username)>12):
    print("the username is too long, please enter a username with less than 12 characters")
elif(username.count(" ")>0):
    print("the username should not contain spaces, please enter a valid username")
elif(username.isalpha()==False):
    print("the username should only contain letters, please enter a valid username")
else:
    print(f"welcome {username}!")