dictionary={
    "kya":"What",
    "pankha":"fan",
    "kitaab":"book"

}

print("the searchable words are: ", dictionary.keys())
x=input("Enter the word to be searched")

print("meaning of the word is: ", dictionary[x])

#better way, the one that avoids errors will be-

print("The meaning of the word is: ", dictionary.get(x))