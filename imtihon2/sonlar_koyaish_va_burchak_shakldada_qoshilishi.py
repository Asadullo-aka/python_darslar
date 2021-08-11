a=int (input('son_kiriting\n>>>'))
if a%2==0:
    for i in range (a,0,-1):
        for j in range(1,i+1):
            if j%2!=0:
                print(i,end='')
            else:
                print('+',i,'+',sep='',end='')
        print('=',i*i,sep='')
else:
    for i in range(1,a+1):
        for j in range(1,i+1):
            if j%2!=0:
                print(i,end='')
            else:
                print('+',i,sep='',end='')
        print('=',i*i,sep='')
        