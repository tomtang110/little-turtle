def sum1(*paragm,base=3):
    result=0
    for each in paragm:
        result+=each
    if list(paragm).pop()==5:
        base=5
        return result
    else:
        result1=result*base
        return result1
print(sum1(1,2,3,4))
