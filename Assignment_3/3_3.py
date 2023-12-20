import random
n = 3
for i in range(n+1):
    with open(f"file{i+1}.txt") as f:
        data = f.read()
        data = data.lower()

        def f1(data):
            data = data.split()
            uniquewords = []
            totalwords = []
            for i in data:
                totalwords.append(i)
                if i not in uniquewords:
                    uniquewords.append(i)
            return len(uniquewords)/len(totalwords)

        def f2(data):
            global top5words
            global totalwords
            data = data.split()
            occurrences = {}
            for i in data:
                if i not in occurrences:
                    occurrences[i] = 0
                occurrences[i] += 1
            occurrences = dict(
                sorted(occurrences.items(), key=lambda x: x[1], reverse=True))
            key = list(occurrences.keys())
            top5 = []
            top5words = []
            for i in range(5):
                top5.append(occurrences[key[i]])
                top5words.append(key[i])

            totalwords = []
            for i in data:
                totalwords.append(i)
            return sum(top5)/len(totalwords)

        def f3(data):
            data = data.split(". ")

            for i in data:
                if i == "":
                    data.remove(i)
            sentences = len(data)
            f3num = []
            for i in data:
                i = i.split()
                if len(i) > 35 or len(i) < 5:
                    f3num.append(i)
            return len(f3num)/sentences

        def f4(data):
            data1 = data
            data1 = data1.split()
            data = data.split()
            totalwords = []
            for i in data:
                totalwords.append(i)
            chars = []
            for i in data1:
                if i.isalpha():
                    pass
                else:
                    chars.append(i)

            special_chars = []
            for i in chars:

                for j in i:
                    if j.isalpha():
                        i = i.replace(j, "")

                special_chars.append(i)
            f4num = []
            for i in special_chars:
                if len(i) > 1:
                    f4num.append(i)

            return len(f4num)/len(totalwords)

        def f5(data):
            data = data.split()
            totalwords = []
            for i in data:
                totalwords.append(i)

            if len(totalwords) > 750:
                return 1
            else:
                return 0
        score = 4+f1(data)*6+f2(data)*6-f3(data)-f4(data)-f5(data)
    with open("3_3_output.txt", "a") as f2:
        f2.write(f'File Name: file{i+1} \n')
        f2.write(f'Score: {score} \n')
        f2.write(f'Top 5 most used words: {top5words}\n')
        words = []
        for i in range(5):
            n = random.randint(1, 10)
            w1 = totalwords[n]
            words.append(w1)
        f2.write(f'5 randomly generated word: {words}')
        f2.write(f"\n")
        f2.write(f"\n")
