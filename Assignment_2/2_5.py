n = int(input("Enter the number of co-ordinates you want to input"))
matrix = []
for i in range(n):
    r = []
    x, y = [float(x) for x in input().split()]
    r.append(x)
    r.append(y)
    r.append(1)
    matrix.append(r)
mult = []
for i in range(n):
    a = []
    for i in range(3):
        a.append(0)
    mult.append(a)

matrix1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matrix1[0][0] = float(input("Enter x scaling parameter: "))
matrix1[1][1] = float(input("Enter y scaling parameter: "))
matrix1[2][2] = 1

for i in range(len(matrix)):
    for j in range(len(matrix1[0])):
        for k in range(len(matrix1)):
            mult[i][j] += matrix[i][k]*matrix1[k][j]

for i in mult:
    print(i[0], i[1])



