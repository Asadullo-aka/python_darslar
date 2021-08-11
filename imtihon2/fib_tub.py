def tub_fib():
    a=int(input("sonni kirting\n>>"))
    l=list()
    for i in range (2,a**2):
        b=0
        for j in range(2,i//2+1):
            if i%j==0:
                b+=1
        if b==0:
            l.append(i)
    #print(l)
    #print(l[a-1])
    #a=int(input("son\n>>"))
    f1=1
    f2=1
    x=list()
    x.append(f1)
    x.append(f2)
    for i in range(3,100):
        f1,f2=f2,f1+f2
        if f2>=100:
            break
        x.append(f2)
    #print(x)
    #print(x[a])
    c=list()
    if len(l)>len(x):
        for i in range(len(x)):
            c.append(l[i])
            c.append(x[i])
    else:
        for i in range(len(l)):
            c.append(l[i])
            c.append(x[i])
    print(c)
tub_fib()

        
        
    
            
                