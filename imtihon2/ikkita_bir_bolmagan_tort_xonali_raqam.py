for i in range (1000,10000):
    a=i//1000
    b=i//100%10
    c=i//10%10
    d=i%10
    if a==b or a==d or a==c or b==c or b==d or c==d:
        pass
    else:
        print(i,end=" ")