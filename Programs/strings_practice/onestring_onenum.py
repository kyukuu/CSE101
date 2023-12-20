str = input()
flag1 = False
flag2 = False
for i in str:
    if i.isalpha():
        flag1 = True
        break
for i in str:
    if i.isdigit():
        flag2 = True
        break


print(flag1 and flag2)


# def checkString(str):

#     # initializing flag variable
#     flag_l = False
#     flag_n = False

#     # checking for letter and numbers in
#     # given string
#     for i in str:

#         # if string has letter
#         if i.isalpha():
#             flag_l = True

#         # if string has number
#         if i.isdigit():
#             flag_n = True

#     # returning and of flag
#     # for checking required condition
#     return flag_l and flag_n


# # driver code
# print(checkString('thishasboth29'))
# print(checkString('geeksforgeeks'))
