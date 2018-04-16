def introd(temp):
    import os 
    os.chdir(temp)
    document=os.listdir()
    document_num=len(document)
    for each_docu in range(document_num):
        ak1=document[each_docu]
        ak2=os.path.getsize(ak1)
        print(ak1+':'+str(ak2)+'Bytes')
temp=input('Please input your direction:')
introd(temp)