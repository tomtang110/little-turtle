with open('something.txt','r') as f:
        a=[i for i in range(1,3)]
        for frontline in range(1):
            f.readline()
            for frontline1 in range(1,3):
                print(f.readline())
            f.close()