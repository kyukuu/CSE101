factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        return (fact)


x=int(input('enter x '))
n=int(input('enter n'))
sum=1
for i in range(1,n):
    sum=sum+ (x**i)/factorial(i)

print(sum)