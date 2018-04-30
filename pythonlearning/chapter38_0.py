class point1():
    def __init__(self):
        self.Ax=int(input('Please input the x axis of A:'))
        self.Ay=int(input('Please input the y axis of A:'))
class point2():
    def __init__(self):
        self.Bx=int(input('Please input the x axis of B:'))
        self.By=int(input('Please input the y axis of B:'))
class getline(point1,point2):
    def __init__(self):
        point1.__init__(self)
        point2.__init__(self)
    def calc(self):

        self.b=(self.Ax-self.Bx)**2+(self.Ay-self.By)**2
        self.L=self.b**(1/2)
        print(self.L)
g=getline()
g.calc()





