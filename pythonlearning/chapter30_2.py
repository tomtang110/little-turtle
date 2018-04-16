def introd(temp,document):
    import os 
    os.chdir(temp)
    document1=os.listdir()
    if document in document1:
        print(os.getcwd())
    else:
        for each_document in document1:
            if os.path.isdir(temp+os.sep+each_document):
                temp1=temp+os.sep+each_document
                introd(temp1,document)
temp=input('Please input your direction:')
document=input('Please input the document:')
introd(temp,document)