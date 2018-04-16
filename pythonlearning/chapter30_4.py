# def statist(document,substr):
#     with open(document,'r') as f:
#         f1=f.readlines()
#         count0=0
#         for each_str in f1:
#             count0+=1
#             each_index=each_str.find(substr)
#             count1=0
#             list0=[]
#             while each_index>-1:
#                 count1+=each_index
#                 new=''.join([each_str[i] for i in range(len(each_str)) if i!=each_index])
#                 list0.append(count1)
#                 each_index=new.index(substr)+1
#             print('The keywords appear in '+str(count0)+' rows:'+'The '+str(list0)+' columns')
def statist(document,substr):
    with open(document,'r') as f:
        f1=f.readlines()
        # print(f1)
        count0=0
        for each_str in f1:
            count0+=1
            each_str_spl=each_str.split(' ')
            # print(each_str_spl)
            a=len(each_str_spl)
            # print(a)
            count1=0
            list0=[]
            for each_str in range(a):
                count1+=1
                if substr in each_str_spl[each_str]:
                    list0.append(count1)
            #     print(list0)
            # print(count1)
                   
            if list0 !=[]:
                print(document)
                print('The keywords appear in '+str(count0)+' rows:'+'The '+str(list0)+' columns')


def introd(direct,substr):
    import os 
    os.chdir(direct)
    document1=os.listdir()
    for each_document in document1:
        temp1=direct
        if os.path.isdir(temp1+os.sep+each_document):
            temp1=temp1+os.sep+each_document
            introd(temp1,substr)
        elif os.path.isfile(temp1+os.sep+each_document):
            if '.txt' in each_document:
                os.chdir(temp1)

                statist(each_document,substr)

substr=input('Please input keywords:')
direct=input('Please input your direction:')
# temp=input('Whether you need print the place of keywords?(Yes/No): ')

introd(direct,substr)

            



    