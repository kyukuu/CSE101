class Triangle:
    def __init__(self,p1,p2,p3):
        self.l1=((p1[0]-p2[0])**2+p1[1]-p2[1]**2)**(1/2)
        self.l2=((p2[0]-p3[0])**2+p2[1]-p3[1]**2)**(1/2)
        self.l3=((p1[0]-p3[0])**2+p1[1]-p3[1]**2)**(1/2)

    def equilateral(self):
        return self.l1==self.l2 and self.l2==self.l3 and self.l1==self.l3
    def perimeter(self):
        return self.l1+self.l2+self.l3
    
t0=Triangle((1,2),(2,3),(1,1))

print(t0.perimeter())