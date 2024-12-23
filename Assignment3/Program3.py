age = int(input("Enter the age of the person : "))
if age in range(0,13):
    print("Person is a CHILD")
elif age in range(13,20):
     print("Person is a TEENAGER")
elif age in range(20,65):
    print("Person is an ADULT")
elif age in range(65,120):
    print("Person is a SENIOR")
else:
    print("INVALID AGE !!!!")