import itertools

print("Approach 1:")
l1=[1,2,3]
l2=[4,5,6]
l=l1+l2

perm=itertools.permutations(l,2)
for i in perm:
    print(i, end=" ")
print()
print("Approach 2:")
t=[[(i,j) for i in l1] for j in l2]

ans=[]
for i in t:
    for j in i:
        if j not in ans:
            ans.append(j)
print(ans)
n=len()
def rec(l1,l2):
    global n
    if len(l1)==0 or len(l2)==0:
        pass
    else:
        print(l1[len(l1)-1-n],l2[len(l2)-1-n])
        l1=l1[:n]
rec(l1,l2)