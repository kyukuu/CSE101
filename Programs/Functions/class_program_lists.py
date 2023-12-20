# written by shagun :)
lissty = [2, 2, 2, 2, 5, 5, 5, 8, 8, 8, 8,
          8, 6, 6, 6, 6, 4, 4, 7, 7, 7, 5, 7, 7]


def repeater(list):
    list_count = []
    count = 1
    for i in range(1, (len(list))):

        if list[i-1] == list[i]:
            count += 1
            product = count*list[i]
        else:
            list_count.append(product)
            count = 0
    return list_count


print(repeater(lissty))

# from slides

lst = [2, 2, 2, 2, 5, 5, 5, 8, 8, 8, 8, 8, 6, 6, 6, 6, 4, 4, 7, 7, 7, 5, 7, 7]

res = []
count = 1

for i in range(1, len(lst)):

    if lst[i] == lst[i-1]:
        count += 1
        product = count*lst[i]
    else:
        res.append(product)
        count = 1


print(res)
