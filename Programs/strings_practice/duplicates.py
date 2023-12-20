str = input()
lst = []
for i in str:
    if i not in lst:
        lst.append(i)

print("".join(lst))
