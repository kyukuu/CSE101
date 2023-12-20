str = input()
count = 0
for i in str:
    if i.isdigit():
        count += 1
print("the frequency of numbers in the above string is:", count)
