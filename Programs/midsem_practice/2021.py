# def finddistinct(l):
#     newlist = []
#     indexl = []
#     for i in l:

#         if i not in newlist:
#             newlist.append(i)
#             indexl.append(l.index(i))

#     for i in range(len(newlist)):
#         print(newlist[i], ":", indexl[i])


# l = [1, 2, 2, 1, 3, 4, 3]

# finddistinct(l)


# lst = [1, "banana", 12, "MIDSEM"]
# print(lst[1:3])
# lst[2] = "IIITD"
# print(lst[-2:-1])
# lst[3] += "_Exam"
# print(lst[3][::-1][3:8])
# print(len(lst))
# lst[1].replace('a', 'z')
# lst[1] = lst[1].replace('n', 'q')
# lst[1] = lst[1].split("q")
# print(lst[1])
# print(len(lst))
# print(len(lst[1]))


# def cubedigitsum(n):
#     sum = 0
#     for i in str(n):
#         sum = sum+int(i)**3
#     return sum


# print(cubedigitsum(231))

n = int(input())
k = int(input())
rem = []

while n > 0:
    i = n % 2
    rem.append(i)
    n = n//2
print(rem[::-1])
