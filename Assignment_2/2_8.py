with open("pages.txt") as f:
    data = f.readlines()
    links = []
    for i in data:
        i = i.split(":")
        list_innit = []
        i[1] = (str(i[1]).split())
        for j in i[1]:
            if j.startswith("URL"):
                list_innit.append(j)
        links.append(list_innit)
    urls = []
    init_importance = []
    for i in data:
        i = i.split(":")
        i[0] = i[0].split(",")
        urls.append(i[0][0])
        init_importance.append(i[0][1])

    for record in range(len(links)):
        for i in range(len(links[record])):
            links[record][i] = links[record][i].rstrip('.')
            links[record][i] = links[record][i].rstrip(',')
    sum_links = []
    for i in links:
        i = set(i)
        sum_links.append((len(i)))

    def url_index(ele):
        imp = []
        for i in range(len(links)):
            if ele in links[i]:
                imp.append(i)
        return imp

    def overall_importance(ele):
        overall = 0
        for i in url_index(ele):
            overall += float(init_importance[i])/sum_links[i]
        return round(overall, 5)
    dict = {}
    for i in urls:
        dict[i] = overall_importance(i)

    key = list(dict.keys())
    value = list(dict.values())

    for i in range(len(key)):
        for j in range(len(key)):
            if value[i] > value[j]:
                value[i], value[j] = value[j], value[i]
                key[i], key[j] = key[j], key[i]
    n = int(input('Enter n: '))
    if n <= len(key):
        for i in range(n):
            print(key[i], value[i])
    else:
        print(f'Only {len(key)} number of elements exist')
        for i in range(len(key)):
            print(key[i], value[i])
