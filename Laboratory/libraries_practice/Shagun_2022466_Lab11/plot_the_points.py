
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
