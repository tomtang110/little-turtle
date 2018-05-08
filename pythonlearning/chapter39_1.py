class Stack():
    def __init__(self,start=[]):
        self.stack=start
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            print('stack is empty')
    def push(self,something):
        self.stack.append(something)
    def pop(self):
        if not self.stack:
            self.stack.pop()
        else:
            print('stack is empty')
    def base(self):
        if self.stack:
            return self.stack[0]
        else:
            print('stack is empty')
a=Stack([])
a.push('a')
a.push('b')
a.push('c')
print(a.top())
print(a.base())


