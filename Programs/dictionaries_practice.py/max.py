Car = {'Audi': 100, 'BMW': 1292, 'Jaguar': 210000, 'Hyundai': 88}
maxval = max(Car.values())
ans = [i for i in Car if Car[i] == maxval]
print(ans)

# approach 2
v = list(Car.values())
k = list(Car.keys())

print(k[v.index(max(v))])
