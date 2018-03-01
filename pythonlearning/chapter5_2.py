temp=int(input('请输入一个年份'))
if temp %4 == 0 and temp % 100 != 0:
    print('润年')
else:
    print('不是闰年')