import random
x_region=[0,10]
y_region=[0,10]



class turtle():
    #property
    def __init__(self):
        x_1=random.randint(x_region[0],x_region[1])
        y_1=random.randint(y_region[0],y_region[1])
        self.curren_location=[x_1,y_1]
        self.red=100
    # way
    def moving(self):
        stepnod=random.randint(1,2)
        rand=random.randint(0,1)
        direction=[-1,1]
        step=stepnod*direction[rand]
        ch_location=self.curren_location[rand]+step
        self.curren_location=self.curren_location
        self.curren_location[rand]=ch_location
        self.red-=1
        # x_axis
        if self.curren_location[0]>10:
            self.curren_location[0]=10
        elif self.curren_location[0]<0:
            self.curren_location[0]=0
        if self.curren_location[1]>10:
            self.curren_location[1]=10
        elif self.curren_location[1]<0:
            self.curren_location[1]=0
        return self.curren_location
    def eating(self):
        self.red+=20
        if self.red>100:
            self.red=100



class fish():
    #property
    def __init__(self):
        x_1=random.randint(x_region[0],x_region[1])
        y_1=random.randint(y_region[0],y_region[1])
        self.curren_location=[x_1,y_1]
    #way
    def moving(self):
        rand=random.randint(0,1)
        stepnod=1
        direction=[-1,1]
        step=stepnod*direction[rand]
        ch_location=self.curren_location[rand]+step
        self.curren_location=self.curren_location
        self.curren_location[rand]=ch_location
        # x_axis
        if self.curren_location[0]>10:
            self.curren_location[0]=10
        elif self.curren_location[0]<0:
            self.curren_location[0]=0
        if self.curren_location[1]>10:
            self.curren_location[1]=10
        elif self.curren_location[1]<0:
            self.curren_location[1]=0
        return self.curren_location
# class goldfish(fish()):
#     pass
# class shark(fish()):
#     pass
# class salmon(fish()):
#     pass
# class carp(fish()):
#     pass

def gameeat():
    turtle1=turtle()
    Fish=[]
    for i in range(10):
        f=fish()
        Fish.append(f)
    while 1:
        if turtle1.red==0:
            print('The turtle has been died')
            print('Game Over')
            break
        if len(Fish)==0:
            print('The fish has been eat out')
            print('Game Over')
            break
        turtle_location=turtle1.moving()
        for j in Fish[:]:
            if j.moving()==turtle_location:
                Fish.remove(j)
                turtle1.eating()
                print('The fish has been eat')
        
        
gameeat()

   









