class WaitingRoom:
    def __init__(self):
        self.line = []
        self.front = 0
        self.end = 0

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


list = WaitingRoom()

while True:
    choice = input("Make your choice: ")
    if choice == "":
        break
    if choice == "1":
        list.add(input("Enter: "))
    elif choice == "2":
        print(list.remove())
    elif choice == "3":
        print(list.isempty())

if list == []:
    print("No more students for the day")
else:
    print("Students in-waiting: ", len(list))
    print(list.line)
