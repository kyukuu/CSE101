class Student:
    def __init__(self, roll: int, name: str):
        self.roll = roll
        self.name = name
        self.courses = {}

    def addcourse(self, course: str, grade: int):
        self.courses[course] = grade

        grades = list(self.courses.values())
        if len(grades) == 0:
            self.grade = 0
            return f"No grades found"
        else:
            self.grade = sum(grades)/len(grades)
            return f'Average: {sum(grades)/len(grades)}'

    def records(self):
        return f'Roll no: {self.roll} Name: {self.name}  Courses: {self.courses} Average Grade: {self.grade}'


s1 = Student("23001", "Stu1")
s1.addcourse("cs101", 9)
s1.addcourse("M101", 8)

print(s1.records())
