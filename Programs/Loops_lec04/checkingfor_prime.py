x=int(input())
for i in range(x):
    if x%i==0:
        print("Number is not prime")
        break
    else:
        print("Number is a prime")