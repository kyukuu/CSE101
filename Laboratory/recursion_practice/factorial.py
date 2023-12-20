# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)


# def digits(n):
#     if n <= 9:
#         return 1
#     else:
#         return 1+digits(n//10)

# def fib(n):
#     if n==1 or n==0:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)


# def len(l):
#     if l==[]:
#         return 0
#     else:
#          return 1+len(l[1:])


# def setl(s):
#     if s==set():
#         return 0
#     else:
#         x=s.pop()
#         return 1+ setl(s)



# def gcd(x,y):
#     if y==0:
#         return x
#     else:
#         return gcd(y,x%y)



def palin(s):
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and palin(s[1:-1])
print(palin(""))

def sume(lst):
    if len(lst)<=1:
        return lst[0]
    else:
        return lst[0]+sume(lst[1:])
print(sume([1,2,3,4,5,6,7]))

def sumd(i):
    if i<=9:
        return i
    else:
        return i%10+sumd(i//10)

print(sumd(391))
count=0
def pascal(n):
    global count
    count+=1
    print("count:",count)
    if n==1:
        print([1])
        return [1]
    else:
        line=[1]
        prev=pascal(n-1)
        
        for i in range(len(prev)-1):
            line.append(prev[i]+prev[i+1])
        line+=[1]
        return line
    
print(pascal(4))