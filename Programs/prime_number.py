n=int(input())
prime=True
for i in range(2,n):
    if n%i==0:
        prime=False
    #you may or maynot add a break here
if prime:
    print("The number is prime")
else: 
    print("The number is not prime")


