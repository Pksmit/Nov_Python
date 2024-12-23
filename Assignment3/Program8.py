s1 = int(input('Enter first side of the triangle :'))
s2 = int(input('Enter second side of the triangle :'))
s3 = int(input('Enter third side of the triangle :'))
if s1 == s2 == s3:
    print("The triangle is an Equilateral Triangle.")
elif (s1 == s2 != s3) or (s1 == s3 != s2) or (s2 == s3 != s1):
    print("The triangle is an Isosceles Triangle.")
elif (s1 != s2 != s3) and (s1 != s3):
    print("The triangle is an Scalene Triangle.")
else:
    print("Invalid!!!")