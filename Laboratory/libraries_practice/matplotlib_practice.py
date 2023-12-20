import matplotlib.pyplot as plt
import math

# x=[1,2,4,5]
# y=[2,4,6,8]

# plt.scatter(x,y)

# plt.title("this is so fun")
# plt.xlabel=("X-Axis")
# plt.ylabel=("Y-Axis")
# plt.show()
x=[i for i in range(100)]
y=[math.sin(i) for i in range(100)]

plt.plot(x,y)
plt.show()
