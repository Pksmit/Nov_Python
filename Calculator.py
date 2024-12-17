f_no = float(input("Enter First no"))
s_no = float(input("Enter second no"))
operator = input("Operation(+,-,*,/):")
if operator == "+":
    res = f_no + s_no
elif operator == "-": 
    res = f_no - s_no
elif operator == "*":
    res = f_no * s_no
elif operator == "/":
    res = f_no / s_no
else:
    res = "Invalid operation!!"
print("output is" ,res)