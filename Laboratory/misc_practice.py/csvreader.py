# import csv

# with open("data.csv") as f:
#     data=csv.DictReader(f)
#     print(data)
# import csv
# header=["Name","Rollno"]
# mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'}, 
#          {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'}, 
#          {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'}, 
#          {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'}, 
#          {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'}, 
#          {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}] 
# filename="university_records.csv"

# with open(filename,"w") as csvfile:
#     data=csv.writer(csvfile)
#     data.writerow(header)
#     data.writerows(rows)
import csv
fields = ['name', 'branch', 'year', 'cgpa'] 
mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'}, 
         {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'}, 
         {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'}, 
         {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'}, 
         {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'}, 
         {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}] 


with open ("unirecs.csv","w") as f:
    data=csv.DictWriter(f,fieldnames=fields)
    data.writeheader()
    data.writerows(mydict)