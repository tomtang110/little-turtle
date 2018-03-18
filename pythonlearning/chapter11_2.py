temp=int(input('please enter an integer:'))
if temp != 'Q':
    print('decimal -> hex:'+'%#X' % temp)
    print('decimal -> octal:'+'%#o'% temp)
    print('decimal -> binary:'+bin(temp))
else:
    False
    
