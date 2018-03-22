def narcissusnum():
    for i in range(100,1000):
        n=str(i)
        count=0
        for k in n:
            count+=int(k)**3
        if count==i:
            print(i)
narcissusnum()


