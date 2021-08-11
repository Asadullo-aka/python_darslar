# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 15:01:31 2021

@author: Asadullo
"""

l=[1,2,3,4,5,6,7,4,5,6,2,3,4,9]
b=[]
b.append(l.pop(0))
n=0
for i in l:
    if b[-1]<i:
        b.append(i)
    else:
        if len(b)>1:
            print(b)
            n+=1
        b=[]
        b.append(i)
print(b)
print(f"Ularning soni {n+1}ta")