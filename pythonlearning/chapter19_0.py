def statistic(*h):
    e=len(h)
    for f in range(e):  
        a=0
        b=0
        c=0
        d=0
        for k in h[f]:
            if k.isalpha()==True:
                a+=1
            else:
                if k.isnumeric()==True:
                    b+=1
                else:
                    if k.isspace()==True:
                        c+=1
                    else:
                        if k.isalpha()==False and k.isnumeric()==False and k.isspace()==False:
                            d+=1
        print('CC:'+str(f+1)+' A:'+str(a)+' B:'+str(b)+' C:'+str(c)+' D:'+str(d))        
aa='I love 1 girl ()'
bb='woshidabendan  *() 123'
cc='ad*wqqweqwenk024423+)(&^^   8isd**6'
dd='29&*^^jjhadb hj&&6677 uh$##4'
statistic(aa,bb,cc,dd)
                    

