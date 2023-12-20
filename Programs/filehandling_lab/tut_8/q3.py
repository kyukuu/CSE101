with open("tut_8\input3.txt") as f:
    with open("tut_8\output3.txt", "w") as f2:
        data = f.readlines()

        for i in data:
            i = i.replace("Hello", "Hi")
            f2.write(i)
