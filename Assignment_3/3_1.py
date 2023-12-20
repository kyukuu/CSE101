
n = int(input("Enter the value of N: "))

if n == 1:
    print("* *")
elif n == 0:
    print()
elif n < 0:
    print(-1)
elif type(n) != int:
    print(-1)
else:
    i = 0

    edge = n

    def stars(n):
        global i
        if n == 1:
            print("* " + "  "*(2*edge-2) + "*")
        else:
            print("* "*n+"    "*i + "* "*n)
            i += 1
            stars(n-1)

    j = n-1

    def stars2(n):
        global j
        if n == 2:
            print("* "*2+"  "*(2*(edge-2)) + 2*"* ")
        else:
            stars2(n-1)
            print("* "*n+"  "*(2*(j-2))+"* "*n)
            j -= 1

    stars(n)
    stars2(n)


# 0,1,2 negative values of n, decimal inputs shouldnt be allowed
