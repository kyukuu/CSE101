a=int(input("a: "))
r=int(input("r: "))
n=int(input("n: "))
sum=a
for i in range(1, n+1):
    sum=sum+a*(r**i)

print(sum)
