test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

res = dict()

for sub in test_list:
    res[tuple(sub[:2])] = list(sub[2:])
# dictionary keys are immutable thus lists or sets cant be dictionary keys
# however the values can be tuples or lists
print(res)
