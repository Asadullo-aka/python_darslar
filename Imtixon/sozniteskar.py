def func(soz,n):
    if n>=len(soz):
        pass
    else:
        print(soz[n:]+soz[0:len(soz)-n])
func(input("sozni kirinting\n>>"),int(input('sonni kiriting\>>')))