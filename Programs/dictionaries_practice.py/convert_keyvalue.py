test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
keys = []
values = []
items = []
for i in test_dict.keys():
    keys.append(i)
for i in test_dict.values():
    values.append(i)
for i in test_dict.items():
    items.append(list(i))
print(keys)
print(values)
print(items)

# method1
res = []
for key, val in test_dict.items():
    res.append([key] + val)
print(res)

# method2
lst = [[key] + val for key, val in test_dict.items()]
