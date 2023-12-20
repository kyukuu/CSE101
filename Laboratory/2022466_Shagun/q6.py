with open("2022466_Shagun\in.txt") as f:
    with open("2022466_Shagun\out.txt" ,"w") as f2:
        data=f.readlines()
        for line in data:
            line=[int(i) for i in line.split()]
            sq=[i**2 for i in line]
            for i in sq:
                x=f'{i} '
                f2.write(x)
            y=f'\n'
            f2.write(y)
            
        