#for loops = execute a block of code for a fixed number of times
# you can iterate over a range ,string ,sequence,etc

for x in reversed(range(1,11)): # reversed() = reverses the order of a sequence
    print(x) # prints numbers from 1 to 10
print ("happy new year") # prints happy new year after the loop is done


for counter in range(1,11,2): # range(start,stop,step) = generates a sequence of numbers from start to stop (exclusive) with a step value
    print(counter) # prints odd numbers from 1 to 10


credit_card_number = "1234-5678-9012-3456"

for digit in credit_card_number: # iterating over a string
    if digit == "-": # skipping the hyphens in the credit card number
        continue
    print(digit) # prints each digit of the credit card number on a new line


   # break # breaks the loop after the first iteration, so only the first digit is printed