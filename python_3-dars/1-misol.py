# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 08:49:22 2021

@author: Asadullo
"""

'''
a=5
b=3.1489
c=True
d='hello'
print("a{:.05d} b={:.3f} c={} d={}".formating(a,b,c,d[0]))
print(2>3 and 1==1)
print(2>3 or 1==1)
print(not (2>3) and 1==1)
print(not(2>3) or 1==1)
print(not (2>3 and 1==1))
print(not(4>3 or 2!=1))
print(not(0.0000001))
#%%string
a='hello word'
#a[0]='K'
print(a)
print('string uzunligi=',len(a))'''
#%%LISTLAR 
list1=['hello',12,34.54,False]
list2=[]
list2=list()
print(list1,list2,sep='\n')
#%% SORTING LIST 
list1=[9,8,7,4,5,6,1,1,2,3]
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list2=['Dilshod','Aziza','aziz','Shodmon','Rahima']
list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)
print(list2[0][::-1])


list3=[True,False,12,7,86,6.25]
list3.sort()
print(list3)
#%%
ls1=[1,2,3]
ls2=[4,5,6]
ls3=[7,8,9]
print(ls1+ls2+ls3)

ls4=[ls1,ls2,ls3]
print(ls4[0][2])
print(ls4[1][0])
print(ls4[::-1])
s='Hello'
print(s[-1])
print(*s)


































