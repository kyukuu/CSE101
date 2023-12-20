def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return (fact)


def sin(x):
    sum = 0
    for i in range(1, 25):
        sum = sum + (((-1)**(i+1))*(x**(2*i-1)))/factorial(2*i-1)
    return round(sum, 2)


def cos(x):
    sum = 0
    for i in range(0, 25):
        sum = sum + (((-1)**i)*(x**(2*i)))/factorial(2*i)
    return round(sum, 2)


def tan(x):
    tan = sin(x)/cos(x)
    return tan


print(tan(0.785398))
angle_degrees = float(
    input("Enter the angle of elevation of the pole in degrees: "))
angle = angle_degrees*(3.1415/180)
base = float(input("Enter the distance from the base of the pole:  "))
tan_angle = tan(angle)
height = base*tan_angle
length = (base**2+height**2)**(1/2)

print("Height of the pole is: ", height, "metres")
print("Distance to the tip of the pole from the observer is: ", length, "metres")
