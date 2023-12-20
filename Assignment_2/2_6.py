try:
    with open("IPmarks.txt") as f:
        with open("IPgrades.txt", "w") as f2:
            data = f.readlines()
            weights = [(10, 5), (10, 5), (40, 20),
                       (100, 30), (10, 5), (10, 5), (80, 30)]

            sum_weights = 0
            for i in weights:
                sum_weights += i[1]

            listofweighted_avg = []
            for i in data:
                i = i.split(",")
                marks = i[1:]
                marks = [float(x) for x in marks]

                weighted_sum = 0

                # calculating the weighted sum
                for j in range(len(marks)):
                    weighted_sum += marks[j]*(weights[j][1])/weights[j][0]

                weighted_avg = weighted_sum
                # weighted_avg = weighted_avg/2
                listofweighted_avg.append(weighted_avg)

            def gradealloted(a):
                if a < 0:
                    return "Invalid Percentage"
                elif 0 < a < 30:
                    return "F"
                elif 30 <= a < 35:
                    return "D"
                elif 35 <= a < 40:
                    return "C-"
                elif 40 <= a < 50:
                    return "C"
                elif 50 <= a < 60:
                    return "B-"
                elif 60 <= a < 70:
                    return "B"
                elif 70 <= a < 80:
                    return "A"
                elif a >= 80:
                    return "A+"

            count = 0
            for i in data:

                i = i.split(",")
                marks_p = i[1:]

                marks_p = [float(x) for x in marks_p]
                name = i[0]
                total_marks = sum(marks_p)

                grade = gradealloted(listofweighted_avg[count])
                count += 1
                str = f'{name} {total_marks} {grade} \n'
                f2.write(str)
except:
    print("File doesn't exist or invalid input format")
