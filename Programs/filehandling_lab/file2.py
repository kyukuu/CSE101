with open("file2.txt") as f:
    data = f.read()
    data = data.lower()
    data = data.split()
    dict = {}
    for i in data:
        if i not in dict:
            dict[i] = 0
        dict[i] += 1

    value = list(dict.values())
    maxv = max(value)

    ans = [i for i in dict.keys() if dict[i] == maxv]
    for i in ans:
        print(i, dict[i])
    with open("worddictionary", 'w') as f2:
        for i in dict.items():

            f2.write(str(i))
