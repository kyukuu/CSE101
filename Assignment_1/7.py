cost = int(input("Enter the cost of the laptop: "))
allowance = 20000
sf = 0.1
savings = allowance*sf
r = 0.5


def compound(principal, r, savings):
    month = 0
    flag = True
    while flag:
        CI = principal*(r/100)
        month = month+1
        if principal >= cost:
            break
        principal = principal+CI+savings
    left = principal-cost
    return (month, left)


month, left = compound(savings, r, savings)
print("You will be able to purchase the laptop after", month, "months. ")
print("The remaining savings are: ", left)
