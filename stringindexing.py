#indexing = accessing elts of a sequence using [] (indexing operator)
# [start:end:step] = slicing operator

credit_card_number = "1234-5678-9012-3456"
print(credit_card_number[0]) # 1
print(credit_card_number[5]) # 5
print(credit_card_number[0:4]) # 1234 , the ending index is exclusive we dont include the 4th caracter here
print(credit_card_number[:9]) # 1234-5678 , if we dont specify the starting index it will start from the beginning of the string
print(credit_card_number[5:9]) # 5678 , if we specify both start and end indices, it will return the substring between them
print(credit_card_number[5:13:2]) # 57-0 , the step parameter specifies the increment between elements
print(credit_card_number[-1]) # 6 , negative indexing starts from the end of the string, -1 is the last character, -2 is the second last character and so on
print(credit_card_number[-4:-1]) # 345 , negative slicing works similarly to positive slicing
print(credit_card_number[::2]) # 13579-0246 , if we dont specify the start and end indices, it will return the entire string with the specified step

last_digits=credit_card_number[-4:] # 3456 , if we dont specify the end index, it will return the substring from the start index to the end of the string
print(f"XXXX-XXXX-XXXX-{last_digits}") # XXXX-XXXX-XXXX-3456 , we can use f-strings to format the output

credit_card_number=credit_card_number[::-1] # 6543-2109-8765-4321 , we can use slicing to reverse a string
print(credit_card_number) # 6543-2109-8765-4321