with open("geeks2") as f:
    data = f.readlines()
    print(data)
    for line in data:
        print(line)
        word = line.split()
        print(word)
