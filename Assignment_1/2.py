cost = 0
cost_values1 = []
cost_values2 = []
M = int(input("Enter Value of M: "))

for c in range(200):
    for t in range(200):
        if 8*t+2*c == 400 and 2*t+c == 120:
            c_ans = c
            t_ans = t
            cost = 90*M+25*M

            cost = cost + 100*(t-M)+30*(c-M)

            break


print("The number of chairs: ", c_ans)
print("The number of tables: ", t_ans)

print(cost)
