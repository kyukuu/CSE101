x0, y0 = 0, 0
x1, y1 = 0, 0
totald = 0
displacement = 0
while True:
    d = float(input("Enter the distance travelled by the car"))
    if d <= 0:
        break
    elif 0 < d <= 25:
        y1 = y1+d
    elif 26 < d <= 50:
        y1 = y1-d
    elif 51 < d <= 75:
        x1 = x1-d
    elif d >= 76:
        x1 = x1+d
    totald = totald + d

displacement = ((x1-x0)**2+(y1-y0)**2)**(1/2)
print("The final co-ordinates of the vehicle are: ", x1, y1)
print("Total distance travelled by the vehicle: ", totald)
print("Displacement wise distance travelled: ", displacement),
