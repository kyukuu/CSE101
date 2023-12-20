def sum(n):
    if n <= 1:
        return n
    else:
        ans = sum(n-1)
    return n + ans


print(sum(100))
