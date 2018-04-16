def introd(temp):
    import os
    os.chdir(temp)
    document=os.listdir()
    countavi=0
    countpgn=0
    counttxt=0
    countpy=0
    countdocx=0
    counttang=0
    countdocu=0
    document_num=len(document)
    for each_docu in range(document_num):
        each_docu1=os.path.split(os.getcwd()+'/'+document[each_docu])
        if '.avi' in each_docu1[1]:
            countavi+=1
        elif '.pgn' in each_docu1[1]:
            countpgn+=1
        elif '.txt' in each_docu1[1]:
            counttxt+=1
        elif '.py' in each_docu1[1]:
            countpy+=1
        elif '.docx' in each_docu1[1]:
            countdocx+=1
        elif '.tang' in each_docu1[1]:
            counttang+=1
        elif '.' not in each_docu1[1]:
            countdocu+=1
    return (countavi,countpgn,counttxt,countpy,countdocx,counttang,countdocu)
temp=input('Please input your direction:')
ab=introd(temp)
a='/Users/tomtang110/desktop/documentstudy/zhuzhu/kaer'
print('Under this direction, the .avi document has '+str(ab[0]))
print('Under this direction, the .pgn document has '+str(ab[1]))
print('Under this direction, the .txt document has '+str(ab[2]))
print('Under this direction, the .py document has '+str(ab[3]))
print('Under this direction, the .docx document has '+str(ab[4]))
print('Under this direction, the .tang document has '+str(ab[5]))
print('Under this direction, the .docu document has '+str(ab[6]))



