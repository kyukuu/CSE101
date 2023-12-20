x = input()
x = list(x)
dic = {}
for i in x:
    if i not in dic:
        dic[i] = 0
    dic[i] = dic[i] + 1
print(dic)
count = 0
for i in dic:
    if dic[i] == 1:
        count += 1

if count == len(x):
    print("Heterogram")
else:
    print("Not a heterogram")
