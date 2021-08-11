list1=[1,2,3,4,5,5,6,7,8,9,4,5,6,7]
list2=[]
for i in list1:
   if i not in  list2:
       list2.append(i)
print(list2)       
a= [f for f in range(1,10)if  f%2==0]
print(a)