def bin2(n):
    temp=[]
    result=''
    while n:
        duo=n%2
        n=n//2
        temp.append(duo)
    while temp:
        result+=str(temp.pop())
    return result
print(bin2(4))


