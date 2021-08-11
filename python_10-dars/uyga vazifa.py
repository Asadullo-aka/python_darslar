# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 10:20:17 2021

@author: Asadullo
"""
a=int (input("boshlangich sonni kiritng: "))
b=int (input("boshlangich sonni kiritng: ") )
d=0
list1=[ i for i in range (a,b)]

for a in list1:
    d=d+a
s=int (input ("son : "))
if d%s==0:
    print('mojiza son')
else:
    print('eeeeeee')