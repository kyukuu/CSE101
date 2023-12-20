sumeven=0
sumodd=0
for i in range(12, 38):

    if i%2==0:
        sumeven=sumeven+i
print(sumeven)

for i in range(12,38):

    if i%2!=0:
        sumodd=sumodd+i
print(sumodd)