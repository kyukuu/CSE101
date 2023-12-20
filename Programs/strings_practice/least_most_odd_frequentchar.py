# str = input()
# unique = {}
# for i in str:
#     if i not in unique:
#         unique[i] = 0
#     unique[i] += 1

# l = [i for i in unique if unique[i] == min(unique.values())]

# for i in l:
#     print("The minimum of all character(s) is/are:", i)

# # for most frequent characters
# str = input()
# unique = {}
# for i in str:
#     if i not in unique:
#         unique[i] = 0
#     unique[i] += 1

# l = [i for i in unique if unique[i] == max(unique.values())]

# for i in l:
#     print("The maximum of all character(s) is/are:", i)

# # odd occurrences

str = input()
unique = {}
for i in str:
    if i not in unique:
        unique[i] = 0
    unique[i] += 1

for i in unique:
    x = unique[i]
    if int(x) % 2 == 1:
        print("odd occurrences:", i)
