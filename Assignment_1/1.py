# Please type single digit numbers as- 0 as 00,1 as 01, 2 as 02...
def unit(x):
    if x == "1":
        print("one")
    elif x == "2":
        print("Two")
    elif x == "3":
        print("Three")
    elif x == "4":
        print("Four")
    elif x == "5":
        print("Five")
    elif x == "6":
        print("Six")
    elif x == "7":
        print("Seven")
    elif x == "8":
        print("Eight")
    elif x == "9":
        print("Nine")
    elif x == "0":
        pass


def tens(x):
    if x == "0":
        pass
    elif x == "2":
        print("Twenty", end=" ")
    elif x == "3":
        print("Thirty", end=" ")
    elif x == "4":
        print("Forty", end=" ")
    elif x == "5":
        print("Fifty", end=" ")
    elif x == "6":
        print("Sixty", end=" ")
    elif x == "7":
        print("Seventy", end=" ")
    elif x == "8":
        print("Eighty", end=" ")
    elif x == "9":
        print("Ninety", end=" ")


number = input("Enter ")

split_number = [*number]

if number == "10":
    print("Ten")
elif number == "11":
    print("Eleven")
elif number == "12":
    print("Twelve")
elif number == "13":
    print("Thirteen")
elif number == "14":
    print("Fourteen")
elif number == "15":
    print("Fifteen")
elif number == "16":
    print("Sixteen")
elif number == "17":
    print("Seventeen")
elif number == "18":
    print("Eighteen")
elif number == "19":
    print("Nineteen")
elif number == "0":
    print("Zero")
else:
    tens(split_number[0])
    unit(split_number[1])
