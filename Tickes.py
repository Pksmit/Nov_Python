tickets = [1,2,3,4,5,6]
print("Available tickets",tickets)
use_input = int(input("Enter how many tickets u wanna buy : "))
for x in range(use_input):
     ticket_num = int(input("Enter ticket number : "))
     tickets.remove(ticket_num)
print("Available tickets",tickets)