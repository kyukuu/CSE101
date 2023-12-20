shagun_dictionary = {'parth': [{'address': 'Dwarka', 'phone': '9810345677', 'email': 'maybe@constantcontemplation.ac.in'}, {'address': 'IIITD', 'phone': '9810345678', 'email': 'maybe@constantcontemplation.ac.in'}], 'swarnima': [{'address': 'Ahmedabad', 'phone': '9867485763', 'email': 'who@kyuku.com'}], 'arnav': [{'address': 'Chennai', 'phone': '7876656234',
                                                                                                                                                                                                                                                                                                                           'email': 'hahaha@wohoo.com'}], 'sha': [{'address': 'react', 'phone': 'whi', 'email': 'where'}], 'hash': [{'address': 'tank', 'phone': '42', 'email': '@'}], 'shashwat jha': [{'address': 'whyamitheonegettingdeleted', 'phone': 'meinnahibataunga', 'email': 'something@iiitd.ac.in'}], 'Akshat': [{'address': 'kargil', 'phone': '9821442378', 'email': 'whatisip@nda.in'}]}
parth_dictionary = {'parth': [{'address': 'dwarka', 'phone': '9910123456', 'email': 'decent@ip.com'}, {'address': 'pitampura', 'phone': '1234567890', 'email': 'rejected@flux.com'}], 'shagun': [{'address': 'punjabibagh', 'phone': '9876543210', 'email': 'god@hci.com'}, {
    'address': 'okhla', 'phone': '1234509876', 'email': 'kaaku@home.com'}], 'sidhartha': [{'address': 'ghaziabad', 'phone': '9910654321', 'email': 'chill@iiitd.com'}], 'tanishk': [{'address': 'faridabad', 'phone': '991024680', 'email': 'tanni@college.com'}]}

for i in parth_dictionary:
    str = (f'{i}: {parth_dictionary[i]}')
    if i in shagun_dictionary:
        for j in parth_dictionary[i]:
            shagun_dictionary[i].append(j)
    else:
        shagun_dictionary[i] = parth_dictionary[i]

print(shagun_dictionary)
