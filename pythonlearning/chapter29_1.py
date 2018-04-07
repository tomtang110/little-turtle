def file_compare(temp,temp1):
    f1=open(temp,'r')
    f2=open(temp1,'r')
    count=0
    diff=[]
    
    for i in f1:
        count+=1
        line2=f2.readline()
        if i != line2:
            diff.append(count)
    f1.close()
    f2.close()
    return diff
temp=input('Please input the name of first document:')
temp1=input('Please input the name of second document:')
f=file_compare(temp,temp1)
print('The total difference:'+str(len(f)))
for i in range(len(f)):
    print('The '+str(f[i]) +'row is different' )


