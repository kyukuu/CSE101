def palin(n):
    if len(n) == 0 or len(n) == 1:
        return True
    else:
        return palin(n[1:-1]) and n[0] == n[-1]


print(palin("civics"))
