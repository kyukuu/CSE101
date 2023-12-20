import datetime

d1=datetime.date(2023,1,17)
print(d1)
# d=datetime.datetime.date.today()
# print(d)
d2=(datetime.datetime.now())
print(d2)
print(datetime.datetime.timestamp(d2))

d1=datetime.datetime(2022,2,13,22,12,33)
d2=datetime.datetime(2023,1,22,1,2,55)

d3=d2-d1
print(d3)
now=datetime.datetime.now()
dt1=now.strftime("%m/%d/%Y , %H:/%M:%S")
print(dt1)
dt2= "17 february, 2023"
dates=datetime.datetime.strptime(dt2,'%d %B, %Y')
print(dates)