n = int(input())

#list comprehension to find the numbers
lst = [[i for i in range(1, n) if i % j == 0] for j in [3, 5, 7, 9]]

#for loop used only for formatting the answer
ans=[]
for i in lst:
    for j in i:
        if j not in ans:
            ans.append(j)
if ans==[]:
    print("No numbers found")
else:
    print(sorted(ans))