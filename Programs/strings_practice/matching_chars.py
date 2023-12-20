str1 = input()
str2 = input()
s = []
for i in str1:
    if i in str2:
        if i not in s:
            s.append(i)

print(s)
print(len(s))
