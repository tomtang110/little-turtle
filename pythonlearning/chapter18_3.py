def findstr(kk,hh):
    if hh in kk:
        count1=kk.count(hh)
        print(count1)
    else:
        print('the'+ hh+ 'is not in' +kk)
a='I love a girl who is 20 years old'
b='ov'
findstr(a,b)