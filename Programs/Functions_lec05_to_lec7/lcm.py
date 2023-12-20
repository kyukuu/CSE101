def lcm(a,b):
    
    if a>=b:
        bigger=a
        y=a
    else:
        bigger=b
        y=b

    while y>=bigger:
        if y%a==0 and y%b==0:
            print(y)
            break
        y=y+1

a=int(input())
b=int(input())

ans=lcm(a,b)