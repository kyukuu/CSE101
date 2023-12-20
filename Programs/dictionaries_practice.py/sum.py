lst = []
dict = {'a': 100, 'b': 200, 'c': 300}

for i in dict.values():
    lst.append(i)
print(sum(lst))

# approach 2
sum = 0
for i in dict:
    sum += dict[i]
print(sum)
