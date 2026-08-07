#conditional expression = A one-line shortcut for an if-else statement. It is also known as a ternary operator. 
# It allows you to evaluate a condition and return one value if the condition is true, 
# and another value if the condition is false.

# X if condition else Y


num = 5

a=6
b=7
age=25

user_role = "admin"

print("positive" if num>0 else "negative") # positive

result = "even" if num%2==0 else "odd"
print(result) # odd

max_num = a if a>b else b
print(max_num) # 7
min_num = a if a<b else b
print(min_num) # 6

print("Full access granted" if user_role=="admin" else "Access denied") # Full access granted



