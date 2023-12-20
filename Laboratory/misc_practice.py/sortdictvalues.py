myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

# mkeys=sorted(list(myDict.keys()))
# sortedd={i:myDict[i] for i in mkeys}
# print(sortedd)
keyl=list(myDict.keys())
print(sorted(myDict.items(), key=lambda x:x[1]))