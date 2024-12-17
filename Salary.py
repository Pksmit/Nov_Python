name = input("Enter name :")
exp = int(input(f"Enter experience year of {name}"))
if exp>=1:
    if exp>=1 and exp<=5:
        print("Salary is:",25000)
    elif exp>5 and exp<=10:
        print("Salary is:",50000)
    else:
        print("Salary is:",75000)
else:
    print("Not Allowed")
    
    