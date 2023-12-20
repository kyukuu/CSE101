class triangle:
    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def checkangles(self):
        return self.angle1+self.angle2+self.angle3 == 180


mytriangle = triangle(90, 30, 60)
print(mytriangle.number_of_sides)
print(mytriangle.checkangles())
