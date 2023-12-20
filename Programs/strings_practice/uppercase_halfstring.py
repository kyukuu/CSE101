str = input()

if int(len(str)) % 2 == 0:
    half = int(len(str)/2)
else:
    half = int(len(str)/2)+1

s1 = str[:half]+str[half:].upper()
print(s1)
