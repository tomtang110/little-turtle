# def introd(direct):
#     import os 
#     os.chdir(direct)
#     document1=os.listdir()
#     for each_document in document1:
#         if os.path.isdir(direct+os.sep+each_document):
#             temp1=direct+os.sep+each_document
#             introd(temp1)
#         elif os.path.isfile(direct+os.sep+each_document):
#             print('heigege')
def introd(direct,substr):
    import os 
    os.chdir(direct)
    document1=os.listdir()
    for each_document in document1:
        if os.path.isdir(direct+os.sep+each_document):
            temp1=direct+os.sep+each_document
            introd(temp1,substr)
        else:
            if os.path.isfile(direct+os.sep+each_document):
                if ('.txt' in each_document):
                    print('hehe')
direct='/Users/tomtang110/Desktop/documentstudy'
substr='Tom'
introd(direct,substr)