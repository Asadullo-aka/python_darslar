# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:15:28 2021

@author: Asadullo
"""

list1=list(input("sonni kiriting:").split())
s1=set(list1)
print(s1)
list2=[]
for i in s1:
    if i in list1:
        list2.append(list1.count(i))
for i in s1:
    if max(list2)==list1.count(i):
        print(i,list1.count(i))
        
    