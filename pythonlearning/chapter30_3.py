def video(temp):
    import os
    os.chdir(temp)
    ak0=os.listdir(temp)
    num0=len(ak0)
    a=['.avi','.wma']
    b=[]
    for each_docum in range(num0):
        if (a[1] in ak0[each_docum]) or (a[0] in ak0[each_docum]):
            b.append('temp'+ak0[each_docum]+'\n')
    with open('videolist.txt','w') as f:
        f1=f.writelines(b)
        f.close()
temp=input('Please input the direction:')
video(temp)

