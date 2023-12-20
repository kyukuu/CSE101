str = input()
freq = {}
for i in str:
    if i not in freq:
        freq[i] = 0
        freq[i] += 1
    freq[i] += 1

print(freq)
