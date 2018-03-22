def narcissus():
    result=0
    a=[str(i) for i in range(100,1000)]
    for each in a:
        temp=each
        if int(temp[0])**3+int(temp[1])**3+int(temp[2])**3==int(temp):
            print(temp)
narcissus()


