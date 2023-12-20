s1 = "abcs"
s2 = "cxzca"

s1 = set(s1)
s2 = set(s2)

uncommons1 = s1 - s2
uncommon2 = s2-s1

uncommon = uncommons1.union(uncommon2)

print("".join(uncommon))
