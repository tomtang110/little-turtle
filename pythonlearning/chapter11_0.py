list1=['1.Just do it','2.exverything is possible','3.let programming change world','4.impossible is nothing']
list2=['4.addidas','3.little turtle','2.lining','1.Nike']
list3=[[name+':'+slogan[2:]] for name in list2 for slogan in list1 if name[0]==slogan[0]]
list3.sort()
for each in list3:
    print(each)
    
