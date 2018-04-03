print('---welcome to contact book program---')
print('---1:look for contacts\' data---')
print('---2:insert new contacts---')
print('---3.delete contacts---')
print('---4.quit contacts book')
dict1={}
temp=int(input('please enter relative code:'))
while temp !=4 :
    
    if temp==1:
        temp1=input('please input name of contacts:')
        if temp1 in dict1:
            print('contact number:'+str(dict1[temp1]))
        else:
            print('The person is not in your contacts')
    if temp==2:
        temp1=input('please input name of contacts:')
        if temp1 in dict1:
            print('The name you input has existed->'+temp1+':'+str(dict1[temp1]))
            temp2=input('Do you want to modify telephone number of the contact(Yes/No):')
            if temp2==Yes:
                temp3=int(input('Please input the telephone number:'))
                dict1[temp1]=temp3
        else:
            temp3=int(input('Please input the telephone number:'))
            dict1[temp1]=temp3
    if temp==3:
        temp1=input('please input name of contacts:')
        dict1.pop(temp1)
    temp=int(input('please enter relative code:'))
else:
    print('---Thank you for using this program')





    