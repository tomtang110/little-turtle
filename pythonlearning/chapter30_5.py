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
                print('The keywords appear in '+str(count0)+' rows:'+'The '+str(list0)+' columns')
document='aaa.txt'
substr='Tom'
statist(document,substr)