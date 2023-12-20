print("Hello world")
list=[]
for i in range(6):
    element=input("Enter Marks for student "+ str(i))
    list.append(element)
print(list)
list.sort()

print("The sorted list is", list)