names = "shagun"
age = "17"
date = "november"
print(f' the age of {names} is {age} as of {date}')


# sets are unordered un-indexed and without duplicates/ much like a bag
# are written in curly brackets

int_set = {1, 2, "hello", "meowmeow", 100}
print(int_set)

# sets are immutable- can change a set by deleting/adding..
# however, set itself is immutable object
# sets can have strings, int, float but not lists as set items

# s = {1, 2, [1, 2, 3, 4]}
# TypeError: unhashable type: 'list'

# sets dont have any order, cannot refer to nth item, internally also python may save them in its own order
s = {1, 2, 3, 4, 4, 6, 7}
print(5 in s)
print(1 in s)

for item in s:
    print("meme")

s.add(600)
s.remove(4)
s.discard(100)
# notice how discard doesn't throw in an error
# checkout difference between s.remove and s.discard

print(s)

s = {1, 2, 3, 4}
L = [1, 2, 3]
s.update(L)

print(s)

# operations on list

s1 = {1, 2, 3, 4, 5, 6}
s2 = {3, 4, 5, 6, 7, 8, 9, 9, 10}

s1.union(s2)
print(s1)

s1.intersection(s2)
print(s1) nṁ


sup = {n*(n+1) for n in range(0, 10)}
print(sup)
