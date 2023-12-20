
with open("addrbook.txt") as f:
    data = f.read()
    phonebook = eval((str(data)))
    print(phonebook)

    def insert():
        namei = input("Enter name: ")
        addressi = input("Enter address: ")
        phonei = input("Enter phone number: ")
        emaili = input("Enter Email-ID: ")
        if namei in phonebook:
            ans = {"address": addressi,
                   "phone": phonei,
                   "email": emaili}
            phonebook[namei].append(ans)

        else:
            phonebook[namei] = [{"address": addressi,
                                "phone": phonei,
                                 "email": emaili}]

    def search():
        namei = input("Enter name: ")
        ans = []
        for name in phonebook:
            if namei in name:
                ans.append([name+": ", phonebook[name]])
        print(ans)

    def delete():
        namei = input("Enter the name: ")
        del phonebook[namei]

    def findwphone():
        phonei = input("Enter phone number: ")
        records = []
        for name in phonebook:
            for record in phonebook[name]:
                if record["phone"] == phonei:
                    records.append([name, record])
        for i in records:
            print(i[0]+':', i[1])

    def findwemail():
        emaili = input("Enter E-Mail ID: ")
        records = []
        for name in phonebook:
            for record in phonebook[name]:
                if record["email"] == emaili:
                    records.append([name, record])
        for i in records:
            print(i[0]+': ', i[1])
    print("To insert an entry, enter 1")
    print("To delete an entry, enter 2")
    print("To search for an entry using name, enter 3")
    print("To search for an entry using phone number, enter 4")
    print("To search for an entry using E-mail ID, enter 5")
    print("To exit, enter 6")

    flag = True
    while flag == True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            insert()
        elif choice == 2:
            delete()
        elif choice == 4:
            findwphone()
        elif choice == 5:
            findwemail()
        elif choice == 3:
            search()
        elif choice == 6:
            with open("addrbook.txt", "w") as f:
                f.write(str(phonebook))
            flag = False
        else:
            print("Invalid Input")

    # print(phonebook)
