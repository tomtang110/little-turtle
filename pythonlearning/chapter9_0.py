temp=input('please enter your password:')
count=3
while temp != '2345' and 1<count<=3:
    if '*' in temp:
        temp=input('* cannot include in password,please enter again:') 
    else:
        a=str(count-1)
        temp=input('wrong answer, you left '+a+' opportunities: ')
        count-=1
else:
    if temp=='2345':
        print('right answer')
        print('in process')
    else:
        print('card is locked')

            
            
    


