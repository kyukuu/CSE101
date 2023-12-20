population = [50, 1450, 1400, 1700, 1500, 600, 1200]


def population_in_year_n(n):
    gr = 2.5
    population = [50, 1450, 1400, 1700, 1500, 600, 1200]
    gr_new = gr
    for i in range(n):
        population_n = []
        for j in population:
            ans = j + (j*(gr/100))
            population_n.append(ans)
            gr = gr-0.4
        population = population_n
        gr_new = gr_new-0.1
        gr = gr_new

    return (population)


def population_sum(n):
    sum = 0
    for i in population_in_year_n(n):
        sum = sum+i

    return sum


flag = True
n = 0
years = 0
while flag:
    if population_sum(n) > population_sum(n+1):
        ans = population_sum(n)
        flag = False
    else:
        n += 1
        years = n+1


print("Current total population of the world: ", population_sum(0), "Million")
print("Years after which maximum population is reached : ", years-1)
print("Value of maximum population: ", ans, "Millions")
