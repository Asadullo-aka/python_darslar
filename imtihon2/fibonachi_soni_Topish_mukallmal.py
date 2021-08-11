def fib(n):
    f1=1
    f2=1
    for i in range (3,n+1):
        f1,f2=f2,f1+f2
        #  ''' f1 f2 ning qiymatini ozlashtirib ketaveradi .f2 esa bir nigneski qiymatiga f2 ni yani ozini kiymatini qoshib ketaveradi '''
        print("f1=",f1,"f2=",f2)
    print(n,"chi fibonachi soni =",f2)
son=int(input("son\n>>"))
print(son,"chi fibonachi soni =")
fib(int(input("n\>>")))

        