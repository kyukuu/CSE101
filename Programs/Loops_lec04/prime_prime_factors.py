def factors(n):
    for i in range(3, int(n)+1):
        if n % i == 0:
            print(i, "is a factor")
    print("2 is a factor")


n = int(input())
for i in range(2, n):
    if n % i != 0:
        print(n, "is a Prime")
        break
    else:
        print(n, "is not a Prime")
        while n % 2 == 0:
            n = n/2
        break
factors(n)
