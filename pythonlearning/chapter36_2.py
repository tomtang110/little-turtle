class ticket():
    #property
    Nticket=100
    Weekend=Nticket*1.2
    boyticket=Nticket/2
    def calculationweek(self):
        try:
            a0=int(input('Please input the number of adults:'))
            
        except ValueError:
            a0=0
        try:
            a1=int(input('Please input the number of children:'))
        except ValueError:
            a1=0
        Tprice=a0*self.Nticket+a1*self.boyticket
        return Tprice
g=ticket()
print(g.calculationweek())

        
