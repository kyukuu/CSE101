def nat(n):
    if n == 1:
        print(n)
    else:
        ans = nat(n-1)
        print(n)


nat(10)


def nat_rev(n):
    if n == 1:
        print(n)
    else:
        print(n)
        ans = nat_rev(n-1)


nat_rev(10)
