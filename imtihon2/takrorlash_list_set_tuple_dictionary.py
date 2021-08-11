'''lis=list()
lis=[son for son in range(1,6)]
print(lis)
lis.append(20)
print(lis)
lis.insert(2, 100)
print(lis)
lis.sort()
print(lis)
lis.sort(reverse=True)
print(lis)
print(lis[5])
print(lis[::-1])
print(lis[3:])
print(lis[:3])
print(lis[1:5:2])
#%%
lis1=list()
for i in range (1,5):
    lis1.append(int(input("n=")))
print(lis1)'''
'''l=[i for i in range (1,11)]
#l.clear()
print(max(l),min(l))
print(len(l),sum(l))
print(l.count('1'))
#print(l.index("1"))
l.pop()
print(l)'''

'''l=[[1,2,3],[4,5,6],[7,8,9]]
a=0
for i ,j ,y in l:
    a+=i+j+y
print(a)'''
'''t1 =tuple()
t1=(1,2,3,4,5,5,6,5,5,5)
t2=10,20,30,40,50
print(t1,t2,sep="\n")
print(t1.count(5))
print(t2.index(40))'''
'''s1=set()
s1={1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9}
print(s1)
s2=list(s1)
print(s2)
s3={"s","s","a",}
print(s3)'''
#%%DICTIONARY
dic=dict()
dic={1:"salom",2:"salom",3:"boldi",4:"tamom"}
print(dic[1])
print(dic.keys())
print(dic.values())
print(dic.items())
for i in dic.keys():
    print(dic[i])
dic.pop(3)
print(dic)
dic.popitem()
print(dic)
print("____________________")
dic1={i for i in range (1,10)}
print(dic1)
dic2={1:23,"salom":4.56}
print(dic2)
dic2['hayr']="tamom"
dic2[1]="ozgardi"
print(dic2)

































