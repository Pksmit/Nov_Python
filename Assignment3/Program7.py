num1 = int(input("Enter value for num1 : "))
num2 = int(input("Enter value for num2 : "))
op = input("Choose operator '+','-','*','/' : ")
if op == "+" :
    print("Sum of the numbers :",num1+num2)
elif op == "-" :
    print("Substraction of the numbers :",num1-num2)
elif op == "*" :
    print("Multiplication of the numbers :",num1*num2)
elif op == "/" :
    print("Division of the numbers :",num1/num2)
else:
    print("Invalid!!!")