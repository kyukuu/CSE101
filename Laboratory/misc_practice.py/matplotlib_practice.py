import matplotlib.pyplot as plt

x=[i for i in range(100)]
y=[j**2 for j in x]

plt.plot(x,y,"--",color="green",marker="o")
plt.title("saksham")
plt.xlabel("x-axis")
plt.ylabel('y-axis')
plt.show()