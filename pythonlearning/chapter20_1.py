def gcb(x,y):
    if y>0:
        t=x%y
        gcb(y,t)
        return  t
    else:
        return 1
print(gcb(6,4))