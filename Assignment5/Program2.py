names = input("Enter names separated by spaces: ").split()
search_name = input("Enter the name to search: ")
found = False  # Flag to check if name is found
for name in names:
    if name == search_name:
        print("Name found")
        found = True
        break

if not found:
    print("Name not found.")
