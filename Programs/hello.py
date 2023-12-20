def prime(n):

    for i in range(2,n+1):
        Prime=True
        for j in range(2,i):
            if i%j==0:
                Prime=False
                break
        if Prime:
            print(i,end=" ")

n=int(input("Enter n: "))
prime(n)
