for i in range(100,1000):
    anumber=i
    a=str(anumber)
    ba=int(a[0])
    bb=int(a[1])
    bc=int(a[2])
    if anumber==ba**3+bb**3+bc**3:
        print(i)
