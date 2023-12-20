with open("tut_8\input.txt") as f:
    data = f.readlines()
    with open("tut_8\output.txt", "w") as f2:
        for i in data:
            f2.write(i)
