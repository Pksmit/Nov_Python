val = int(input("Enter grade value : "))
if val in range(90,101):
    print("Grade is A ")
elif val in range(80,90):
    print("Grade is B ")
elif val in range(70,80):
    print("Grade is C ")
elif val in range(60,70):
    print("Grade is D ")
elif val in range(0,61):
    print("Grade is F ")
else:
    print("Invalid Grade !!!")