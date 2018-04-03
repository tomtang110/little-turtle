def main():
    print('---Create account---:N/n')
    print('---Log on account---:E/e')
    print('---Log out account---:Q/q')
    dict1={}
    temp=input('please enter relative code:')
    while temp != 'Q' and temp != 'q':
        
        if temp=='N' or temp=='n':
            temp1=input('please input name of accounts:')
            if temp1 in dict1:
                temp1=input('The name has existed, please input name of accounts again:')
            else:
                temp2=input('Please input password:')
                dict1[temp1]=temp2
                print('Creating is successful,please log on')
        elif temp=='E' or temp=='e':
            temp1=input('please input name of accounts:')
            if temp1 in dict1:
                temp2=input('Please input password:')
                if temp2==dict1[temp1]:
                    print('Welcome to xxoo system, this is fate of world')
                else:
                    temp2=input('Password is wrong,Please input again')
            else:
                temp1=input('The account does not exist,please input again:')
        # elif temp=='q' or 'Q':
        #     print('---Thank you for using this program')
        temp=input('please enter relative code:')
    else:
        print('---Thank you for using this program')
main()