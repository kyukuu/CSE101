with open("tut_8\input4.txt") as f:
    with open("tut_8\output4.txt", "w") as f2:
        data = f.readlines()

        for i in data:
            i = i.split()
            marks = i[1:]
            marks = [int(x) for x in marks]
            if sum(marks)/len(marks) >= 80:
                ans = " ".join(i)+"\n"
                f2.write(ans)
