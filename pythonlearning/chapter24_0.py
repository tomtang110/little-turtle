def henoi(n,x,y,z):

    if n==1:

        print(x, '->',z)

    else:
        henoi(n-1, x,z,y)

        print(x, '->',z)

        henoi(n-1,y,x,z)
        
henoi(3,'X','Y','Z')