#format specifiers= {value:flags} format a value based on what flags are inserted

#.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad to that many spaces
# :< = left justify 
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive numbers
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator 


price1= 49.993947
price2= -1000.99
price3=12.34
price4= 345127.89

print(f"price1={price1:.2f}") # price1=49.99
print(f"price2={price2:10}") # price2=   -1000.99

print(f"price3={price3:010}") # price3=000012.34

print(f"price4={price4:<10}") # price4=345127.89 , left
print(f"price4={price4:>10}") # price4=    345127.89 ,right 
print(f"price4={price4:^10}") # price4=  345127.89 ,center
print(f"price4={price4:+.3f}") # price4=+345127.89 , plus 
print(f"price4={price4:,}") #each thousand will be separated by a comma 345,127.89
print(f"price4={price4:=+15,.2f}") # price4=     +345,127.89 , sign to leftmost position, 15 spaces allocated, comma separator, 2 decimal places




