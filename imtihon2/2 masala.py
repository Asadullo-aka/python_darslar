a="sa 45 lom 77 95 hello"
lis=[]
lis2=[]
for i in a:
    if i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
      continue
    else:
        lis.append(i)
lis.sort()
print(lis)