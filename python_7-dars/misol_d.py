a=input("matnni kiriting: ")
list1=list(a[::])
print(list1)
list2=[]
o=""
y=""
t=""
list3=[]
h=0
for i in range(len(list1)-1):
    if list1[i]=='0' or list1[i]=='1' or list1[i]=='2' or list1[i]=='3' or list1[i]=='4' or list1[i]=='5' or list1[i]=='6' or list1[i]=='7' or list1[i]=='8' or list1[i]=='9':
        list2.append(list1[i])
        t=t+list1[i]
for e in range(len(list1)-1):
    if list1[e]==list2[0] and h==0:     
        p=e
        h=h+1
for u in range(len(list1)-1):
    if list1[u]==list2[len(list2)-1]:
        b=u+1
for x in range(p):
    o=o+list1[x]
for k in range(b,len(list1)):
    y=y+list1[k]
print(y[::-1],t,o[::-1],sep='')


