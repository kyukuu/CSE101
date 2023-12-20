str = input()
flag = True
for i in str:
    if not (i.isalnum() or i == " "):
        flag = False

if flag:
    print("Accepted")

else:
    print("Not Accepted")
