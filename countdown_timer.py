import time 


my_time = int(input("Enter the time in seconds for the countdown timer: "))


for x in reversed(range(0,my_time)):
    print(x)
    time.sleep(1) # pause the program for 1 second


print("TIME's UP!")

#METHOD2 

for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1) # pause the program for 1 second

print("TIME's UP!")