with open("tut_8\input2.txt") as f:
    data = f.read()
    count = 0
    for i in data:
        if i.isalpha():
            if i.isupper():
                count += 1
    print(count)
