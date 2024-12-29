count = 0
for i in range(1,30):
    if i % 3 == 0:
        count += 1
        print(i)
        if count == 5:
            print("First 5 numbers divisible by 3 are as follows.")
            break
        