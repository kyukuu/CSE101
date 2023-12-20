str = input()
vowels1 = ["a", "e", "i", "o", "u"]
vowels2 = ['A', 'E', 'I', 'O', 'U']
flag1 = True
flag2 = True
for i in vowels1:
    if i not in str:
        flag1 = False
for i in vowels2:
    if i not in str:
        flag2 = False
if not flag1 or not flag2:
    print("Accepted")
else:
    print("Not accepted")
