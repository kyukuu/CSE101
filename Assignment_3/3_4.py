import time
class Student:
    def __init__(self,name,policy,assessments):
        self.name=name
        
        self.student_totalmarks=[]
        self.student_records=[]
        self.relevant_totalmarks=[]
        self.policy=policy
        self.assessments=assessments

    def uploadmarks(self):
        with open("marks.txt") as f:
            data = f.readlines()
        
            for line in data:
                line = line.split(",")
                line = [int(x) for x in line]
                marks = line[1:]
                marks = [int(x) for x in marks]
                sum_marks = sum(marks)
                self.student_totalmarks.append(sum_marks)
                line.append(sum_marks)
                self.student_records.append(line)

        self.student_totalmarks = sorted(self.student_totalmarks)
        for i in self.policy:
            self.relevant_totalmarks = []
            for j in self.student_totalmarks:
                if j in range(i-2, i+2):
                    self.relevant_totalmarks.append(j)
            diff = []
            for ele in range(1, len(self.relevant_totalmarks)):
                diff.append(
                    self.relevant_totalmarks[ele-1]-self.relevant_totalmarks[ele])

            if diff != []:
                maxval_index = diff.index(max(diff))
                ll = self.relevant_totalmarks[maxval_index]
                ul = self.relevant_totalmarks[maxval_index+1]

                self.policy[self.policy.index(i)] = (ll+ul)/2
        for i in self.student_records:
            if i[-1] >= self.policy[0]:
                i.append("A")

            elif self.policy[0] > i[-1] >= self.policy[1]:
                i.append("B")
            elif self.policy[1] > i[-1] >= self.policy[2]:
                i.append("C")
            elif self.policy[2] > i[-1] >= self.policy[3]:
                i.append("D")
            elif self.policy[3] > i[-1]:
                i.append("F")
        print(self.policy)
        return (self.student_records)

class Course:
    def __init__(self,name,credits,assessments,policy,student_records):
        self.name=name
        self.credits=credits
        self.assessments=assessments
        self.policy=policy
        self.student_records=student_records



        self.freq = {}

        self.out=0
    
    def summary(self):
        

        print("Course:", self.name)
        print("Credits:", self.credits)
        print("assessments and their weights:", self.assessments)
        print("Cutoffs for different grades:", self.policy)
        for i in self.student_records:
            if i[-1] not in self.freq:
                self.freq[i[-1]] = 0
            self.freq[i[-1]] += 1
        print("Grading Summary: ")
        for i in self.freq:
            print(f'{i}: {self.freq[i]}')
    def grade(self):
        with open("3_4_output_dict.txt", "w") as f:
            for i in self.student_records:
                self.out = f'Rollnumber: {i[0]} Total Marks: {i[-2]} Grade: {i[-1]}'
                f.write(self.out+"\n")
                print(self.out)
                
    def search(self,x):
        for i in self.student_records:
            if int(x) == i[0]:
                print(
                    f'Roll No: {i[0]} Marks: {i[1:5]}  Total Marks: {i[5]} Grade: {i[6]}')
    



s1=Student("Shagun",[80, 65, 50, 40],[["labs", 30], ["midsem", 15], ["assignments", 30], ["endsem", 25]])
st_records=s1.uploadmarks()
IP=Course("IP",4, [["labs", 30], ["midsem", 15], ["assignments", 30], ["endsem", 25]],s1.policy,st_records)


print("Select choice 1 to generate summary")
print("Select choice 2 to generate grades of all students")
print("Select choice 3 to search for a student record")
# search for students with same name/roll no?
# is it fine if i work with roll numbers instead of names, int problems
while True:
    n = int(input("Enter Choice: "))
    if n == "":
        break
    if n == 1:
        IP.summary()
    elif n == 2:
        begin1=time.time()
        IP.grade()
        end1=time.time()
        print("Runtime taken for grading operation:",end1-begin1)
    elif n == 3:
        begin2=time.time()
        searchwhat = input("Enter the Roll Number you want to search: ")
        IP.search(searchwhat)
        end2=time.time()
        print("Runtime taken for search operation:", end2-begin2)
    else:
        print("Invalid Input")

