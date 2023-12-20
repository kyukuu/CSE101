list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

missinginlist2 = []
for i in list1:
    if i not in list2:
        missinginlist2.append(i)

print(missinginlist2)
