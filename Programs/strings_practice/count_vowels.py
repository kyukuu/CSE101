vowels = {"a", "e", "i", "o", "u"}
str = input()
str = str.lower()
count = 0
for i in str:
    if i in vowels:
        count += 1
print("The number of vowels are: ", count)
