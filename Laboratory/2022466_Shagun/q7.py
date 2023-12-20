l = [1, 1, 2, 2, 1, 3, 2, 4, 5, 2, 6, 7, 8, 9]
elt = int(input())
d = {}
for i in l:
    if i not in d:
        d[i] = 0
    d[i] += 1

indices = []
for i in range(len(l)):
    if l[i] == elt:
        indices.append(i)
print(f'frequency is {d[elt]} and indices are {indices}')
