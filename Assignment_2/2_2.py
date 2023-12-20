lst = []
while True:
    x = input("Enter your grades in the format: CourseName Credits Grade \n")
    if x == "":
        break
    else:
        x = x.split()
        flag_course = False
        if x[0][0].isupper() and x[0][-1].isdigit():
            flag_course = True
        if flag_course == False:
            print("Improper Course Name")
        flag_credits = False
        if x[1] == "1" or x[1] == "2" or x[1] == "4":
            flag_credits = True
        if flag_credits == False:
            print("Improper Credits")
        flag_grade = False
        if x[2] == "A+" or x[2] == "A" or x[2] == "A-" or x[2] == "B" or x[2] == "B-" or x[2] == "C" or x[2] == "C-" or x[2] == "D" or x[2] == "E" or x[2] == "F":
            flag_grade = True
        if flag_grade == False:
            print("Improper Grade")

        if flag_course == True and flag_credits == True and flag_grade == True:
            lst.append(x)


def sgpa(list):
    sums = 0
    sum_credits = 0
    grade = {
        "A+": 10,
        "A": 10,
        "A-": 9,
        "B": 8,
        "B-": 7,
        "C": 6,
        "C-": 5,
        "D": 4,
        "E": 3,
        "F": 2
    }
    for i in list:

        sums += int(i[1])*grade[i[2]]
        sum_credits += int(i[1])
    if sum_credits > 0:
        return round(sums/sum_credits, 2)
    else:
        print("No valid course entered")


lst = sorted(lst)
print("-------------------")
print("Semester Transcript")
print("-------------------")
for i in lst:
    print(f'{i[0]}          {i[2]}')
print("SGPA :  ", sgpa(lst))
print("-------------------")
