def f(x):
    ans = x**3 - 10.5*x**2 + 34.5*x - 35
    return ans


def f_dash(x):
    ans = 3*(x**2) - 21*x + 34.5
    return ans


def func(x0):
    for i in range(100):
        if f(x0) <= 0.02 and f(x0) >= -0.02:
            return x0

        else:
            x0 = (x0-(f(x0)/f_dash(x0)))


x = float(input("Enter value of x for f(x): "))
ans = func(x)
if ans != 0:
    print(round(func(x), 2))
else:
    print("No root found")
