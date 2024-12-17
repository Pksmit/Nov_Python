cost = 82
age = float(input("Enter age of the person"))
if age>=18 and age<=30:
    print("the cost of the ticket is ",5*cost)
elif age>30 and age<=50:
    print("the cost of the ticket is ",30*cost) 
elif age>50:
    print("The ticket is FREE of cost ") 
else:
    print("Invalid age")