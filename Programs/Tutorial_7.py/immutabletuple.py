x = int(input())
lst = []
for i in range(x):
    ans = int(input())
    lst.append(ans)
print(lst)

del lst[4]
lst.append(5)

print(tuple(lst))
