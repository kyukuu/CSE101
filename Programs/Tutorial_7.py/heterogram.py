str = input()
lst = []
for i in str:
    if i not in lst:
        lst.append(i)

if len(lst) == len(str):
    print("Heterogram")
else:
    print("Not a Heterogram")
