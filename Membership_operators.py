#Membership operators = used to test whether a value or variable is found in a sequence 
# (string,list,tuple,set,or dictionary)
# 1.in
# 2.not in 


word ="APPLE"

letter= input("Guess a letter in the secret word : ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} is not found")



grades={"Spongebob":"A","Patrick":"B","Sandy":"C"}

student = input("Enter the name of a student : ")


if student not in grades : 
    print(f"{student} is not found")
else:
    print(f"{student}'s grade is {grades[student]}")



email = "Brocode@gmail.com"

if "@" in email and "." in email :
    print("Valid Email")
else:
    print("Invalid Email")