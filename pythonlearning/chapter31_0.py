def pickler():
    import pickle
    with open('aaa.txt','r') as f1:
        ak0=f1.readlines()
    list0=[]
    list00=[]
    for each in ak0:
        if 'Tom:' in each:
            ak1=each.strip('Tom:')
            list0.append(ak1)
        if 'Lucy:' in ak0:
            ak2=eacj.strip('Lucy:')
            list00.append(ak2)
    with open('boy_*.txt','wb') as b1:
        pickle.dump(list0,b1)
    with open('girl_*.txt','wb') as g1:
        pickle.dump(list00,g1)
    f1.close()
    b1.close()
    g1.close()

pickler()






