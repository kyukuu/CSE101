class Complex:
    
    def __init__(self, r, im):
        self.real = r
        self.img = im
    def __len__(self):
        return self.real -self.img
    def __eq__(self,x):
        return self.real==x.real 
    def __add__(self,x):
        return self.real+x.real,self.img+x.img
c1=Complex(10,2)
c2=Complex(10,3)
print(c1 is c2)
print(len(c1))
print(c1==c2)
print(c1+c2)