file = open("geeks2", 'w')

file.write("Parth teaches API")
file.close()

file = open("geeks2")
print(file.read())
