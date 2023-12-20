passw = input()


def checker(passw):
    flag1 = True
    if len(passw) < 8:
        flag1 = False

    flag2 = False
    for i in passw:
        if i.isdigit():
            flag2 = True
            break

    chars = ['@', '#', '$', '%', '&']
    flag3 = False
    for i in passw:
        if i in chars:
            flag3 = True
            break

    flag4 = False
    for i in passw:
        if i.isupper():
            flag4 = True
            break

    flag5 = False
    for i in passw:
        if i.islower():
            flag5 = True
            break
    return flag1 and flag2 and flag3 and flag4 and flag5


print(checker(passw))
