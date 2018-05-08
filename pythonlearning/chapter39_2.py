class Pizza(object):
    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)
a=Pizza().mix_ingredients(2,3)
print(a)
import time
def sayhi():
    print('say hi')

def kk(func):
    def ko():
        a=time.clock()
        func()
        b=time.clock()
        print('this time is %d:'%(b-a))
    return ko
sayhi=kk(sayhi) 
sayhi()

class timeslong(object):
    def __init__(self,func):
        self.f = func
    def __call__(self):
        start = time.clock()
        print("It's time starting ! ")
        self.f()
        print("It's time ending ! ")
        end = time.clock()
        return "It's used : %s ." % (end - start)

@timeslong
def f():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)
    return y

print(f())
