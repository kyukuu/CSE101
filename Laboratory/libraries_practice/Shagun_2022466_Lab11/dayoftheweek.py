import calendar
import datetime
data=input()
ans=datetime.datetime.strptime(data, '%Y-%m-%d').weekday()

print(calendar.day_name[ans])