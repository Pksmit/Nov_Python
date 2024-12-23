# Indexing:
val = "rama"
print(val[0])
print(val[1])
print(val[2])
print(val[3])

# Slicing :

# Start : Stop
val2 = '''prashant'''
print(val2[4:7])
print(val2[-7:-1])

# Start : Stop : Step
val2 = '''prashant'''
print(val2[::1])
print(val2[::-1])

# palindrome
val3 = 'nitin'
print(val3[::1])
print(val3[::-1])
if val3[::1] == val3[::-1]:
    print(val3," is Palindrome")
else:
    print(val3," is Not a Palindrome")