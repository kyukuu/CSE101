file = open("geeks2", "a")
file.write("This line will be appended if everything goes well")
file.write("maybe")
file.close()

file = open("geeks2")
print(file.read())
file.close()
