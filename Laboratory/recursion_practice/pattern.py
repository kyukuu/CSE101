def A(n):
    if n > 0:
        print("", n, end='')
        B(n + 1)


def B(n):
    if n > 1:
        print("", n, end='')
        A(n - 5)


A(5)
