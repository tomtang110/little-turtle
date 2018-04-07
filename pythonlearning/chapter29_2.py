def showrow(temp,num):
    
    f=open(temp,'r')
    for i in range(num):
        print(f.readline())
temp=input('Please input the name of document:')
num=int(input('Please input the rows'))
showrow(temp,num)