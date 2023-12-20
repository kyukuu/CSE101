num=int(input())
sums=0
for i in range(1, num):
    if num%i==0:
        sums=sums+i

if num==sums:
    print("perfect number")
else:
    print("not a perfect number")