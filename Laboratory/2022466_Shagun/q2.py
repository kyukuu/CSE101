salary = [1, 2, 3, 4,5,6,7,8,9,10]

def ans(salary):
    if len(salary) % 2 == 0:
        median = (salary[(len(salary)//2)-1]+salary[((len(salary))//2)])/2
    elif len(salary) % 2 == 1:
        median = salary[((len(salary)+1)//2)-1]
    else:
        print("invalid input")
    
    lessthanmedian=[]
    morethanmedian=[]
    for i in salary:
        if i<median:
            lessthanmedian.append(i)
        else:
            morethanmedian.append(i)
    
    avg1=sum(lessthanmedian)/len(lessthanmedian)
    avg2=sum(morethanmedian)/len(morethanmedian)
    return median,avg1,avg2
medianans,avg1,avg2=ans(salary)

print(f'Median: {medianans}')
print(f'Average for students whose salary less than median: {avg1}')
print(f'Average for students whose salary more than or equal to median: {avg2}')