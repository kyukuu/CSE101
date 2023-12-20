import os
cwd=(os.getcwd())
print(cwd)
files=os.listdir()
for i in files:
    f=open(i)
    s=f.readlines()
    print(s)
# new_dir='C:\Users\braje\OneDrive\Desktop\Semester_1\Introduction_to_Programming\Laboratory\libraries_practice\kaku'
# os.mkdir(new_dir)
os_name=os.name()
print(os_name)