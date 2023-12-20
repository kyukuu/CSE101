myDict = {'ravi': 10, 'rajnish': 9,
          'sanjeev': 15, 'yash': 2, 'suraj': 32}

keys = sorted(myDict.keys())
value = sorted(myDict.values())

for i in sorted(myDict.keys()):
    print((i, myDict[i]))

for i in value:
    print(keys[value.index(i)])


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict1.update(dict2)
print(dict1)

