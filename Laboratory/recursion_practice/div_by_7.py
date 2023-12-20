def dic(n):
    if n < 0:
        n = (-n)
    if n == 0 or n == 7:
        return True
    elif n < 10:
        return False
    else:
        return dic(n//10-2*(n-n//10*10))


n = 70
print(n-n//10*10)

print(dic(70))
