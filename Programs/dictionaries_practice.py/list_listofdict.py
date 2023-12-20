
test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
dict = {}
for i in range(len(test_list)):
    if i % 2 == 0:
        dict[test_list[i]] = test_list[i+1]

print(dict)

for i in dict:
    print(i, dict[i])
key_list = ["name", "number"]
# according to the question
res = []
for i in range(0, len(test_list), 2):
    res.append({key_list[0]: test_list[i], key_list[1]: test_list[i+1]})
print(res)
