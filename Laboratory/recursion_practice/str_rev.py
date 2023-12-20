def rev(s):
    if len(s) <= 0:
        return
    else:
        temp = s[0]
        rev(s[1:])
    print(temp)


print(rev("h"))
