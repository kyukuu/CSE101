mydict = {
    "ravi": 10,
    "rajnish": 9,
    "sanjeev": 15,
    "yash": 2,
    "suraj": 32
}
print(mydict.keys())
mykeys = list(mydict.keys())
print(mykeys)
mykeys.sort()
print(mykeys)

sorted_dict = {i: mydict[i] for i in mykeys}
print(sorted_dict)


# approach 2

key_value = {}

# Initializing value
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

for i in sorted(key_value.keys()):

    print(i, key_value[i], end=" ")
    # print(key_value[i])


dict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

# sorted_dict = {i: values for sorted(values))}
