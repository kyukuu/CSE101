def isvowel(n):
    if n.lower() in ["a", 'e', 'i', 'o', 'u']:
        return True


def countvowel(str, n):
    if n == 1:
        return isvowel(str[n-1])
    else:
        return countvowel(str, n-1)+isvowel(str[n-1])


print(countvowel("shagun", 6))
