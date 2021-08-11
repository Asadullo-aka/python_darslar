a=str(input("soz kiriting\n>>"))
for i in range(len(a)+2):
    print(a[::2])
#%%
go=str(input('soz kiritng\n>>'))
m=0
n=0
c=0
for i in go:
    if i=='a'or i=='A' or i=='i' or i=='I' or i=='e' or i=='E' or i=="o'" or i=="O'" or i=='u' or i=="U" or i=='o' or i=='O':
        m+=1
    elif i==" ":
        n+=1
    else:
        c+=1
print(f">>unli harflar soni {m} \n>>probellar soni {n} \n>>undosh harflar soni {c} ")
#%%
a="salaom45987454 hello hello 454552"
l=list()
for i in a:
    if i=='1' or i=='2' or i=='3' or i=='4'or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
        continue
    else:
        l.append(i)
print(sorted(l))
#%%
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
#%%
a=input('soz kiritng\n>>')
b=len(a)
for i in a:
    if i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
           continue
    else:
        print(i*b)
        b-=1
        