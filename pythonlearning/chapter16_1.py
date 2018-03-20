def sum1(n):
    result=0
    kk=list(n)
    for each in kk:
        if type(each)==int or type(each)==float:
            result+=each
        else:
            result+=0
    return result
a=[1,2,3,4,'kk']
print(sum1(a))


