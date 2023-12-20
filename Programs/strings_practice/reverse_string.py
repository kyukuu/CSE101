# s = input().split()

# s_reverse = s[::-1]
# for i in s_reverse:
#     print(i, end=" ")

# input string
string = "geeks quiz practice code"
# reversing words in a given string
s = string.split()[::-1]
print(s)
l = []
for i in s:
    print(i, end=" ")
