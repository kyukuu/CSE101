s = input()

half = int(len(s)/2)

if len(s) % 2 == 0:
    firsthalf = s[:half]
    secondhalf = s[half:]
else:
    firsthalf = s[:half]
    secondhalf = s[half+1:]

if firsthalf == secondhalf:
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")

if firsthalf == secondhalf[::-1]:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
