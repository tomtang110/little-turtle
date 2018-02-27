temp=int(input('请输入一个数'))
while temp:
    i=temp-1
    while i:
        print(' ',end='')
        i-=1
    j=temp
    while j:
        print('*',end='')
        j-=1
    print()
    temp-=1


