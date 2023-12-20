def isa(lst):
    if len(lst) == 0 or len(lst) == 1:
        return True
    else:
        return lst[0] <= lst[1] and isa(lst[1:])


print(isa([1, 1, 70, 4, 5, 100, 111, 1333, 14567]))
