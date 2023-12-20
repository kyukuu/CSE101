num=int(input())

initnum=num
altnum=0

while int(num)>0:
    rem= num%10
    altnum=altnum*10+rem
    num=num//10

if num==altnum:
    print('yes')
else:
    print('no')
    

        

