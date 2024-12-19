u_name = "admin"
p_word = "pass123"
username = input("Enter username : ")
password = input("Enter password : ")
if u_name == username and p_word == password:
    print("Access Granted")
else:
    print("Access Denied")
