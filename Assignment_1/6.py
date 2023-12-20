n = int(input("Enter a number n: "))

for i in range(n):
    print("*" * (i+1), end="")
    print(" "*(2*(n-(i+1))), end="")
    print("*"*(i+1), end="")
    print()
