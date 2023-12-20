#first 10 natural numbers
for i in range(1,11):
    print(i)

#first 10 even numbers

for i in range(2,21,2):
    print(i)

print("first 10 even number sin reverse order")
for i in range(20,1,-2):
    print(i)

print("program to print table of number accepted from user")

x=int(input())

for i in range(0,20):
    print(str(x) +" Multiplied by "+str(i)+" = "+ str(x*i))

print("program to print factorial of a number")

num=int(input())
i=0
fact=1
for i in range(1, num+1):
    fact=fact*i
    
print(fact)

print("program to find product of digits of a number accepted from user")

x=input("Enter a number: ")
str(x)
product=1
for i in x:
    product=product*int(i)
print(product)

print("program to print the sum of digits")
x=input("Enter a num")
i=0
sum=0
for i in str(x):
    sum=sum+int(i)
print(sum)

print("To check whether a number is prime or not")
