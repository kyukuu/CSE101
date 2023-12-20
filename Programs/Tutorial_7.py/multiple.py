n = int(input())

lst = [i for i in range(n+1) if i % 3 == 0 and i % 5 == 0]
print(set(lst))
