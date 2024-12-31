sets = {1,2,2}
print(sets)

lst = [1,2,3,4,1,2]
emp_list =[]
for x in lst:
    if x not in emp_list:
        emp_list.append(x)
print(emp_list)
        
        
lst = [1,2,3,4,1,2]
emp_list =[]
[emp_list.append(x) for x in lst if x not in emp_list]
print(emp_list)


lst = [1,2,3,4,1,2]
emp_list =[]
dup_list =[]
for x in lst:
    if x  in emp_list:
        dup_list.append(x)
    else:
        emp_list.append(x)
       
print(dup_list)
        