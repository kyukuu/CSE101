times=0
# def classesgrade():
#     global times
#     import time
#     class Student:
#         def __init__(self,name,policy,assessments):
#             self.name=name
            
#             self.student_totalmarks=[]
#             self.student_records=[]
#             self.relevant_totalmarks=[]
#             self.policy=policy
#             self.assessments=assessments

#         def uploadmarks(self):
#             with open("marks.txt") as f:
#                 data = f.readlines()
            
#                 for line in data:
#                     line = line.split(",")
#                     line = [int(x) for x in line]
#                     marks = line[1:]
#                     marks = [int(x) for x in marks]
#                     sum_marks = sum(marks)
#                     self.student_totalmarks.append(sum_marks)
#                     line.append(sum_marks)
#                     self.student_records.append(line)

#             self.student_totalmarks = sorted(self.student_totalmarks)
#             for i in self.policy:
#                 self.relevant_totalmarks = []
#                 for j in self.student_totalmarks:
#                     if j in range(i-2, i+2):
#                         self.relevant_totalmarks.append(j)
#                 diff = []
#                 for ele in range(1, len(self.relevant_totalmarks)):
#                     diff.append(
#                         self.relevant_totalmarks[ele-1]-self.relevant_totalmarks[ele])

#                 if diff != []:
#                     maxval_index = diff.index(max(diff))
#                     ll = self.relevant_totalmarks[maxval_index]
#                     ul = self.relevant_totalmarks[maxval_index+1]

#                     self.policy[self.policy.index(i)] = (ll+ul)/2
#             for i in self.student_records:
#                 if i[-1] >= self.policy[0]:
#                     i.append("A")

#                 elif self.policy[0] > i[-1] >= self.policy[1]:
#                     i.append("B")
#                 elif self.policy[1] > i[-1] >= self.policy[2]:
#                     i.append("C")
#                 elif self.policy[2] > i[-1] >= self.policy[3]:
#                     i.append("D")
#                 elif self.policy[3] > i[-1]:
#                     i.append("F")
#             return (self.student_records)

#     class Course:
#         def __init__(self,name,credits,assessments,policy,student_records):
#             self.name=name
#             self.credits=credits
#             self.assessments=assessments
#             self.policy=policy
#             self.student_records=student_records



#             self.freq = {}

#             self.out=0
        
#         def summary(self):
            

#             print("Course:", self.name)
#             print("Credits:", self.credits)
#             print("assessments and their weights:", self.assessments)
#             print("Cutoffs for different grades:", self.policy)
#             for i in self.student_records:
#                 if i[-1] not in self.freq:
#                     self.freq[i[-1]] = 0
#                 self.freq[i[-1]] += 1
#             print("Grading Summary: ")
#             for i in self.freq:
#                 print(f'{i}: {self.freq[i]}')
#         def grade(self):
#             with open("3_4_output_dict_runtime.txt", "w") as f:
#                 for i in self.student_records:
#                     self.out = f'Rollnumber: {i[0]} Total Marks: {i[-2]} Grade: {i[-1]}'
#                     f.write(self.out+"\n")
                    
                    
#         def search(self,x):
#             for i in self.student_records:
#                 if int(x) == i[0]:
#                     print(
#                         f'Roll No: {i[0]} Marks: {i[1:5]}  Total Marks: {i[5]} Grade: {i[6]}')
        



#     s1=Student("Shagun",[80, 65, 50, 40],[["labs", 30], ["midsem", 15], ["assignments", 30], ["endsem", 25]])
#     st_records=s1.uploadmarks()
#     IP=Course("IP",4, [["labs", 30], ["midsem", 15], ["assignments", 30], ["endsem", 25]],[80, 65, 50, 40],st_records)


#     n = int(2)
#     if n == "":
#         pass
#     if n == 1:
#         IP.summary()
#     elif n == 2:
#         begin1=time.time()
#         IP.grade()
#         end1=time.time()
#         times+=end1-begin1

#     elif n == 3:
#         begin2=time.time()
#         searchwhat = input("Enter the Roll Number you want to search: ")
#         IP.search(searchwhat)
#         end2=time.time()
#         print("Runtime taken for search operation:", end2-begin2)
# times1=0
# def classessearch():
#     global times1
#     import time
#     class Student:
#         def __init__(self,name,policy,assessments):
#             self.name=name
            
#             self.student_totalmarks=[]
#             self.student_records=[]
#             self.relevant_totalmarks=[]
#             self.policy=policy
#             self.assessments=assessments

#         def uploadmarks(self):
#             with open("marks.txt") as f:
#                 data = f.readlines()
            
#                 for line in data:
#                     line = line.split(",")
#                     line = [int(x) for x in line]
#                     marks = line[1:]
#                     marks = [int(x) for x in marks]
#                     sum_marks = sum(marks)
#                     self.student_totalmarks.append(sum_marks)
#                     line.append(sum_marks)
#                     self.student_records.append(line)

#             self.student_totalmarks = sorted(self.student_totalmarks)
#             for i in self.policy:
#                 self.relevant_totalmarks = []
#                 for j in self.student_totalmarks:
#                     if j in range(i-2, i+2):
#                         self.relevant_totalmarks.append(j)
#                 diff = []
#                 for ele in range(1, len(self.relevant_totalmarks)):
#                     diff.append(
#                         self.relevant_totalmarks[ele-1]-self.relevant_totalmarks[ele])

#                 if diff != []:
#                     maxval_index = diff.index(max(diff))
#                     ll = self.relevant_totalmarks[maxval_index]
#                     ul = self.relevant_totalmarks[maxval_index+1]

#                     self.policy[self.policy.index(i)] = (ll+ul)/2
#             for i in self.student_records:
#                 if i[-1] >= self.policy[0]:
#                     i.append("A")

#                 elif self.policy[0] > i[-1] >= self.policy[1]:
#                     i.append("B")
#                 elif self.policy[1] > i[-1] >= self.policy[2]:
#                     i.append("C")
#                 elif self.policy[2] > i[-1] >= self.policy[3]:
#                     i.append("D")
#                 elif self.policy[3] > i[-1]:
#                     i.append("F")
#             return (self.student_records)

#     class Course:
#         def __init__(self,name,credits,assessments,policy,student_records):
#             self.name=name
#             self.credits=credits
#             self.assessments=assessments
#             self.policy=policy
#             self.student_records=student_records



#             self.freq = {}

#             self.out=0
        
#         def summary(self):
            

#             print("Course:", self.name)
#             print("Credits:", self.credits)
#             print("assessments and their weights:", self.assessments)
#             print("Cutoffs for different grades:", self.policy)
#             for i in self.student_records:
#                 if i[-1] not in self.freq:
#                     self.freq[i[-1]] = 0
#                 self.freq[i[-1]] += 1
#             print("Grading Summary: ")
#             for i in self.freq:
#                 print(f'{i}: {self.freq[i]}')
#         def grade(self):
#             with open("3_4_output_dict_runtime.txt", "w") as f:
#                 for i in self.student_records:
#                     self.out = f'Rollnumber: {i[0]} Total Marks: {i[-2]} Grade: {i[-1]}'
#                     f.write(self.out+"\n")
                    
                    
#         def search(self,x):
#             for i in self.student_records:
#                 if int(x) == i[0]:
#                     ans=(f'Roll No: {i[0]} Marks: {i[1:5]}  Total Marks: {i[5]} Grade: {i[6]}')
#                     return ans

#     begin=time.time()
#     s1=Student("Shagun",[80, 65, 50, 40],[["labs", 30], ["midsem", 15], ["assignments", 30], ["endsem", 25]])
   
#     st_records=s1.uploadmarks()
    
#     IP=Course("IP",4, [["labs", 30], ["midsem", 15], ["assignments", 30], ["endsem", 25]],[80, 65, 50, 40],st_records)
#     end=time.time()

#     begin2=time.time()
#     list=["2022001","2022002","2022003","2022004","2022005","2022006","2022007","2022008","2022009"]
#     for i in list:
#         w=IP.search(i)
#         print(w)
        
#     end2=time.time()  
#     return end2-begin2

def dgs():
    import time
    course = "IP"
    credits = 4
    assessments = [("labs", 30), ("midsem", 15),
                ("assignments", 30), ("endsem", 25)]
    policy = [80, 65, 50, 40]
    # def summary(course, assessments, credits):

    begin1=time.time()
    def assigning_grades():
        with open("marks.txt") as f:
            data = f.readlines()
            student_totalmarks = []
            student_records = []
            for line in data:
                line = line.split(",")
                line = [int(x) for x in line]
                marks = line[1:]
                marks = [int(x) for x in marks]
                sum_marks = sum(marks)
                student_totalmarks.append(sum_marks)
                line.append(sum_marks)
                student_records.append(line)

            student_totalmarks = sorted(student_totalmarks)
            for i in policy:
                relevant_totalmarks = []
                for j in student_totalmarks:
                    if j in range(i-2, i+2):
                        relevant_totalmarks.append(j)
                diff = []
                for ele in range(1, len(relevant_totalmarks)):
                    diff.append(
                        relevant_totalmarks[ele-1]-relevant_totalmarks[ele])

                if diff != []:
                    maxval_index = diff.index(max(diff))
                    ll = relevant_totalmarks[maxval_index]
                    ul = relevant_totalmarks[maxval_index+1]

                    policy[policy.index(i)] = (ll+ul)/2
            for i in student_records:
                if i[-1] >= policy[0]:
                    i.append("A")

                elif policy[0] > i[-1] >= policy[1]:
                    i.append("B")
                elif policy[1] > i[-1] >= policy[2]:
                    i.append("C")
                elif policy[2] > i[-1] >= policy[3]:
                    i.append("D")
                elif policy[3] > i[-1]:
                    i.append("F")
            return (student_records)


    begin1=time.time()
    student_records = assigning_grades()

    end1=time.time()
    def summary():
        freq = {}

        print("Course:", course)
        print("Credits:", credits)
        print("assessments and their weights:", assessments)
        print("Cutoffs for different grades:", policy)
        for i in student_records:
            if i[-1] not in freq:
                freq[i[-1]] = 0
            freq[i[-1]] += 1
        print("Grading Summary: ")
        for i in freq:
            print(f'{i}: {freq[i]}')
    begin2=time.time()
    def grade():
        with open("3_5_output_dict.txt", "w") as f:
            for i in student_records:
                out = f'Rollnumber: {i[0]} Total Marks: {i[-2]} Grade: {i[-1]}'
                f.write(out+"\n")
                print(out)
    end2=time.time()
    begin3=time.time()
    def search(x):
        for i in student_records:
            if int(x) == i[0]:
                print(
                    f'Roll No: {i[0]} Marks: {i[1:5]}  Total Marks: {i[5]} Grade:{i[6]}')

    end3=time.time()
    
    
    begin1=time.time()
    for i in range(100):
        grade()
    end1=time.time()
    print("Runtime for grading operation using dictionary: ", end1-begin1)

    
    begin2=time.time()
    list=["2022001","2022002","2022003","2022004","2022005","2022006","2022007","2022008","2022009"]
    for i in list:
        searchwhat = i
            
        search(searchwhat)
    end2=time.time()
    print("Runtime for search  operation using dictionary: ", end2-begin2)

# for i in range(100):
#     classesgrade()
# ans=classessearch()
# # print(f'Runtime for grades using classes : {times}')
# print(f'Runtime for search using classes : {ans}')
dgs()
