class feiji:
    x=0
    def __init__(self):
        feiji.x+=1
    def __del__(self):
        feiji.x-=1

aa=feiji()
bb=feiji()
cc=feiji()
print(feiji.x)
del aa
print(feiji.x)

