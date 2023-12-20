import math


def f(t):
    ans = (2000*(math.log(140000/(140000-2100*t))))-9.8*t
    return ans


a = float(input("Enter the starting time (in seconds): "))
b = float(input("Enter ending time(in seconds): "))

distance = 0
i = a
while a <= i < b:
    avg_v = (f(i)+f(i+0.25))/2
    distance = 0.25*avg_v + distance
    i = i+0.25


print("the distance covered by the rocket from the starting time to the ending time is:",
      distance, "metres")
