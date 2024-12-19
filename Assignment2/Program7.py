age = int(input("Enter age of the user : "))
if age >= 0 and age <= 12:
    print("User is a : CHILD ")
elif age >= 13 and age <= 19:
    print("User is a : TEENAGER ")
elif age >= 20 and age <= 64:
    print("User is an : ADULT ")
else: 
    print("User is a : SENIOR ")