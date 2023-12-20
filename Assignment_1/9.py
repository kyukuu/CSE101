
import math


def demand(p):
    a = 10
    b = 1.05
    D = math.exp(a-(b*p))
    return int(D)


def supply(p):
    c = 1
    d = 1.06
    D = math.exp(c+(d*p))
    return int(D)


i = 1
while i >= 1:
    if demand(i)-supply(i) <= 0.05:
        ans = i
        break
    i += 1*(5/1000)

print("Equilibrium Price: ", ans)
print("Demand at the above mentioned Price: ", demand(i))
print("Supply at the above mentioned Price: ", supply(i))
