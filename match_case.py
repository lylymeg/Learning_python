#Match-case statement (switch) : An alternative to using many elif statements
# execute some code if a value matches a case
#benefits: cleaner and syntax is more readable 



def day_of_week(day):
    match day:
        case 1 : 
            return "It's Sunday"
        case 2:
            return "It's Monday"
        case 3 : 
            return "It's Tuesday"
        case 4 : 
            return "It's Wednesday"
        case 5 : 
            return "It's Thursday"
        case 6 : 
             return "It's Friday"
        case 7 : 
            return "It's Saturday"
        case _ : 
            return "Not a valid day"

print(day_of_week("pizza"))