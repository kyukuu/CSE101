class Stack:
    def __init__(self):
        self.top=0
        self.data=[]
    def push(self,item):
        self.data.append(item)
        self.top+=1
    def pop(self):
        if self.top<=0:
            print("No elements present")
        item=self.data[self.top-1]
        self.data.remove(item)
        self.top-=1
        return(item)
    def isempty(self):
        return self.top<=0

def postfix(l):
    global stck
    stck=Stack()
    for i in l:
        if isinstance(i,float) or isinstance(i,int):
            stck.push(i)
        if isinstance(i,str):
            y=stck.pop()
            x=stck.pop()
            if i=="+":
                stck.push(x+y)
            elif i=="-":
                stck.push(x-y)
        
    
l=[2,3,"-",4,"+"]
print(postfix(l))
print(stck.data)
