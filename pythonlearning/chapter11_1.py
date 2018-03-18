sp=['~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',':',';','[',']','{','}','|','\\']
temp=input('Please enter your password:')
def spacej(n):
    count=0
    for each in n:
        if each.isspace()==True:
            count+=1
    if count>0:
        return False
    else:
        return True
def atnum(n):
    count=0
    for each in n:
        if each.isnumeric()==True:
            count+=1
    if count>0:
        return False
    else:
        return True
def atal(n):
    count=0
    for each in n:
        if each.isalpha()==True:
            count+=1
    if count>0:
        return False
    else:
        return True
def specialsign(n):
    count=0
    for each in n:
        if each in sp:
            count+=1
    if count>0:
        return False
    else:
        return True
# lower password
while spacej(temp)==False:
    temp=input('password could not include space, please set again:')
else:
    if atal(temp)==True or atnum(temp)==True or len(temp)<=8:
        print('Assessment of safety: low')
        print('''please improve your level of safety:
    1. The password is composed of number, alphabet and special sign
    2. Alphabet is located in the head of password
    3. The length of password could not be less than 16''')
# middle password
    else:
        if (temp.isalpha()==False and specialsign(temp)==True) or (specialsign(temp)==False and atal(temp)==True)\
        or (specialsign(temp)==False and atnum(temp)==True) and len(temp)>=8:
                print('Assessment of safety: middle')
                print('''please improve your level of safety:
            1. The password is composed of number, alphabet and special sign
            2. Alphabet is located in the head of password
            3. The length of password could not be less than 16''')
        else:
            if temp.isalnum()==False and specialsign(temp)==False and len(temp)>=16 and temp[0].isalpha()==True:
                print('Assessment of safety: high')
                print('continue to keep')
            else:
                print('Assessment of safety: middle-high')
                print('need some change')


