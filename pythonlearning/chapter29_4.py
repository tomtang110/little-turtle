def subword(temp,substr,substr1):
    with open(temp,'r') as f:
        count=0
        for each_line in f:
            ak=each_line.split(' ')
            for each_str in ak:
                if each_str==substr:
                    count+=1  
        print(temp+' have '+str(count)+' '+substr)
        content=[]
        ak1=f.seek(0,0)
        ak3=f.readlines()
        for i in ak3:
            count1=0
            ak2=i.split(' ')
            for k in ak2:
                count1+=1
                if k==substr:
                    ak2[count1-1]=substr1
            k2=' '.join(ak2)
            content.append(k2)      
        temp1=input('Are you willing to replace all'+substr+'?[Yes/No]:')
        k=open('aaa1.txt','w+')
        if temp1=='Yes':
            f2=k.writelines(content)
        k.close()
        f.close() 
       
temp=input('Please input the name of document:')
substr=input('Please input string or words needed to be replaced:')
substr1=input('Please input new strings and words:')
subword(temp,substr,substr1)

        


