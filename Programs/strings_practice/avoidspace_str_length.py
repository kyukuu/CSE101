x = input()

lst = [i for i in x if i != " "]
for i in lst:
    print(i, end="")
print()

# approach 2
res = sum(not chr.isspace() for chr in x)
print(res)

# approach 3

res2 = sum(map(len, x.split()))
print(res2)

# approach 4

str = x.replace(" ", "")
print(len(str))
