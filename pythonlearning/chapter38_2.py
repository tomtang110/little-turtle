class A:
    def get_a(self):
        print('a')

class B:
    def get_b(self):
        print('b')

class C(): 
    pass
C. __bases__+=(A,B,)


