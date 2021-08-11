# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 13:18:10 2021

@author: Asadullo
"""

A,B=10,20
(A,B)=(B,A)
print(A,B)
A,B,C=10,20,30
(A,B,C)=(C,B,A)
print(A,B,C)
S=12
Q=S//10
F=S%10
print('ONLIK',Q)
print('birlik',F)
print('yigindi: ',Q+F)
a=12
print('a=',a)
s=a%10
d=a//10
print('teskari ',s,d)
a=123
d=a//100
print('yuzlik',d)
s=a//10
print('onlik',s)
f=s%10
b=a%10
(d,f,b)=(b,f,d)
print(d,f,b)
(d,f,b)=(f,d,b)
print(d,f,b)
(d,f,b)=(d,b,f)
print(d,f,b)
print('yigindi ',d+f+b)
print('natija ',d,f,b)
(d,f,b)=(f,b,d)
print(d,f,b)
q=1999
print('q=',q)
s=q%1000
print('s=',s)
f=s%100
print('f=',f)
d=f%10
print('d=',d)
