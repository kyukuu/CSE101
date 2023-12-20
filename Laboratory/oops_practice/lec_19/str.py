class Complex:
    
    def __init__(self, r, im):
        self.real = r
        self.img = im
    def __str__(self):
        return f'{self.real,self.img}'

c1=Complex(1,2)

print(c1)
print(c1.__str__())