temp=int(input('please input a mark:'))
if 100>=temp>90:
    print('A')
elif 90>=temp>80:
    print('B')
elif 80>=temp>60:
    print('C')
elif 0<temp<60:
    print('D')
else:
    print('wrong number')
