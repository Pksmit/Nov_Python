val=[1,3,4,5,6,7]
emp_list = []
for x in val:
    if x%2==1:
        emp_list.append(x)
    else:
        pass
print(emp_list)
print(" ")
print(" ")

# Using List Comprehension!!
print("Using List Comprehension")
print([x for x in [1,3,4,5,6,7] if x%2==0])
print(" ")
print(" ")


print([f'{x} even number' if x%2==0 else f'{x} odd value' for x in [1,2,3,4,5,6,7,8,9,10]])