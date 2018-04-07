def maxi_line(temp):
    count=0
    f=open(temp,'r')
    for each_line in f:
        count+=1
    f.close()
    return count
temp=input('Please input the name of document:')
aa=maxi_line(temp)
def checkup(temp, num1=0,num2=aa):
    with open(temp,'r') as f:
        a=[i for i in range(num1,num2)]
        for frontline in range(num1-1):
            f.readline()
        for frontline1 in range(num1,num2+1):
            print(f.readline())
        f.close()

    pass
nume=input('Please input the rows:')
split1=nume.split(':')
if split1[0]=='':
    num1=0
    num2=int(split1[1])
elif split1[1]=='':
    num2=aa
    num1=int(split1[0])
else:
    num1=int(split1[0])
    num2=int(split1[1])
checkup(temp,num1,num2)