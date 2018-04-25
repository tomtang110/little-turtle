class rectangle():
    #property
    length=int(input('Please input the length:'))
    width=int(input('Please input the width:'))
    #way
    def getrct(self):
        print('The length:'+str(self.length)+'\n'+'The width:'+str(self.width))
    def getarea(self):
        l=self.length
        w=self.width
        A=l*w
        print('The area:'+str(A))
g=rectangle()
g.getarea()
g.getrct()
