year = int(input("Enter any year : "))
if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0): 
    print("This year ",year," is a LEAP YEAR.")  
else:
    print("This year ",year," is not a LEAP YEAR.")