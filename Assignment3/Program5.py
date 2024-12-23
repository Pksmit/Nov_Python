wt = float(input("Enter the weight of the person in killograms : "))
ht = float(input("Enter the height of the person meters: "))
bmi = wt/(ht*2)
print(bmi)
if bmi < 18.5 :
    print("The person is UnderWeight.")
elif 18.5 <= bmi < 24.9 :
    print("The person has Normal Weight.")
elif 25 <= bmi < 29.9 :
    print("The person is OverWeight.")
elif bmi >= 30:
    print("The person is Obese.")
else:
    print("Invalid!!!")