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

def grade():
    with open("3_5_output_dict.txt", "w") as f:
        for i in student_records:
            out = f'Rollnumber: {i[0]} Total Marks: {i[-2]} Grade: {i[-1]}'
            f.write(out+"\n")
            print(out)


def search(x):
    for i in student_records:
        if int(x) == i[0]:
            print(
                f'Roll No: {i[0]} Marks: {i[1:5]}  Total Marks: {i[5]} Grade:{i[6]}')


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
        summary()
    elif n == 2:
        begin1=time.time()
        grade()
        end1=time.time()
        print("Runtime for grading operation: ", end1-begin1)

    elif n == 3:
        searchwhat = input("Enter the Roll Number you want to search: ")
        begin2=time.time()
        search(searchwhat)
        end2=time.time()
        print("Runtime for grading operation: ", end2-begin2)

#placement of begin and end of time
#different time for running the same operation twice
#running N times, not quite working out
#time goes on increasing after every run