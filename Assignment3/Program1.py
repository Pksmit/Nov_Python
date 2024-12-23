temp = int(input("Enter temperature in celsius : "))
print("1. Celsius to Farenheit :")
print("2. Celsius to Kelvin :")
choice = int(input("Enter your choice : "))
if choice == 1 :
    print("Temperature in Farenheit :",(temp*1.8)+32,"F")
elif choice == 2:
    print("Temperature in Kelvin :",temp+273.15,"k")
else:
    print("Invalid choice!!!")