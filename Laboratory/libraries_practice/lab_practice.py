
import matplotlib.pyplot as plt
import numpy as np
y=[int(x) for x in input().split()]
x=[i for i in range(1,len(y)+1)]

means=np.mean(y)
means_l=[]
for i in range(len(x)):
    means_l.append(means)
plt.plot(x,y,color="Blue")
plt.plot(x,means_l,"--",color="Red")
plt.show()

import numpy
n=int(input())
p=int(input())
k=int(input())
m=int(input())


np=[]
for i in range(n):
    inp=float(x) for x in input().split()]
    np.append(inp)
km=[]
for i in range(k):
    inp=[float(x) for x in input().split()]
    km.append(inp)
    
np=numpy.array(np)
km=numpy.array(km)

if p!=k:
    print("Dimensions of matrices are not compatible")
else:
    ans=numpy.matmul(np,km)
    for i in ans:
        for j in i:
            print(j,end=" ")
        print()    
