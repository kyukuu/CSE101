class WaitingRoom:
    def __init__(self):
        self.line = []
        self.front = 0
        self.end = 0
    def __len__(self):
        return len(self.line)
   
    def __str__(self):
        return f'{self.line}'


    def add(self, stud):
        self.line.append(stud)
        self.end += 1

    def remove(self):
        x = None
        if self.isempty() == False:
            x = self.line[0]
            self.line.remove(x)
            self.end -= 1
        else:
            return ("Queue is empty")
        return x

    def isempty(self):
        return self.front-self.end == 0

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.grade=0
    def grade(self,yr):
        self.grade=yr
    def __str__(self):
        return f'{self.name} {self.rollno} {self.grade}'
    

qs=WaitingRoom()
s1=Student("One",11)
qs.add(s1)
s2=Student("Two",122)
qs.add(s2)
s3=Student("Three",1)
qs.add(s3)
# s3.grade(2022)
print("Student Queue: ",len(qs))
print("Students: ")
for i in qs.line:
    print(i)