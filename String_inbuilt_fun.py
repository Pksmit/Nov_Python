print("hello🤗".upper())

print('A','--->',ord('A'))
print('a','--->',ord('a'))


print(65,'--->',chr(65))
print(97,'--->',chr(97))

# Converting uppercase to lowercase
val = 'ABC'
for x in val:
    ord_val = ord(x)
    conv_chr = ord_val+32
    print(chr(conv_chr))
    
    # Converting  lowercase to uppercase 
val = 'abc'
for x in val:
    ord_val = ord(x)
    conv_chr = ord_val-32
    print(chr(conv_chr))