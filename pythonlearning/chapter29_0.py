def something():
    temp=input('Please input the name of document:')
    with open(temp,'w') as f:
        temp1=input('Please input context[Individually input w as saving and quiting]:')
        f.write(temp1)
        temp3=input()
        if temp3==':w':
            f.close()
    pass
something()