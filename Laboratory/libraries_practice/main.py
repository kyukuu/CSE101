def fx1(a):
    return a*a
def fx2(a):
    return a*a*a
print("A print message in da module!")
if __name__=="__main__":
    print(fx1(2))
    print(fx2(2))