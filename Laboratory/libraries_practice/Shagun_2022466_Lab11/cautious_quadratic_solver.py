x=[int(x) for x in input().split()]
c,b,a=x[:3]
x1=(-b+(b**2-4*a*c)**(1/2))/2*a
x2=(-b-(b**2-4*a*c)**(1/2))/2*a


if a==0:
    print("Type-1")
elif b**2-4*a*c<0:
    print("Type-2")
elif b**2-4*a*c>=0:
    if x1>=x2:
        if x1%x2==0:
            print("True")
        else:
            print("False")
    if x1<x2:
        if x2%x1==0:
            print("True")
        else:
            print("False")
else:
    print("Type-3")