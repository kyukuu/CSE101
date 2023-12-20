s = input().split()
res = []
for i in s:
    last = int(len(i))-1
    x = i[0].upper() + i[1:-1] + i[-1].upper()
    res.append(x)
print(res)
