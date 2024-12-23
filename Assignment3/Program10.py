val = input("Enter Password: ")
length = len(val)
has_upper = False
has_lower = False
has_digit = False
has_special = False
for char in val:
    if 'A' <= char <= 'Z': 
        has_upper = True
    elif 'a' <= char <= 'z': 
        has_lower = True
    elif '0' <= char <= '9': 
        has_digit = True
    else: 
        has_special = True
if length >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong")
elif length >= 6 and has_digit and (has_upper or has_lower):
    print("Moderate")
else:
    print("Weak")
