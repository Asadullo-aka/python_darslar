# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 18:54:40 2021

@author: user
"""


n=int(input("Nechta ma'lumot kiritmoqchisiz? \n:>>"))
lst=[]
for i in range(n):
    i=input("So'zni kiriting: ")
    if i[0]=="k":
        lst.append(i)
print(lst)