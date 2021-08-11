son =int (input ("son kiriting"))
lis=[]
for i in range (2,100):
    a=0
    for j in range (2,i):
        if i%j==0:
            a=+1
    if a==0:
        lis.append(i)
print(lis)
            