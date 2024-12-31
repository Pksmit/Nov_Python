atom=[1,66,4,56,88,99]
atom.sort()
print(atom)
print('Lowest element of the list is :',atom[0])
print('Biggest element :',atom[0]+atom[-1])
print('Heighest element of the list is :',atom[-1])

# Another way!!
print(max(atom)+min(atom))