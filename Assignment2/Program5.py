num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
print("First no is : ",num1)
print("Second no is : ",num2)
print("Third no is : ",num3)
if num1 > num2 and num1 > num3:
    print("Largest no is : ",num1)
elif num2 > num3:
    print("Largest no is : ",num2)
else:
    print("Largest no is : ",num3)