test_dict = {'month': [1, 2, 3],
             'name': ['Jan', 'Feb', 'March']}

list = list(test_dict.values())
print(list)
s0 = list[0]
s2 = list[1]

dict = {}

for i in range(len(s0)):
    dict[s0[i]] = s2[i]
print(dict)
# for i in range()
