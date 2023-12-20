
test_list = [{"gfg": 2, "best": 4},
             {"gfg": 2, "is": 3, "best": 4},
             {"gfg": 2}]

leng = 0
for i in test_list:
    if len(i) > leng:
        leng = len(i)
        ans = i
print(ans)

res = max(test_list, key=len)
print(res)
