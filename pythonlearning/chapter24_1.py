def people(n):
    if n==1:
        return 10
    else:
        return 2+people(n-1)
print(people(5))
