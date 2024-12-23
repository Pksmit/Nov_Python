year = int(input("Enter any year : "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("This year is  LEAP YEAR ")
else :
    print("This year is NOT a LEAP YEAR")