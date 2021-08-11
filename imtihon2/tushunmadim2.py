def tub(son):
    count=0
    for i in range (1,son):
        if son%i==0:
            count+=1
    if count==0:
        return 1
    else:
        return 0
lst=[]
son= int (input("kiriting\n>>"))
for i in range (1,son):
    b= son-i
    if (tub(i) and tub(b)) and b!=1 and i!=1:
        if i not in lst and b not in lst:
            lst.append(i)
            lst.append(b)
print(son,end="")
for a in range (0,len(lst),2):
    print("={}+{}".format(lst[a],lst[a+1]),end="")