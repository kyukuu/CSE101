test_list = [{'Gfg': 123, 'best': 10}, {'Gfg': 51, 'best': 7}]
lst = []
for i in test_list:
    res = []
    for j in i:
        res.append([j]+[i[j]])
    lst.append(res)

print(lst)

test_list = [{'Nikhil': 17, 'Akash': 18, 'Akshat': 20},
             {'Nikhil': 21, 'Akash': 30, 'Akshat': 10},
             {'Nikhil': 31, 'Akash': 12, 'Akshat': 19}]

meow = []
for idx, sub in enumerate(test_list, start=0):
    if idx == 0:
        meow.append(list(sub.keys()))
        meow.append(list(sub.values()))
    else:
        meow.append(sub.values())
print(meow)
