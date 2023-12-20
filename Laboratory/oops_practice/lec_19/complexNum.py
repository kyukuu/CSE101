class Complex:
    def __init__(self,r,i):
        self.i=i
        self.r=r

    def getreal(self):
        return self.r

    def getimag(self):
        return self.i
        
    def add(self,c):
        self.r=+c.getreal()
        self.i+=c.getimag()

    def equal(self,c):
        return self.r==c.getreal() and self.i==c.getimag()

    def sub(self,c):
        self.r-c.getreal()
        self.i=c.getimag()
    def modulus(self):
        return(self.r**2+self.i**2)**(1/2)
    def conjugate(self):
        return self.r,-self.i


c1,c2,c3=Complex(1,2),Complex(3,4),Complex(3,4)

print(c1.equal(c2))
c2.add(c3)

print(c2.getreal(),c2.getimag())
print(c2.modulus())
print(c1.conjugate())