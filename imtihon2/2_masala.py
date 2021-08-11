b=list(input("matn kiritng:\n>>"))
lis2=[]
l=[]
ll=0
for i in b:
    if i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
        lis2.append(i)
        if len(lis2)==2:
            ll=lis2[0]+lis2[1]
            l.append(ll)
            lis2=[]
l.sort(reverse=True)
print(l)