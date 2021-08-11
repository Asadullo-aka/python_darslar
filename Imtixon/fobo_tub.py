z=[]
f1=1
f2=1
x=[]
x.append(f1)
x.append(f2)
for j in range(2,100):
        s=0
        for i in range(2,j):
            if j%i==0:
                s+=1
        if s==0:
            z.append(j)

for i in range(3,100):
        f1,f2=f2,f1+f2
        if f2>100:
            break 
        x.append(f2)
c=[]
if len(z)>len(x):
    for i in range(len(x)):
        c.append(z[i])
        c.append(x[i])
else:
    for i in range(len(z)):
        c.append(z[i])
        c.append(x[i])
print(c)
