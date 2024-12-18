count = 0
sum = 0
mul = 1
for x in range(1,10,2):
    print(x)
    count=count+1
    sum = sum+x
    mul = mul*x
print("Total odd num:",count)
print("Sum of odd num:",sum)
print("Mul of odd num:",mul)