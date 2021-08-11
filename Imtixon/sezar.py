for i in range(100,1000):
    a=i//100
    b=i%100//10
    c=i%10
    d=a+b+c
    if i%d==0:
        print(i)
    