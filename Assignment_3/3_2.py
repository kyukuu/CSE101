with open("sorted_data.txt") as f:
    data = f.readlines()
    records = {}
    for line in data:
        line = line.split(", ")
        if line[0] not in records:
            records[line[0]] = [line[1:]]
        else:
            records[line[0]].append(line[1:])

n = input("Enter Choice: ")
if n == "1":
    name = input("Enter the Student Name: ")
    end=input("Enter current time: ")
    end=[int(i) for i in end.split(":")]
    with open("3_2_1_output.txt","w") as f:
        for i in records:
            if i == name:
                for j in records[i]:
                    
                    tu=(j[-1][:-1])
                    tu=[int(i) for i in tu.split(":")]
                    if tu[0]>end[0]:
                        break
                    elif end[0]==tu[0]:
                        if end[1]<tu[1]:
                            break
                        elif end[1]==tu[1]:
                            if end[2]<tu[2]:
                                break
                    
                    f.write(f'{i},{j[0]},{j[1]},{j[-1][:-1]} \n')
                    last = [i, j]
    

    if last[1][0] == "ENTER":
        print("Student currently in Campus")
    elif last[1][0] == "EXIT":
        print("Student currently out of campus")

elif n == "2":
    time_d={}
    start=[int(i) for i in input("Enter starting time: ").split(":")]
    end=[int(i) for i in input("Enter ending time: ").split(":")]

    for line in data:
        line=line[:-1]
        line=line.split(",")
        
        time_d[line[-1]]=line
        
    with open("3_2_2_output.txt","w") as f1:
        for t in time_d:
            tu=[int(x) for x in t.split(":")]
            
            if start[0]<tu[0]<end[0]:
                f1.write(f'{time_d[t]} \n')
                print(time_d[t])
            elif start[0]==tu[0]:
                if start[1]<tu[1]:
                    f1.write(f'{time_d[t]} \n')
                elif start[1]==tu[1]:
                    if start[2]<tu[2]:
                        f1.write(f'{time_d[t]} \n')
            elif end[0]==tu[0]:
                if end[1]>tu[1]:
                    f1.write(f'{time_d[t]} \n')
                elif end[1]==tu[1]:
                    if end[2]>tu[2]:
                        f1.write(f'{time_d[t]} \n')

elif n=="3":
    gate=input("Enter the gate number: ")
    gate=" "+gate
    gates={}
    with open("sorted_data.txt") as f:
        data=f.readlines()
        for line in data:
            line=line.split(",")
            if line[2] not in gates:
                gates[line[2]]=[line]
            else:
                gates[line[2]].append(line)
    entercount=0
    exitcount=0
    for i in gates:
        if i==gate:
            for j in gates[i]:
                if j[1]==' ENTER':
                    entercount+=1
                if j[1]==' EXIT':
                    exitcount+=1
            
    print(f'No. of times students entered through gate {gate}: {entercount}')
    print(f'No. of times students exited through gate {gate}: {exitcount}')
    
            

        
