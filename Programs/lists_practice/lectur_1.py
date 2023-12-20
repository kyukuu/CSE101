# # print("good morning")
# # L1 = [1, 2, 3, 4, 5]
# # print(L1[-3::2])

# L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# string = '''
# heyyo
# '''
# print(L[-2:-5])
# print(L[-5: -2])
# x = 10 in L
# print(x)
# L[-4] = 10000

# print(L[-5: -2])
# print(len(L[0:5]))


# print(string)
# print(len(string))


# print(L)
# print(sum(L))
# print(sum(L[1:6]))
# del L[7]
# print(L)

# # operations on lists

# if 10 in L:
#     print(L[5])
# if 100 not in L:
#     print(L[:]*2)


# L_1 = ["shagun"]
# L_2 = ["cutie"]

# print(L_1, L_2)
# print(L_1+L_2)
# print(L_2*3)

# L_1.append("kaku")
# print(L_1)

# L_1.insert(0, "peekaboo")
# print(L_1)

# L_1.extend(L_2)
# print(L_2)
# print(L_1 + L_2)

# Operations for removing data

# L = [1, 3, 4, 6, 7, 8, 9, 6, 67, 7, 88, 8, None, 76, 4, 4, 4000]
# print(L)

# L.remove(1)
# print(L)

# x = L.pop()
# print(x)

# L.clear()
# print(L)

# Operations on list

# print(L.index(67))

# Lnew = L.reverse
# print(L)
# print(Lnew)
# print(L.count(4))

# lst = [2, 2, 2, 2, 5, 5, 5, 8, 8, 8, 8, 8, 6, 6, 6, 6, 4, 4, 7, 7, 7, 5, 7, 7]
# res = []
# count = 1

# for i in range(1, len(lst)):
#     if lst[i] == lst[i-1]:
#         count += 1
#     else:
#         count = count*lst[i-1]
#         res.append(count)
#         count = 1

# print(res)

# lst = [2, 3, 3, 5, 7, 3, 4, 3]

# old_val = 3
# new_val = 13
# if old_val in lst:
#     for i in range(len(lst)):
#         if lst[i] == old_val:
#             lst[i] = new_val
#     print("Index : ", i)
#     print(lst)
# else:
#     print(old_val, " not in list")

# L1 = [1, 3, 5, 6, 7]

# L2 = L1
# L3 = L1.copy()

# L3[2] = 200

# print(L1)
# print(L2)
# print(L3)

# print(id(L1))
# print(id(L2))
# print(id(L3))

# list = [1, 3, 2, 5, 9, 4]


# # def sum(list=[]):
# #     sum = 0
# #     for item in len(list):
# #         sum = item[i]**2 + sum

# #     return sum


# # fl = ["orange", "mango", "kiwi", "pineapple", "banana"]
# # fl.sort(reverse=True, key=len)
# # print(fl)

# def f(var):
#     return (var**2)


# list.sort(key=f)
# print(list)

# def sql(b):
#     b[0] = 2
#     b2 = [i*i for i in b]
#     return b2


# a = [1, 3, 5, 7, 8]
# a2 = sql(a)
# print(a)
# print(a2)

# list comprehension

# list0 = [i for i in range(1, 100) if i % 2 == 0]
# print(list0)

# list1 = [x**2 for x in range(1, 10)]
# print(list1)

# list2 = [x**2 for x in list]
# print(list2)
# c = 10
# list3 = [x*c for x in range(1, 10)]
# L1 = [2, 3, 3, 5, 7, 3, 4, 3]
# list4 = [x for x in L1 if x != 3]
# print(list4)

# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]

# L3 = [l1[i]*l2[i] for i in range(len(l1))]
# print(L3)

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # print(M[2][2])
# # print(sum(M))


# for i in (M):
#     print(i)

# for i in (M):
#     for j in i:
#         print(j, end=' ')
#     print()

# for i in range(len(M)):
#     for j in range(len(M[i])):
#         print(M[i][j], end=" ")
#     print()


# n, m = 4, 6
# listnew = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(0)
#     listnew.append(row)

# print(listnew)


# newlist = []
# for i in range(m):
#     newlist.append([0 for i in range(n)])
# print(newlist)

# N, M = 3, 4
# lst2 = []
# for i in range(N):
#     lst2.append([0 for i in range(M)])
# print(lst2)
# print(M)

# for i in range(3):
#     M[i].pop(1)

# print(M)
# list = []
# n = 3
# for i in range(n):
#     list.append([0 for i in range(n)])
# print(list)

# for i in range(n):
#     for j in range(n):
#         if i < j:
#             list[i][j] = -1
#         if i > j:
#             list[i][j] = 1
# print(list)


# def print_matrix(list):
#     for i in list:
#         print(i)


# print_matrix(list)
