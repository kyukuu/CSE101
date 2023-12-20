with open("signatures.txt") as f:
    data = f.read()
    data = data.split("...")
    sumofsignsforpeople = []
    name = []
    for i in data:
        i = i.split(":")
        names = i[0].split()
        name.append(names)
        signs = i[1].split()

        sum_signs = 0
        for j in signs:
            j = j.split(",")
            sum_signs += int(j[1])
        sumofsignsforpeople.append(sum_signs)

    ok = []
    okname = []
    for i in range(len(sumofsignsforpeople)):
        if sumofsignsforpeople[i] == max(sumofsignsforpeople):
            ok.append(sumofsignsforpeople[i])
            okname.append(name[i])

    notok = []
    notokname = []
    for i in range(len(sumofsignsforpeople)):
        if sumofsignsforpeople[i] == min(sumofsignsforpeople):
            notok.append(sumofsignsforpeople[i])
            notokname.append(name[i])

    for i in range(len(ok)):
        print(f'{"max signs:"} {okname[i]} {ok[i]} sign(s)')
    for i in range(len(notok)):
        print(f'{"min signs:"} {notokname[i]} {notok[i]} sign(s)')
