amt=int(input("Electricity consumption in Kw/h"))

if amt<100:
    amt=amt*100
    print(amt)
elif 101<amt<200:
    amt=amt*200
else:
    amt=amt*300

print(amt)